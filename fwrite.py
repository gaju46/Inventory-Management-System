def fwriter(laptopda):
    filew = open("laptop.txt", "w")
    for eachl in laptopda:
        print(eachl)
        filew.write(eachl[0]+", "+eachl[1]+", "+eachl[2]+", "+eachl[3]+", "+eachl[4]+", "+eachl[5]+", "+eachl[6]+"\n")
