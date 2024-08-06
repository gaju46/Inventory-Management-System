#
# import datetime
# import wc
# import fwrite
# import read
# time = datetime.datetime.now()
#
# wc.menu()
#
# read.reader()
#
# venditem = []
# lprice = []
# def selllaptop(bill=None):
#      id = input("Enter the laptop id of the laptop to sell: ")
#      for eachitem in read.ldata:
#           if id == eachitem[0]:
#                qty = input("Enter the qtyity: ")
#                if int(qty) < int(eachitem[4]):
#                     eachitem[4] = str(int(eachitem[4])-int(qty))
#                     fwrite.fwriter(read.ldata)
#                     price = str(int(eachitem[3]) * int(qty))
#                     lprice.append(price)
#                     shipped = 500
#                     venditem.append([eachitem[1],eachitem[2],eachitem[5],eachitem[6],eachitem[3],qty])
#                     rvenditem = input("Enter yes")
#                     if rvenditem == "yes":
#                          break
#                     tprice = sum(int(price) for price in lprice)
#                     tpvat = str((tprice + (tprice * 13/100)) + shipped)
#                     cliname = input("Enter Your Name")
#                     cliaddress = input("Enter Your Address")
#                     clinumber = input("Enter Your Number")
#                     bills = open(str(time.hour)+str(time.minute)+cliname+".txt","w")
#                     billf = "\n***********************************\n"+"            Invoice                \n\n"+"Date: "+ time.strftime("%Y-%m-%d %H:%M:%S")+"\n"+"Customer Name: "+cliname+"\n"+"Customer Address: "+cliaddress+"\n"+"Customer Phone Number: "+clinumber+"\n"+"***********************************\n"
#                     sbill= "\n"+"Shipping: "+str(shipped)+"\n"+"Total Price without Vat and Shipping: "+ str(tprice)+"\n"+"Total Price with Vat and Shipping: "+ str(tpvat)+"\n***********************************\n"
#                     print(billf)
#                     for q in venditem:
#                          print(q,"\n")
#                     print(bill.f)
#                     bills.write(billf)
#                     for q in venditem:
#                          bills.write(q[0]+q[1]+q[2]+q[3]+q[4]+q[5])
#                          bills.write("\n")
#                     bills.write(bill.f)
#                     break
#
#
#                elif int(qty) == int(eachitem[4]):
#                      read.ldata.remove(eachitem)
#                      fwrite.fwriter(read.ldata)
#                      price = str(int(eachitem[3]) * int(qty))
#                      lprice.append(price)
#                      shipped = 500
#                      venditem.append([eachitem[1],eachitem[2],eachitem[5],eachitem[6],eachitem[3],qty])
#                      rvenditem = input("Enter yes")
#                      if rvenditem == "yes":
#                           break
#                      tprice = sum(int(price) for price in lprice)
#                      tpvat = str((tprice + (tprice * 13/100)) + shipped)
#                      cliname = input("Enter Your Name")
#                      cliaddress = input("Enter Your Address")
#                      clinumber = input("Enter Your Number")
#                      bills = open(str(time.hour)+str(time.minute)+cliname+".txt","w")
#                      billf = "\n***********************************\n"+"            Invoice                \n\n"+"Date: "+ time.strftime("%Y-%m-%d %H:%M:%S")+"\n"+"Customer Name: "+cliname+"\n"+"Customer Address: "+cliaddress+"\n"+"Customer Phone Number: "+clinumber+"\n"+"***********************************\n"
#                      sbill= "\n"+"Shipping: "+str(shipped)+"\n"+"Total Price without Vat and Shipping: "+ str(tprice)+"\n"+"Total Price with Vat and Shipping: "+ str(tpvat)+"\n***********************************\n"
#                      print(billf)
#                      for q in venditem:
#                           print(q,"\n")
#                      print(bill.f)
#                      bills.write(billf)
#                      for q in venditem:
#                           bills.write(q[0]+q[1]+q[2]+q[3]+q[4]+q[5])
#                           bills.write("\n")
#                      bills.write(bill.f)
#                      break
#                else:
#                      print("The qtyity you entered is higher than our stocks")
#                      break
#
#
#      else:
#          print("invalid")

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
    laptop_id = input("Enter the laptop id of the laptop to sell: ")
    for item in read.ldata:
        if laptop_id == item[0]:
            quantity = int(input("Enter the quantity: "))
            if quantity <= int(item[4]):
                item[4] = str(int(item[4]) - quantity)
                fwrite.fwriter(read.ldata)
                price = str(int(item[3]) * quantity)
                lprice.append(price)
                shipped = 500
                venditem.append([item[1], item[2], item[5], item[6], item[3], str(quantity)])
                rvenditem = input("Enter 'yes' to continue: ")
                if rvenditem.lower() == "yes":
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
                    sbill = "\n" + "Shipping: " + str(shipped) + "\n" + "Total Price without Vat and Shipping: " + str(
                        tprice) + "\n" + "Total Price with Vat and Shipping: " + str(tpvat) + "\n***********************************\n"
                    print(billf)
                    for q in venditem:
                        print(q, "\n")
                    print(billf)
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


