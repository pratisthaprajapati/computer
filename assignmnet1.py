# Write the program in any computer language to convert the given number from any
# base to a different base. The program needs to verify the validity of the given number
# first. If it is invalid, please prompt error information. Otherwise, print the correct
# result in the new base. For instance, as follows is the def function "base_conv" in
# Python.
# def base_conv (num, base, new_base):
# """
# conv(123-45-6, 44, 23) # -45- represents one digit in base 44
# 123-45-6 is invalid, since one single bit -45- is bigger than base 44
# conv(123-45-6, 46, 23)
# # 123-45-6 (base 46) = 1*46^4 + 2*46^3 + 3*46^2 + 45*46^1 + 6*46^0 = 4680552 (base 10)
# # 4680552 (base 10) = -16-16-15-21-6 (base 23) = 16*23^4 + 16*23^3 + 15*23^2 + 21*23^1 + 6*23^0
# -16-16-15-21-6 (base 23) # Final answer with 5 digits for base 23
# conv(6-54-3-21-, 46, 23) # -54- and -21- represent one digit in base 46 respectively
# 6-54-3-21- is invalid, since one single bit -54- is bigger than base 46
# conv(6-54-3-21-, 63, 74)


#It take the number to be converted
num = input("enter a number: ")

#it recognize the base of input number
firstbase = int(input("enter a base: "))

length= len(num)
b: int = 0
for newv in num:
    if int(newv)>firstbase:
        
        raise ValueError("Error!! Your base is not correct")

second_base= int(input("Enter the second base(In positive integer number):"))


decimal:int= 0
remainder =""
for i in num:
    decimal+=int(i)*(firstbase**(length-1))
    length -=1

result =""

if decimal==0:
    print(f"The value of {num} of base {firstbase} to base {second_base} is 0")
else:
    for i in str(decimal):
        remainder = decimal % second_base
        result = str(remainder)+ result
        decimal //= second_base

print(f"The value of {num} of base {firstbase} to base {second_base} is {result}")