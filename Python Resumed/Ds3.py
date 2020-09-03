seq=[]
nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   seq.append(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       seq.append(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
print(seq)

even=[]
i=0
while i < len(seq):
    num  = seq[i]
    if num % 2 == 0:
        even.append(num)
    i+=1
print("List of even Values from the fibonancci series",even)
print("Sum of Even Terms from the fibonancci serie :",sum(even))