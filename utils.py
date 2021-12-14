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



def list2csv(l, fn):
    f=open(fn, 'w')
    write=csv.writer(f)
    for ll in l: # ll  list element, maybe I shoulda done le, not sure
        write.writerow(ll)
    

'''


# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

with open('GFG.csv', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(rows)

'''