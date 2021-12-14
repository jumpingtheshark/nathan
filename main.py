from utils import *
import os


def intersection(left, right):
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
            if el[0] == er[0]:
                match = True
        if not match:
            l.append(el)
    return l



def right_not_left(left, right):
    l = []
    for el in right:
        match = False
        for er in left:
            if el[0] == er[0]:
                match = True
        if not match:
            l.append(el)
    return l



def flush_file(path):
    path = os.getcwd()
    fl = ['union.csv', 'left-not-right.csv', 'right-not-left.csv', 'or.csv']
    for file in fl:
        try:
            os.remove(path + '/files/' + file)
        except:
            pass

def union(left, right):
    l=[]

    for el in left:
        for er in right:
            if el[0]==er[0]:
                if not contains_element(l, el[0]):
                    l.append(el)
            else:
                if not contains_element(l, el[0]):
                    l.append(el)
                if not contains_element(l, er[0]):
                    l.append(er)
    # now do a distinct
    # I still have to figure out how this whole set thing atually works
    # l=list(set(l))  - this did not work
    return l



def contains_element (l, e):
    for row in l:
        if row[0]==e:
            return True
    return False




def main():
    path = os.getcwd()
    flush_file(path)
    left = csv2list(path + '/files/Left.csv')
    right = csv2list(path + '/files/Right.csv')
    l = intersection(left, right)
    list2csv(l, path + "/files/union.csv")
    # print("union", u)
    l = left_not_right(left, right)
    list2csv(l, path + "/files/left-not-right.csv")
    l=right_not_left (left, right)
    list2csv(l,path + '/files/right-not-left.csv')
    l=union(left,right )
    list2csv(l, path + '/files/union.csv')



main()
