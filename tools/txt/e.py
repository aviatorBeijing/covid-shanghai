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
    
    rsts = {}
    for e in args:
        fds = e.strip().split(',')
        if len(fds) == 2:
            fds = [ fds[0] ] + fds

        try:
            assert( len(fds) == 3 )
        except AssertionError as e:
            print( e )
            raise e
        if len(fds) == 3:
            num = int(fds[1])-int(fds[0]) + 1
            if fds[2] in rsts:
                rsts[ fds[2] ] += num
            else:
                rsts[ fds[2] ] = num
    
    # due to the change in the public annoucement format changed on 3/27: no sex, no age anymore. 
    for k,v in rsts.items():
        for i in range(0,v):
            print('无', 1, k )

if __name__ == '__main__':
    main( sys.argv)
