num=371
digits=str(num)
num_digits=len(digits)
sum_of_powers=0
for  digit in digits:
    sum_of_powers += int(digit) ** num_digits
print(f"{num} is an armstrong number: {sum_of_powers == num}")

 #370
num= 370
digit=str(num)
num_digit=len(digit)
sum_of_powers=0
while  digit in digits :
    sum_of_powers += int(digit) ** num_digit
print(f"{num} is an armstrong number: {sum_of_powers == num}")

#153
num=153
digits=str(num)
num_digits=len(digits)
sum_of_powers=0
while digit in digits:
    sum_of_powers += int(digit) ** num_digits
print(f"{num} is an armstrong number: {sum_of_powers == num}")