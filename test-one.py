import datetime
import wc
import fwrite
import read

time = datetime.datetime.now()

wc.menu()
read.reader()

venditem = []
lprice = []

def sell_laptop():
    try:
        laptop_id = input("Enter the laptop id of the laptop to sell: ")
        for item in read.ldata:
            if laptop_id == item[0]:
                quantity = int(input("Enter the quantity: "))
                if quantity <= int(item[4]):
                    item[4] = str(int(item[4]) - quantity)
                    fwrite.fwriter(read.ldata)
                    price = str(int(item[3].replace('$','')) * quantity)
                    lprice.append(price)
                    shipped = 500
                    venditem.append([item[1], item[2], item[5], item[6], item[3], str(quantity)])
                    rvenditem = input("Enter 'yes' to continue: ")
                    if rvenditem.lower() == "no":
                        break
                    tprice = sum(int(price) for price in lprice)
                      tpvat = str((tprice + (tprice * 13 / 100)) + shipped)
                    cliname = input("Enter Your Name: ")
                    cliaddress = input("Enter Your Address: ")
                    clinumber = input("Enter Your Number: ")
                    bill_filename = str(time.hour) + str(time.minute) + cliname + ".txt"
                    with open(bill_filename, "w") as bill_file:
                        billf = "\n***********************************\n" + "            Invoice                \n\n" + "Date: " + time.strftime(
                            "%Y-%m-%d %H:%M:%S") + "\n" + "Customer Name: " + cliname + "\n" + "Customer Address: " + cliaddress + "\n" + "Customer Phone Number: " + clinumber + "\n" + "***********************************\n"
                        billf = billf + "\n" + "Shipping: " + str(shipped) + "\n" + "Total Price without Vat and Shipping: " + str(
                            tprice) + "\n" + "Total Price with Vat and Shipping: " + str(tpvat) + "\n-----------------------------------------\n"
                        print(billf)
                        for q in venditem:
                            print(' '.join(q), "\n")
                        bill_file.write(billf)
                        for q in venditem:
                            bill_file.write("".join(q))
                            bill_file.write("\n")
                        bill_file.write(billf)
                else:
                    print("The quantity you entered is higher than our stock.")
                break
        else:
            print("Invalid laptop ID.")
    except Exception as e:
        print("An error occurred:", str(e))

def buyitem():
    Iname = input("Enter the Laptop name")
    ibrand = input("Enter the Laptop brand")
    iprocessor = input("Enter the Laptop processor")
    lgrcs = input("Enter the Laptop graphics")
    iprice = input("Enter the Laptop price")
    iquantity = input("Enter the No of laptops to be purchased")
    for etop in read.ldata:
        if Iname == etop[1]:
            print("Laptop already exists so quantity will be updated.")
            etop[4] = str(int(etop[4])+int(iquantity))
            fwrite.fwriter(read.ldata)
            price = str(int(etop[3].replace('$', '')) * int(iquantity))
            lprice.append(price)
            shipped = 500
            venditem.append([etop[1],etop[2],etop[5],etop[6],etop[3],iquantity])
            rvenditem = input("Enter yes")
            if rvenditem.lower() == "no":
                 break
            tprice = sum(int(price) for price in lprice)
            tpvat = str((tprice + (tprice * 13/100)) + shipped)
            cliname = input("Enter Your Name")
            cliaddress = input("Enter Your Address")
            clinumber = input("Enter Your Number")
            bills = open(str(time.hour)+str(time.minute)+cliname+".txt","w")
            billf = "\n***********************************\n"+"            Invoice                \n\n"+"Date: "+ time.strftime("%Y-%m-%d %H:%M:%S")+"\n"+"Customer Name: "+cliname+"\n"+"Customer Address: "+cliaddress+"\n"+"Customer Phone Number: "+clinumber+"\n"+"***********************************\n"
            billf = billf + "\n"+"Shipping: "+str(shipped)+"\n"+"Total Price without Vat and Shipping: "+ str(tprice)+"\n"+"Total Price with Vat and Shipping: "+ str(tpvat)+"\n***********************************\n"
            print(billf)
            for q in venditem:
                 print(' '.join(q),"\n")
            bills.write(billf)
            for q in venditem:
                 bills.write(q[0]+q[1]+q[2]+q[3]+q[4]+q[5])
                 bills.write("\n")
            bills.write(billf)
            break
    else:
         while True:
             read.ldata.append([str(len(read.ldata)+1), Iname, ibrand, iprice, iquantity, iprocessor, lgrcs])
             fwrite.fwriter(read.ldata)
             price = str(int(iprice) * int(iquantity))
             lprice.append(price)
             shipped = 500
             venditem.append([Iname,ibrand,iprocessor,lgrcs,iprice,iquantity])
             rvenditem = input("Enter yes")
             if rvenditem == "no":
                  break
             tprice = sum(int(price) for price in lprice)
             tpvat = str((tprice + (tprice * 13/100)) + shipped)
             cliname = input("Enter Your Name")
             cliaddress = input("Enter Your Address")
             clinumber = input("Enter Your Number")
             bills = open(str(time.hour)+str(time.minute)+cliname+".txt","w")
             billf = "\n***********************************\n"+"            Invoice                \n\n"+"Date: "+ time.strftime("%Y-%m-%d %H:%M:%S")+"\n"+"Customer Name: "+cliname+"\n"+"Customer Address: "+cliaddress+"\n"+"Customer Phone Number: "+clinumber+"\n"+"***********************************\n"
             billf = billf + "\n"+"Shipping: "+str(shipped)+"\n"+"Total Price without Vat and Shipping: "+ str(tprice)+"\n"+"Total Price with Vat and Shipping: "+ str(tpvat)+"\n***********************************\n"
             print(billf)
             for q in venditem:
                  print(' '.join(q),"\n")
             bills.write(billf)
             for q in venditem:
                  bills.write(q[0]+q[1]+q[2]+q[3]+q[4]+q[5])
                  bills.write("\n")
             bills.write(billf)
             break


def check_input():
    while True:
        try:
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Given below are some of the options for you to carry out the necessary operations in the system")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("\n")
            print("Press 1 to sell a laptop to a customer.")
            print("Press 2 to purchase from a manufacturer.")
            print("Press 3 to exit the system.")
            print("\n")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("\n")

            user_input = int(input("Enter the option to continue: "))

            print("\n")

            if user_input == 1:
                sell_laptop()
            elif user_input == 2:
                buyitem()
            elif user_input == 3:
                print("Thank you for using the system. Have a nice day. Visit again")
                print("\n")
                break
            else:
                print("Your option", user_input, "The data you enter does not match our requirements. Please fill the avaliable data and try again.")
                print("\n")

        except TypeError:
            print("Invalid input. Please enter a valid option.")
            print("\n")

check_input()
