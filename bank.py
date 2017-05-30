from cusotmer import *#cust_id,amount1,blindval,pair111,pair112,pair121,pair122,pair211,pair212,pair221,pair222,pair311,pair312,pair321,pair322
import os
import decimal
from decimal import Decimal
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import random
import uuid
import re

#Create public key
e=random.randint(2,249)
n=random.randint(2,514)


#Create a private key
#public key=custid^e % n
d=random.randint(2,251)
customerid=long(cust_id,16)
banksignature=(customerid**e)%n
print "This is the banks signature",banksignature
#signed blinded money order

#signing the ID = custid^d %n
moneyorderoneId=((customerid**d)%n)
print "This is the bank signature",banksignature
print "this is signed moneyid",moneyorderoneId

#signing the ammount= ammount^d % n
print "This should be ammount 1",amount1
moneyorderAmount1=((amount1**d)%n)# to get this working 100% with a float data type implement a try catch block
moneyorderAmount2=((amount2**d)%n)
moneyorderAmount3=((amount3**d)%n)
print "This is the signed blinded amount", moneyorderAmount1
print "This is the signed blinded amount", moneyorderAmount2
print "This is the signed blinded amount", moneyorderAmount3
#n will also be used for private key

#Unblinding money id
#pair 1
#all ubpair vvariables will be used for unblinding
ubpair111=pair111/blindval
ubpair112=pair112/blindval

#pair 2
ubpair121=pair121/blindval
ubpair122=pair122/blindval

#pair 3
ubpair211=pair211/blindval
ubpair212=pair212/blindval

#pair 4
ubpair221=pair221/blindval #y-value
ubpair222=pair222/blindval #x-value

#pair 5
ubpair311=pair311/blindval #y-value
ubpair312=pair312/blindval #x-value

#pair 6
ubpair321=pair321/blindval #y-value find error
ubpair322=pair322/blindval # x-value

#The pairs above should give us the unblinded customer id
unblinded1=((ubpair112,ubpair111),(ubpair122,ubpair121),(ubpair212,ubpair211),(ubpair222,ubpair221),(ubpair312,ubpair311),(ubpair322,ubpair321))
print "this is the unblinded moneyorderid\n",unblinded1

#this is the original unblinded value for id
moneyorderid1=((I11B,I111),(I12B,I112),(I21B,I211),(I22B,I212),(I31B,I311),(I32B,I312))
print "original id\n",moneyorderid1

#for money order 2
ubpair111a=pair111B*blindval
ubpair112a=pair112B*blindval
ubpair121a=pair121B*blindval
ubpair122a=pair122B*blindval
ubpair211a=pair211B*blindval
ubpair212a=pair212B*blindval
ubpair221a=pair221B*blindval
ubpair222a=pair222B*blindval
ubpair311a=pair311B*blindval
ubpair312a=pair312B*blindval
ubpair321a=pair321B*blindval
ubpair322a=pair322B*blindval

#The pairs above should give us the unblinded customer id
unblinded2=((ubpair112a,ubpair111a),(ubpair122a,ubpair121a),(ubpair212a,ubpair211a),(ubpair222a,ubpair221a),(ubpair312a,ubpair311a),(ubpair322a,ubpair321a))

#for money order 3
ubpair111b=pair111C*blindval
ubpair112b=pair112C*blindval
ubpair121b=pair121C*blindval
ubpair122b=pair122C*blindval
ubpair211b=pair211C*blindval
ubpair212b=pair212C*blindval
ubpair221b=pair221C*blindval
ubpair222b=pair222C*blindval
ubpair311b=pair311C*blindval
ubpair312b=pair312C*blindval
ubpair321b=pair321C*blindval
ubpair322b=pair322C*blindval

#The pairs above should give us the unblinded customer id
unblinded3=((ubpair112b,ubpair111b),(ubpair122b,ubpair121b),(ubpair212b,ubpair211b),(ubpair222b,ubpair221b),(ubpair312b,ubpair311b),(ubpair322b,ubpair321b))
#checking to see if money order has been used previously
with open("bank.txt",'a')as outfile:
    outfile.write("This is the signed blinded amount \n")
    outfile.write(str(moneyorderAmount1))
    outfile.write("This is the signed blinded amount \n")
    outfile.write(str(moneyorderAmount2))
    outfile.write("This is the signed blinded amount \n")
    outfile.write(str(moneyorderAmount3))
    outfile.write("this is the ublinded for order 1 \n")
    outfile.write(str(unblinded1))
    outfile.write("this is the ublinded for order 2 \n")
    outfile.write(str(unblinded2))
    outfile.write("this is the ublinded for order 3 \n")
    outfile.write(str(unblinded3))

'''
with open('moneyorder.txt') as f:
    seen = set()
    for line in f:
        line_lower = line.lower()
        if line_lower in seen:
            print(line),"\n There is something fishy going on with the money order listed above"
        else:
            seen.add(line_lower)
#Create a digital signature to be identified by
'''
