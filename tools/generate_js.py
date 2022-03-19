import requests
import pandas as pd
import numpy as np 

ds = '20220318'
caseFiles = [f'txt/{ds}/cases-nosyndrome-clear.txt', f'txt/{ds}/cases-confirmed-clear.txt']

for fn in caseFiles:
    # Txt to Dataframe
    items = []
    with open(fn, 'r') as fh:
        for line in fh.readlines():
            fds = line.strip().split(' ')
            items += [fds]
    items = list( 
        map( lambda e: {'sex': e[0], 'age': e[1], 'address':e[2]}, items)
    )
    df = pd.DataFrame.from_dict(items)

    # Fetch address
    """
    https://lbs.amap.com/api/webservice/guide/api/georegeo
    """
    cached = pd.DataFrame() 
    cached_file = 'cached/addresses.csv'
    try:
        cached = pd.read_csv(cached_file)
    except Exception as e:
        print( e )

    def get_by_address(addressLine):
        global cached
        if not cached.empty:
            if addressLine in list(cached.address):
                return cached[ cached.address==addressLine ]
        import os
        print( 'searching:', addressLine )
        mapsKey = os.getenv('GAODE_APIKEY')
        url = "https://restapi.amap.com/v3/geocode/geo?"
        url += f"city=上海"
        url += f"&address={addressLine}"
        url += f"&key={mapsKey}"
        resp = requests.get( url ).json()
        
        resp = resp['geocodes'][0]['location'].split(',')
        resp = {'lat': resp[1], 'lng': resp[0]}
        resp['address'] = addressLine
        ddf = pd.DataFrame.from_dict([ resp ])
        ddf = ddf[['address', 'lat', 'lng']]
        ddf.to_csv( cached_file, index=0)
        if not cached.empty:
            cached = pd.concat([ cached, ddf ], axis=0)
            cached.to_csv( cached_file, index=False )
        return resp 
    print('query address via bing api:', fn)
    df.address.apply(lambda e: get_by_address(e))

address_latlng_map = pd.DataFrame()
cases = []
for fn in caseFiles:
    with open( fn, 'r') as fh:
        for line in fh.readlines():
            fds = line.strip().split(' ')
            cases += [ {'sex': fds[0],
                        'age': fds[1], 
                        'address':fds[2],
                        'status': '确诊' if 'confirm' in fn else '无症状',
                        } ]
cases = pd.DataFrame.from_records( cases )
cases['age'] = cases.age.apply(lambda e: e.strip('岁'))
print( cases )

def _geo(d):
    x = address_latlng_map[ address_latlng_map.address==d ]
    return x.lat.iloc[0], x.lng.iloc[0]
def _lat(d): return _geo(d)[0]
def _lng(d): return _geo(d)[1]
address_latlng_map = pd.read_csv('cached/addresses.csv')
cases['lat'] = cases['address'].apply( lambda e:  _lat(e) )
cases['lng'] = cases['address'].apply( lambda e:  _lng(e) )

print('***')
cases['cnt'] = 1
count_cases = cases.groupby(['address','status']).agg(np.sum)[['cnt']].sort_values(by=['cnt'], ascending=False)
count_cases = count_cases['cnt']
count_cases = count_cases.to_dict()
count_cases_ = {}
for k,v in count_cases.items():
    address, status = k
    count_cases_[ address] = (status, v )

tmp = set()
codes = []
codes += [ 'var pushpinInfos = [];\n' ]
idx = 0
for i in range(0,cases.shape[0]):
    case = cases.iloc[i]
    if case.address in tmp: 
        continue
    tmp.add( case.address )
    status, cnt = count_cases_[case.address]
    codes += [ "pushpinInfos[%d] = {'lat': %s, 'lng': %s, 'title': \'%s\', 'description': \'%s\', 'count': %d};\n"%(
        idx, 
        case.lat,
        case.lng,
        case.address,
        f"{status} {cnt}人",
        cnt,
    ) ]
    idx+=1

with open('data.js','w') as fh:
    fh.writelines(codes)

