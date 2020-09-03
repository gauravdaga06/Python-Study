##n=int(input("Enter the n natural number n:"))
##sum=0
##avg=0
##for i in range(1,n+1,1):
##    sum=sum+i
##print("average of n natural number is:",sum/n)
##
##------------------------------------------------------------------
##Multiplication table of n
##n=int(input("Enter the number n whose table is to be find:"))
##for i in range(0,11,1):
##    print(n,"X",i,"=",n*i)
##------------------------------------------------------------------
##m=int(input("Enter the value of m :"))
##n=int(input("Enter the Value of n:"))
##i=m
##for i in range(m,n+1,1):
##    if(i%2==0):
##        print(i,"This is even Number")
##    else:
##        print(i,"This is odd Number")
##---------------------------------------------------------------
# n=int(input("Enter the Numberfor factorial"))
 # fact=1
# if(n==0):
#    fact=1
# else:
#    for i in range(1,n+1,1):
#        fact=fact*i
# print(fact)
# #-----------------------------------------------------------------------
# n=int(input("Enter the Number till where u want to find square:"))
# sum=0

# for i in range (1,n+1,1):
#    sum=sum +i*i
# print(sum)
# ---------------------------------------------------------------------
# d=int(input("Enter the Day(1-7):"))
# day=int(input("Enter the Number of Days in The month u want:"))
# print("Sun  Mon  Tue  Thur  Fri  Sat")
# for i in range(d-1):
#    print(end= "  ")
# i=day-1
# for j in range(1,day+1,1):
#    if(i>6):
#       print()
#       i=1
#    else:
#       i=i+1
#       print(str(j)+"  ",end="  ")
# ----------------------------------------------------------------
# for i in range(1,6,1):
#    print("Pass ",i,"-  ",end=' ')
#       print(j,end=' ')
#    for j in range(1,6,1):
#    print()
# ---------------------------------------------------------------------
# for i in range(1,6):
#    for j in range(1,11):
#           print("*",end='')
#    print()
# -------------------------------------------------------------------------
# for i in range(1,6):
#    print()
#    for j in range(0,i):
#       print("*",end='')
# --------------------------------------------------------------------------
# for i in range(1,6):
#    print()
#    for j in range(1,i+1):
#       print(j,end='')
# --------------------------------------------------------------------
# count=0
# for i in range(1,5):
#    print()
#    for j in range(0,i):
#       print(count,end='')
#       count=count+1
# --------------------------------------------------------------
# for i in range(1,6):
#    for k in range(5,i,-1):
#       print(" ",end=' ')
#    for j in range(1,i+1):
#       print(j,end=' ')
#    for l in range(i-1,0,-1):
#       print(l,end=' ')
#    print()
# -------------------------------------------------------------