'''
Zach Aebersold
Ryan Goyette
Raghu Manthena
'''

import uuid
import random
from decimal import*
from random import randint

#Prompting customer to input 3 variables for 3 money orders
amount1 =int(input("please enter the amount of the first money order $"))
amount2 =float(input ("please enter the amount of the second money order $"))
amount3 =round(float(input ("please enter the amount of the third money order $")),2)

#Generating customer id and other random strings
cust_id=(uuid.uuid4().get_hex().upper()[0:16])
print "The customer id is",cust_id

#r values for money order 1
r1=random.randint(0,1000)
r2=random.randint(0,1000)
r3=random.randint(0,1000)

#r values for money order 2
r1B=random.randint(0,1000)
r2B=random.randint(0,1000)
r3B=random.randint(0,1000)

#r values for money order 3
r1C=random.randint(0,1000)
r2C=random.randint(0,1000)
r3C=random.randint(0,1000)

#!!!!!!!!Money order 1 secret split,bit commit and blind!!!!!!!!!!!!!!!!!!!!
#xor for s1 value in money order 1
I11=r1
I12=r1^ int(cust_id, 16)
s1=I12
#xor for s2 value
I21=r2
I22=r2^ int(cust_id, 16)
s2=I22
#xor for s3 value
I31=r3
I32=r3^ int(cust_id, 16)
s3=I32

I11B=r1B
I12B=r1B ^ int(cust_id, 16)
s1B=I12B
#xor for s2 value
I21B=r2B
I22B=r2B^ int(cust_id, 16)
s2B=I22B
#xor for s3 value
I31B=r3B
I32B=r3B^ int(cust_id, 16)
s3B=I32B

I11C=r1C
I12C=r1C^ int(cust_id, 16)
s1C=I12C
#xor for s2 value
I21C=r2C
I22C=r2C^ int(cust_id, 16)
s2C=I22C
#xor for s3 value
I31C=r3C
I32C=r3C^ int(cust_id, 16)
s3C=I32C
#Bit commit random number I111
I111=random.randint(0,1000)
I111B=random.randint(0,1000)
I111C=random.randint(0,1000)
#PRNG for I112
I112=random.randint(0,1000)
#Converting hex to int to get value of M
M11B=(I111)+(I112)+(I11)
I11B=M11B%amount1
print "This is for I11B",I11B

#I121 and I122 and s1
I121=random.randint(0,1000)
I122=random.randint(0,1000)
M12B=(I121)+(I122)+(s1)
I12B=M12B%amount1
print "This is for I12B",I12B

#Bit commit prng I211 ,I212 and r2
I211=random.randint(0,1000)
I212=random.randint(0,1000)
M21B=(I211)+(I212)+(I21)
I21B=M21B%amount1
print "This is for I21B",I21B

#Bit commit prng I211 ,I212 and s2
I221=random.randint(0,1000)
I222=random.randint(0,1000)
M22B=(I221)+(I222)+(s2)
I22B=M22B%amount1
print "this is for I22B",I22B

#Bit commit prng I211 ,I212 and r2
I311=random.randint(0,1000)
I312=random.randint(0,1000)
M31B=(I311)+(I312)+(r3)
I31B=M31B%amount1
print "This is for I21B",I21B

#Bit commit prng I211 ,I212 and s2
I321=random.randint(0,1000)
I322=random.randint(0,1000)
M32B=(I321)+(I322)+(s3)
I32B=M32B%amount1
print "this is for I22B",I22B

#converting all numbers into an integer. Might need to reconvert to a hex val later

moneyorderid1=((I11B,I111),(I12B,I121),(I21B,I211),(I22B,I212),(I31B,I311),(I32B,I321))

#Blinding the money order
#_______________________________________________________________________________
#There are 6 pairs that will be blinded {(I111,I11b),(I112,I12b),(I211,I21b),#(I212,I22B),(I311,I31B),(I312,I32B)}

#Generating a PRNG to multiply the pairs
blindval=random.randint(0,1000)
#money order 2
#pair 1
pair111=(I111)*blindval
pair112=(I11B)*blindval
#pair 2
pair121=(I112)*blindval
pair122=(I12B)*blindval
#pair 3
pair211=(I211)*blindval
pair212=(I21B)*blindval
#pair 4
pair221=(I211)*blindval #y-value
pair222=(I22B)*blindval #x-value
#pair 5
pair311=(I311)*blindval #y-value
pair312=(I31B)*blindval #x-value
#pair 6
pair321=(I312)*blindval #y-value
pair322=(I32B)*blindval # x-value