# def buyitem():
#     Iname = input("Enter the Laptop name")
#     ibrand = input("Enter the Laptop brand")
#     iprocessor = input("Enter the Laptop processor")
#     lgrcs = input("Enter the Laptop graphics")
#     iprice = input("Enter the Laptop price")
#     iquantity = input("Enter the No of laptops to be purchased")
#     for etop in read.ldata:
#         if Iname == etop[1] and ibrand == etop[2] and iprice == etop[3] and iprocessor == etop[5] and lgrcs == etop[6]:
#             print("Laptop already exists so qtyity will be updated.")
#             etop[4] = str(int(etop[4])+int(iquantity))
#             fwrite.fwriter(read.ldata)
#             price = str(int(etop[3]) * int(iquantity))
#             lprice.append(price)
#             shipped = 500
#             venditem.append([etop[1],etop[2],etop[5],etop[6],etop[3],iquantity])
#             rvenditem = input("Enter yes")
#             if rvenditem == "yes":
#                  break
#             tprice = sum(int(price) for price in lprice)
#             tpvat = str((tprice + (tprice * 13/100)) + shipped)
#             cliname = input("Enter Your Name")
#             cliaddress = input("Enter Your Address")
#             clinumber = input("Enter Your Number")
#             bills = open(str(time.hour)+str(time.minute)+cliname+".txt","w")
#             billf = "\n***********************************\n"+"            Invoice                \n\n"+"Date: "+ time.strftime("%Y-%m-%d %H:%M:%S")+"\n"+"Customer Name: "+cliname+"\n"+"Customer Address: "+cliaddress+"\n"+"Customer Phone Number: "+clinumber+"\n"+"***********************************\n"
#             sbill= "\n"+"Shipping: "+str(shipped)+"\n"+"Total Price without Vat and Shipping: "+ str(tprice)+"\n"+"Total Price with Vat and Shipping: "+ str(tpvat)+"\n***********************************\n"
#             print(billf)
#             for q in venditem:
#                  print(q,"\n")
#             print(bill.f)
#             bills.write(billf)
#             for q in venditem:
#                  bills.write(q[0]+q[1]+q[2]+q[3]+q[4]+q[5])
#                  bills.write("\n")
#             bills.write(bill.f)
#             break
#     else:
#          while True:
#              read.ldata.append([str(len(read.ldata)+1), Iname, ibrand, iprice, iquantity, iprocessor, lgrcs])
#              fwrite.fwriter(read.ldata)
#              price = str(int(iprice) * int(iquantity))
#              lprice.append(price)
#              shipped = 500
#              venditem.append([Iname,ibrand,iprocessor,lgrcs,iprice,iquantity])
#              rvenditem = input("Enter yes")
#              if rvenditem == "yes":
#                   break
#              tprice = sum(int(price) for price in lprice)
#              tpvat = str((tprice + (tprice * 13/100)) + shipped)
#              cliname = input("Enter Your Name")
#              cliaddress = input("Enter Your Address")
#              clinumber = input("Enter Your Number")
#              bills = open(str(time.hour)+str(time.minute)+cliname+".txt","w")
#              billf = "\n***********************************\n"+"            Invoice                \n\n"+"Date: "+ time.strftime("%Y-%m-%d %H:%M:%S")+"\n"+"Customer Name: "+cliname+"\n"+"Customer Address: "+cliaddress+"\n"+"Customer Phone Number: "+clinumber+"\n"+"***********************************\n"
#              sbill= "\n"+"Shipping: "+str(shipped)+"\n"+"Total Price without Vat and Shipping: "+ str(tprice)+"\n"+"Total Price with Vat and Shipping: "+ str(tpvat)+"\n***********************************\n"
#              print(billf)
#              for q in venditem:
#                   print(q,"\n")
#              print(bill.f)
#              bills.write(billf)
#              for q in venditem:
#                   bills.write(q[0]+q[1]+q[2]+q[3]+q[4]+q[5])
#                   bills.write("\n")
#              bills.write(bill.f)
#              break


