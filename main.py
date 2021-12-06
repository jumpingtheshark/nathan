from utils import *


def union(left, right):
    u = []
    for el in left:
        for er in right:
            if el[0][0] == er[0][0]:
                u.append(er)
    return u


def left_not_right(left, right):
    l = []
    for el in left:
        match = False
        for er in right:
            if el[0][0] == er[0][0]:
                match = True
        if not match:
            l.append(el)
    return l

def main():
    left = csv2list('Left.csv')
    right = csv2list('Right.csv')
    print(left)
    print(right)
    # u = union(left, right)
    # print("union", u)
    l = left_not_right(left, right)
    print (l)


main()
