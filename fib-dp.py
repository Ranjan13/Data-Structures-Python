num = int(raw_input("Enter a number to find fibonacci: \n"))

fibtable = {1:1,2:1}
def fibo(n):
        if n<=2:
                return 1
                if n in fibtable[n]:
                        return fibtable[n]
        else:
                fibtable[n] = fibo(n-1) + fibo(n-2)
                return fibtable[n]
print fibo(num)
#print fibtable