def buy_item():
    Iname = input("Enter the Laptop name: ")
    ibrand = input("Enter the Laptop brand: ")
    iprocessor = input("Enter the Laptop processor: ")
    lgrcs = input("Enter the Laptop graphics: ")
    iprice = input("Enter the Laptop price: ")
    iquantity = input("Enter the No of laptops to be purchased: ")

    for etop in read.ldata:
        if (
            Iname == etop[1]
            and ibrand == etop[2]
            and iprice == etop[3]
            and iprocessor == etop[5]
            and lgrcs == etop[6]
        ):
            print("Laptop already exists, so quantity will be updated.")
            etop[4] = str(int(etop[4]) + int(iquantity))
            fwrite.fwriter(read.ldata)

            price = str(int(etop[3]) * int(iquantity))
            lprice.append(price)
            shipped = 500

            venditem.append([etop[1], etop[2], etop[5], etop[6], etop[3], iquantity])
            rvenditem = input("Enter yes: ")
            if rvenditem == "yes":
                break

            tprice = sum(int(price) for price in lprice)
            tpvat = str((tprice + (tprice * 13 / 100)) + shipped)

            cliname = input("Enter Your Name: ")
            cliaddress = input("Enter Your Address: ")
            clinumber = input("Enter Your Number: ")

            bill_filename = str(time.hour) + str(time.minute) + cliname + ".txt"
            with open(bill_filename, "w") as bill_file:
                billf = "\n***********************************\n" + "            Invoice                \n\n" + "Date: " + time.strftime(
                    "%Y-%m-%d %H:%M:%S"
                ) + "\n" + "Customer Name: " + cliname + "\n" + "Customer Address: " + cliaddress + "\n" + "Customer Phone Number: " + clinumber + "\n" + "***********************************\n"
                sbill = "\n" + "Shipping: " + str(shipped) + "\n" + "Total Price without Vat and Shipping: " + str(
                    tprice
                ) + "\n" + "Total Price with Vat and Shipping: " + str(tpvat) + "\n***********************************\n"
                print(billf)
                for q in venditem:
                    print(q, "\n")
                print(billf)
                bill_file.write(billf)
                for q in venditem:
                    bill_file.write("".join(q))
                    bill_file.write("\n")
                bill_file.write(billf)
            break
    else:
        while True:
            read.ldata.append(
                [
                    str(len(read.ldata) + 1),
                    Iname,
                    ibrand,
                    iprice,
                    iquantity,
                    iprocessor,
                    lgrcs,
                ]
            )
            fwrite.fwriter(read.ldata)

            price = str(int(iprice) * int(iquantity))
            lprice.append(price)
            shipped = 500

            venditem.append([Iname, ibrand, iprocessor, lgrcs, iprice, iquantity])
            rvenditem = input("Enter yes: ")
            if rvenditem == "yes":
                break

# def checkinput():
#      loop = True
#      while loop == True:
#          print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#          print("Given below are some of the options for you to carry out the need operations in the system")
#          print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#          print("\n")
#          print("press 1 to sale the laptop to customer.")
#          print("press 2 to purchase from Manufacturer.")
#          print("press 3 to Exit form the system.")
#          print("\n")
#          print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#          print("\n")
#
#          user_input = int(input("Enter the option to continue:  "))
#
#          print("\n")
#
#          if user_input == 1:
#              selllaptop()
#
#
#          elif user_input == 2:
#               buyitem()
#
#          elif user_input ==3:
#              loop = False
#              print("Thank you for using the system, have a good day Admin.")
#              print("\n")
#
#          else:
#              print("Your option", user_input,
#                     "does not seem to match as per our requirement, plese look at the option and try again, ")
#              print("\n")
# checkinput()

def check_input():
    while True:
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
            buy_item()
        elif user_input == 3:
            print("Thank you for using the system. Have a good day, Admin.")
            print("\n")
            break
        else:
            print("Your option", user_input, "does not match our requirements. Please try again.")
            print("\n")

check_input()
