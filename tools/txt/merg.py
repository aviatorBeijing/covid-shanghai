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
    '长宁区','黄浦区','虹口区','宝山区','普陀区','静安区'
]
def main( params ):
    assert( len(params)>1)
    args = params[1:]
    named_district = None
    for addr in args:
        #sex, age, address = args[i*3], args[i*3+1], args[i*3+2]
        sex, age, address = '无', 1, addr
        if address in districts:
            named_district = address;continue
        if '、' in address:
            address = address.split('、')
        else:
            address = [address]
        for addr in address:
            print( sex, age, f"{named_district}{addr}")

if __name__ == '__main__':
    main( sys.argv)
