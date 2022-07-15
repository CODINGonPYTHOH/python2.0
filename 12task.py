#Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

#Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case





def  count_bits(n):
    c = 0
    b = ""
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    for e in b:
        if e == str(1):
            c += 1
    return c
