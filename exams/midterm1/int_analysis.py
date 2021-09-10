PROMPT = "Input an integer (0 to quit): "

even_count = 0
odd_count = 0
even_sum = 0
odd_sum = 0

next_int = int(input(PROMPT))
while next_int != 0:
    if next_int > 0:
        if next_int % 2 == 0:   # even
            even_count += 1
            even_sum += next_int
        else:                   # odd
            odd_count += 1
            odd_sum += next_int
    else:
        print("Ignoring this negative number!")

    next_int = int(input(PROMPT))

print("Sum of even:", even_sum)
print("Sum of odd:", odd_sum)
print("Even count:", even_count)
print("Odd count:", odd_count)