blindedID=((pair112,pair111),(pair122,pair121),(pair212,pair211),(pair222,pair221),(pair312,pair311),(pair322,pair321))
print "This is the blinded id1,",blindedID

#money order 2
#xor for s1 value in money order 1
I11B=r1B
I12B=r1B ^ int(cust_id, 16)
s1B=I12B
#xor for s2 value
I21B=r2B
I22B=r2B^ int(cust_id, 16)
s2B=I22B
#xor for s3 value
I31B=r3B
I32B=r3B^ int(cust_id, 16)
s3B=I32B

#Bit commit random number I111
I111=random.randint(0,1000)
I111B=random.randint(0,1000)
I111C=random.randint(0,1000)
#PRNG for I112
I112B=random.randint(0,1000)
#Converting hex to int to get value of M
M11BB=(I111B)+(I112B)+(I11B)
I11BB=M11BB%amount1
print "This is for I11BB",I11BB

#I121 and I122 and s1
I121B=random.randint(0,1000)
I122B=random.randint(0,1000)
M12BB=(I121B)+(I122B)+(s1B)
I12BB=M12BB%amount1
print "This is for I12BB",I12BB

#Bit commit prng I211 ,I212 and r2
I211B=random.randint(0,1000)
I212B=random.randint(0,1000)
M21BB=(I211B)+(I212B)+(I21B)
I21BB=M21BB%amount1
print "This is for I21BB",I21BB

#Bit commit prng I211 ,I212 and s2
I221B=random.randint(0,1000)
I222B=random.randint(0,1000)
M22BB=(I221B)+(I222B)+(s2B)
I22BB=M22BB%amount1
print "this is for I22BB",I22BB

#Bit commit prng I211 ,I212 and r2
I311B=random.randint(0,1000)
I312B=random.randint(0,1000)
M31BB=(I311B)+(I312B)+(r3B)
I31BB=M31BB%amount1
print "This is for I21BB",I21BB

#Bit commit prng I211 ,I212 and s2
I321B=random.randint(0,1000)
I322B=random.randint(0,1000)
M32BB=(I321B)+(I322B)+(s3B)
I32BB=M32BB%amount1
print "this is for I22BB",I22BB

#money order 2
#xor for s1 value in money order 1
I11B=r1B
I12B=r1B ^ int(cust_id, 16)
s1B=I12B
#xor for s2 value
I21B=r2B
I22B=r2B^ int(cust_id, 16)
s2B=I22B
#xor for s3 value
I31B=r3B
I32B=r3B^ int(cust_id, 16)
s3B=I32B

#Bit commit random number I111
I111=random.randint(0,1000)
I111B=random.randint(0,1000)
I111C=random.randint(0,1000)
#PRNG for I112
I112A=random.randint(0,1000)
I112B=random.randint(0,1000)
I112C=random.randint(0,1000)
#Converting hex to int to get value of M
M11BB=(I111B)+(I112B)+(I11B)
I11BB=M11BB%amount1
print "This is for I11BB",I11BB

#I121 and I122 and s1
I121B=random.randint(0,1000)
I122B=random.randint(0,1000)
M12BB=(I121B)+(I122B)+(s1B)
I12BB=M12BB%amount1
print "This is for I12BB",I12BB

#Bit commit prng I211 ,I212 and r2
I211B=random.randint(0,1000)
I212B=random.randint(0,1000)
M21BB=(I211B)+(I212B)+(I21B)
I21BB=M21BB%amount1
print "This is for I21BB",I21BB

#Bit commit prng I211 ,I212 and s2
I221B=random.randint(0,1000)
I222B=random.randint(0,1000)
M22BB=(I221B)+(I222B)+(s2B)
I22BB=M22BB%amount1
print "this is for I22BB",I22BB

#Bit commit prng I211 ,I212 and r2
I311B=random.randint(0,1000)
I312B=random.randint(0,1000)
M31BB=(I311B)+(I312B)+(r3B)
I31BB=M31BB%amount1
print "This is for I21BB",I21BB

