upper = int(input ("eneter a upper range: "))
Lower = int(input ("eneter a lower range"))

print("prime numbers between", Lower, "and", upper, "are:")
for num in range(Lower, upper + 1):

    if num > 1:
        for i in range(2, num): 
            if (num % i) ==0:
                break
            else:
                print (num)