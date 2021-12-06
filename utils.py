import csv

def csv2list(fn):
    csvfile = open (fn)
    csvreader= csv.reader(csvfile)
    l=[]
    for row in csvreader:
        line=[]
        for token in row:
            line.append(token)
        l.append(line)
    return l