#Money order 3
#Bit commit prng I211 ,I212 and s2
I321C=random.randint(0,1000)
I322C=random.randint(0,1000)
M32BC=(I321C)+(I322C)+(s3C)
I32BC=M32BC%amount1
print "this is for I32BC",I32BC

#pair 1
pair111=(I111C)*blindval
pair112=(I11B)*blindval
#pair 2
pair121=(I12C)*blindval
pair122=(I12B)*blindval
#pair 3
pair211=(I21C)*blindval
pair212=(I21B)*blindval
#pair 4
pair221=(I22C)*blindval #y-value
pair222=(I22B)*blindval #x-value
#pair 5
pair311=(I31C)*blindval #y-value
pair312=(I31B)*blindval #x-value
#pair 6
pair321=(I32C)*blindval #y-value
pair322=(I32B)*blindval # x-value
#Blinded money order id
blindedID=((pair112,pair111),(pair122,pair121),(pair212,pair211),(pair222,pair221),(pair312,pair311),(pair322,pair321))
print "This is the blinded id2,",blindedID
#money order 3
#pair 1
pair21B=(I111B)*blindval
pair21B=(I11BB)*blindval
#pair 2
pair221B=(I112B)*blindval
pair222B=(I12BB)*blindval
#pair 3
pair211=(I211B)*blindval
pair212=(I21BB)*blindval
#pair 4
pair221=(I212B)*blindval #y-value
pair222=(I22BB)*blindval #x-value
#pair 5
pair311=(I311B)*blindval #y-value
pair312=(I31BB)*blindval #x-value
#pair 6
pair321=(I312B)*blindval #y-value
pair322=(I32BB)*blindval # x-value
#Blinded money order id
blindedID=((pair112,pair111),(pair122,pair121),(pair212,pair211),(pair222,pair221),(pair312,pair311),(pair322,pair321))
print "This is the blinded id3,",blindedID

#!!!!!!!!!!!!!!!!!!!!!!!!!!Money order 2!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#xor for s1 value in money order 2
I11B=r1B
I12B=r1B ^ int(cust_id, 16)
s1B=I12B
#xor for s2 value
I21B=r2B
I22B=r2B^ int(cust_id, 16)
s2B=I22B
#xor for s3 value
I31B=r3B
I32B=r3B^ int(cust_id, 16)
s31B=I32B

#Bit commit random number I111
I111B=random.randint(0,1000)
#PRNG for I112
I112B=random.randint(0,1000)
#Converting hex to int to get value of M
M11BB=(I111B)+(I112B)+(I11B)
I11BB=M11BB%amount1
print "This is for I11BB",I11BB

#I121 and I122 and s1
I121B=random.randint(0,1000)
I122B=random.randint(0,1000)
M12BB=(I121B)+(I122B)+(s1B)
I12BB=M12BB%amount1
print "This is for I12BB",I12BB

#Bit commit prng I211 ,I212 and r2
I211B=random.randint(0,1000)
I212B=random.randint(0,1000)
M21BB=(I211B)+(I212B)+(I21B)
I21BB=M21BB%amount1
print "This is for I21BB",I21BB

#Bit commit prng I211 ,I212 and s2
I221B=random.randint(0,1000)
I222B=random.randint(0,1000)
M22BB=(I221B)+(I222B)+(s2B)
I22BB=M22BB%amount1
print "this is for I22BB",I22BB

#Bit commit prng I211 ,I212 and r2
I3111B=random.randint(0,1000)
I3121B=random.randint(0,1000)
M31B1B=(I311B)+(I312B)+(r3B)
I31BB=M31BB%amount1
print "This is for I21BB",I21BB

#Bit commit prng I211 ,I212 and s2
I321B=random.randint(0,1000)
I322B=random.randint(0,1000)
M32BB=(I32B)+(I322B)+(s3B)
I32BB=M32BB%amount1
print "this is for I22BB",I22BB

#converting all numbers into an integer. Might need to reconvert to a hex val later

moneyorderid1=((I11BB,I111B),(I12BB,I121B),(I21BB,I211B),(I22BB,I212B),(I31BB,I311B),(I32BB,I321B))

#Blinding the money orders
#_______________________________________________________________________________
#There are 6 pairs that will be blinded {(I111,I11b),(I112,I12b),(I211,I21b),(I212,I22B),(I311,I31B),(I312,I32B)}

