def factorial(num):
    ans = 1
    
    for i in range(1, num+1):
        ans *=i
        
        
    print(f"{num}! = {ans}")

#displays sum of 1 to number
# ex: sum 5 = 5+4+3+2+1 = 15
def sum(num):
    total = 0
    
    for i in range(1, num+1):
        total += i
        
    print(f"sum 1 to {num} = {total}")

#sum(5)
#we are leaving this out to try the next example
#ex: 2^3 = 2 * 2 * 2
def power(base,exp):
    ans = 1
    
    for i in range(exp):
        ans *= base
    print(f"{base}^{exp} = {ans}")


#displays either number is prime or is not
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not prime")
            return # break exits a loop. "return" exits an entire function
        
        # no number is evenly divided once it reaches line 38.
        print(f"{num} is prime.") 


#Math Program
print("Welcome to my math game!!!")

while True:
    command = input("(S)um, (P)ower, (F)actorial, P(R)ime, or (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    elif command == "s":
        num = int(input("Enter Number: "))
        sum(num)
    elif command == "p":
        base = int(input("Enter Base: "))
        exp = int(input("Enter Exponent: "))
        power(base, exp)
    elif command == "f":
        num = int(input("Enter Number: "))
        factorial(num)
    elif command == "r":
        num = int(input("Enter Number: "))
        is_prime(num)
    else: 
        print("Invalid command.")
print("Goodbye.")