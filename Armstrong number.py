def isArmstrong(num):
    digits=str(num)
    num_digits=len(digits)
    sum_of_powers=0
    for  digit in digits:
        sum_of_powers += int(digit) ** num_digits
    return sum_of_powers
    
num = int(input('Enter a number to check:'))
print(f"{num} is an armstrong number: {isArmstrong(num) == num}")
    