#Generating a PRNG to multiply the pairs
blindval=random.randint(0,1000)
#money order 2
#pair 1
pair111B=(I111B)*blindval
pair112B=(I11BB)*blindval
#pair 2
pair121B=(I112B)*blindval
pair122B=(I12BB)*blindval
#pair 3
pair211B=(I211B)*blindval
pair212B=(I21BB)*blindval
#pair 4
pair221B=(I212B)*blindval #y-value
pair222B=(I22BB)*blindval #x-value
#pair 5
pair311B=(I311B)*blindval #y-value
pair312B=(I31BB)*blindval #x-value
#pair 6
pair321B=(I312B)*blindval #y-value
pair322B=(I32BB)*blindval # x-value

#!!!!!!!!!!!!!!!!!!!!!!!!!!!Money Order 3!!!!!!!!!!!!!!!!!!!!!!!!!!!
#xor for s1 value in money order 2
I11C=r1C
I12C=r1C ^ int(cust_id, 16)
s1C=I12C
#xor for s2 value
I21C=r2C
I22C=r2C^ int(cust_id, 16)
s2C=I22C
#xor for s3 value
I31C=r3C
I32C=r3C^ int(cust_id, 16)
s31C=I32C

#Bit commit random number I111
I111C=random.randint(0,1000)
#PRNG for I112

#Converting hex to int to get value of M
M11BC=(I111C)+(I112C)+(I11C)
I11BC=M11BC%amount1
print "This is for I11BC",I11BC

#I121 and I122 and s1
I121C=random.randint(0,1000)
I122C=random.randint(0,1000)
M12BC=(I121C)+(I122C)+(s1C)
I12BC=M12BC%amount1
print "This is for I12BC",I12BC

#Bit commit prng I211 ,I212 and r2
I211C=random.randint(0,1000)
I212C=random.randint(0,1000)
M21BC=(I211C)+(I212C)+(I21C)
I21BC=M21BC%amount1
print "This is for I21BC",I21BC

#Bit commit prng I211 ,I212 and s2
I221C=random.randint(0,1000)
I222C=random.randint(0,1000)
M22BC=(I221C)+(I222C)+(s2C)
I22BC=M22BC%amount1
print "this is for I22BC",I22BC

#Bit commit prng I211 ,I212 and r2
I311C=random.randint(0,1000)
I312C=random.randint(0,1000)
M31BC=(I311C)+(I312C)+(r3C)
I31BC=M31BC%amount1
print "This is for I31BC",I31BC

#Bit commit prng I211 ,I212 and s2
I321C=random.randint(0,1000)
I322C=random.randint(0,1000)
M32BC=(I32C)+(I322C)+(s3C)
I32BC=M32BC%amount1
print "this is for I22BC",I22BC

#converting all numbers into an integer. Might need to reconvert to a hex val later

moneyorderid3=((I11BC,I111C),(I12BC,I121C),(I21BC,I211C),(I22BC,I212C),(I31BC,I311C),(I32BC,I321C))

#Blinding the money orders
#_______________________________________________________________________________
#There are 6 pairs that will be blinded {(I111,I11b),(I112,I12b),(I211,I21b),(I212,I22B),(I311,I31B),(I312,I32B)}

#Generating a PRNG to multiply the pairs
blindval=random.randint(0,1000)
#money order 2
#pair 1
pair111C=(I111C)*blindval
pair112C=(I11BC)*blindval
#pair 2
pair121C=(I112C)*blindval
pair122C=(I12BC)*blindval
#pair 3
pair211C=(I211C)*blindval
pair212C=(I21BC)*blindval
#pair 4
pair221C=(I212C)*blindval #y-value
pair222C=(I22BC)*blindval #x-value
#pair 5
pair311C=(I311C)*blindval #y-value
pair312C=(I31BC)*blindval #x-value
#pair 6
pair321C=(I312C)*blindval #y-value
pair322C=(I32BC)*blindval # x-value

#output for the moneyorder file
text_file=open("moneyorder.txt",'a')
text_file.write("Money order 1\n")
text_file.write("____________________________________\n")
text_file.write("The ammount =$")
text_file.write("")
text_file.write(str(amount1))
text_file.write("")
text_file.write("\nThe customer id is:")
text_file.write(str(cust_id))

text_file.write("\nThis is the blinded id:\n")
text_file.write(str(blindedID))
