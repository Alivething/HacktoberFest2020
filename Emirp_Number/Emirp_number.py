#An emirp number is one that remains prime even after the order of digits is switched
#This problem is taken from HP Codewars 2019 and is one of my first python programs
print("An emirp number is one that remins prime even the order of its digits is switched, an example would be 13")
number=int(input('Enter an integer: '))

#Making a temp variables
temp_number=number
switched_number=0


#Loop to switch order
while(temp_number!=0):

    switched_number=switched_number*10 + int(temp_number%10)
    temp_number=int(temp_number/10)
    
#Now to make a function to check if numbers are prime
def CheckPrime(input_number):
    for i in [2,int(input_number/2)]:
        if(input_number%i==0):
            return 0
    return 1

#Lets call the function with the numbers
if(CheckPrime(number)+CheckPrime(switched_number)==2):
    print(number, "is an emirp number")
else:
    print(number, "is not an emirp number")
