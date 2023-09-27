num = float(input("Enter your number: "))
if num > 0:
    a = "0"
else:
    a = "1"
absolute_number = abs(num)
num_bin = bin(int(absolute_number))[2:]
num_bin = num_bin.zfill(5)


length = len(num_bin) + 16
b = str(bin(length)[2:])
# print("The value of a is", a)
# print("The value of b is", b)

c = str(num_bin)
string_num = str(num)
last_part = string_num.split(".")[1]
final_num = float("0." + last_part)

# print(final_num)
bit_string = ""
for _ in range(8):
    final_num *= 2
    if final_num >= 1.0:
        bit = '1'
    else:
        bit = '0'
    bit_string += bit
    final_num -= int(final_num)


# print(bit_string)

c = str(num_bin) + str(bit_string)
c = c[1:]
# print(c)

f14_bit_number2 = a + b + c
f14_bit_number= f14_bit_number2[0:14]
print (f14_bit_number)