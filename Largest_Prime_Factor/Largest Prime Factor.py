num = 600851475143
primeNumbers = []
i = 2
end = int(num**0.5)+ 1 # No factor will be larger than the square root of the number

while i <= end:
    if num % i == 0: # Check if i is a factor of num
        primeNumbers.append(i) # If it is, add it to the list of prime factors
        num //= i # Divide num by i to reduce it
    else: # If i is not a factor, increment i
        i += 1
print(max(primeNumbers))