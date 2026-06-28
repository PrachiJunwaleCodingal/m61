
def fac(n):
    if(n==1 or n==0):
        return 1
    return n*fac(n-1)
n = int(input("Enter your number : "))
print ("Factorial of", n, "is : ",fac(n))

print("The time complexity of this factorial function is \(O(n)\) (linear time).")