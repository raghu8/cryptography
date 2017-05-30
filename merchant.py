
from bank import banksignature,moneyorderAmount1,moneyorderAmount2,moneyorderAmount3,n,unblinded,d
from cusotmer import *
import random

#modified with banks private key
with open("merchant.txt",'a')as outfile:
    s1=(float(amount1)/blindval)%n
    s2=(float(amount2)/blindval)%n
    s3=(float(amount3)/blindval)%n
    left="left"
    right="right"
    half=random.choice([left,right])
    print "choice",half
    if half=="left":
        reval=(I11,I121,I12B)
        h1=(I11**d)%n
        h2=(I121**d)%n
        h3=(I12B**d)%n
        outfile.write("This right half of id is,\n")
        outfile.write(str(reval))
        SignedUnblinded=(h1,h2,h3)
        outfile.write( "This is the signed unblinded moneyorder \n")
        outfile.write(str(SignedUnblinded))
    else:
        reval=(I11B,I111,I11)
        h1=(I11B**d)%n
        h2=(I111**d)%n
        h3=(I11**d)%n
        outfile.write("This right half of id is, \n")
        outfile.write(str(reval))
        SignedUnblinded=(h1,h2,h3)
        outfile.write( "This is the signed unblinded moneyorder \n")
        outfile.write(str(SignedUnblinded))
        print "This is s1",s1
        print "This is s2",s2
        print "This is s3",s3


'''
x1=moneyorderAmount1
x2=moneyorderAmount2
x3=moneyorderAmount3
print x1
print x2
print x3
#dividing x1,x2 and x3 with blinding value used by the customer
k=blindval
print "this is the blinded value",blindval
y1=x1*((k**(-1))%n)
y2=x2*((k**(-1))%n)
y3=x3*((k**(-1))%n)

print "This is the first y",y1
print "This is the first y",y2
print "This is the first y",y3
'''
