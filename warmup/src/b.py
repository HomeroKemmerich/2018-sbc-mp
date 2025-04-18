"""
time@2025-04-18: 01:05:36
"""
length = int(input())
coord_1 = input().split(' ')
coord_2 = input().split(' ')

coord_1 = list(map(lambda x : int(x), coord_1))
coord_2 = list(map(lambda x : int(x), coord_2))

def get_quadr(coord: list):
    print(coord)
    half = int(length / 2)

    if coord[0] <  half:
        if coord[1] > half:
            return 2
        return 1
    elif coord[0] >  half:
        if coord[1] > half:
            return 4
        return 3

quadr1 = get_quadr(coord_1)
quadr2 = get_quadr(coord_2)

print(quadr1)
print(quadr2)

if quadr1 == quadr2:
    print('N')
else:
    print('S')