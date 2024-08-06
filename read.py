ldata = []
def reader():
    filer = open("laptop.txt","r")
    for e in filer:
        data = (e.strip()).split(", ")
        ldata.append(data)
    for each in ldata:
        print(each,"\n")
