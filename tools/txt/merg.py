import os, sys

districts = [
    '浦东新区',
    '金山区',
    '松江区',
    '嘉定区',
    '杨浦区',
    '闵行区',
    '徐汇区',
    '长宁区','黄浦区','虹口区','宝山区','普陀区','静安区'
]
def main( params ):
    assert( len(params)>1)
    args = params[1:]
    named_district = None
    for i in range( len(args)//3 ):
        sex, age, address = args[i*3], args[i*3+1], args[i*3+2]
        if address in districts:
            named_district = address;continue
        print( sex, age, f"{named_district}{address}")

if __name__ == '__main__':
    main( sys.argv)