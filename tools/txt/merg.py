import os, sys

districts = [
    '浦东新区',
    '崇明区',
    '金山区',
    '松江区',
    '嘉定区',
    '杨浦区',
    '闵行区',
    '徐汇区',
    '青浦区',
    '长宁区',
    '黄浦区',
    '虹口区',
    '宝山区',
    '普陀区',
    '静安区',
    '奉贤区'
]
def main( params ):
    filename = params[1]
    with open(filename, 'r') as fh:
        addresses = fh.read().split('\n')
    named_district = None
    cached = []
    for addr in addresses:
        #sex, age, address = addresses[i*3], addresses[i*3+1], addresses[i*3+2]
        sex, age, address = '无', 1, addr
        cached += [ address ] 
        if address in districts:
            named_district = address;continue
        if '、' in address:
            address = address.split('、')
        else:
            address = [address]
        for addr in address:
            try:
                assert( named_district )
            except AssertionError as e:
                print( named_district, addr )
                print( cached[::-1][:50] )
                raise e
            print( sex, age, f"{named_district}{addr}")

if __name__ == '__main__':
    main( sys.argv)
