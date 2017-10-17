def ackermann(m,n):
     if m == 0:
          return int(2)*int(n)
     elif m >= 1 and n==0:
        return 0
     elif m >= 1 and n==1:
        return 2

     else:
          return ackermann(m - 1, ackermann(m, n - 1))

x=int(input("What is the value for m? "))
print x

y=int(input("What is the value for n? "))
print y

print "\nThe result of your inputs according to the Ackermann Function is:"
print (ackermann(x, y))
