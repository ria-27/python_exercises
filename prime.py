#Program to write a python function that takes an integer and returns True if it's a prime and False otherwise
def prime(num):
   is_prime = 1
   if num != 1 and num!=0:
        for i in range(2,num):
            if num % i == 0:
                is_prime = 0
                break
        if is_prime:
            print("True")
        else:
               print("False")
prime(int(input("Enter a number: ")))
