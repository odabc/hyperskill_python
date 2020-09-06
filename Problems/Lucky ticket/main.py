# Save the input in this variable
ticket = input()


def sum_digits(chars):
    return sum(map(int, chars))


# Add up the digits for each half
half1 = sum_digits(ticket[:3])
half2 = sum_digits(ticket[-3:])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
