import random
import string
print("Welcome to our Random Password Generator")
def my_function():
        #print("Welcome to our Random Password Generator")
        length=int(input("enter the length of the password you want:"))
        lowerD=string.ascii_lowercase
        upperD=string.ascii_uppercase
        digitD=string.digits
        symbolsD=string.punctuation
        combine=lowerD+upperD+symbolsD
        x=random.sample(combine,length)
        password="".join(x)
        print(password)
        my_function()
my_function()


    