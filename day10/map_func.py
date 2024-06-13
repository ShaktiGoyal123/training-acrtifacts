def power2(val: int) -> int:
    return val*val

numbers = [1, 2, 3, 4, 5]

power_numbers = list(map(power2, numbers))
# OR
squared_numbers = list(map(lambda x: x**2, numbers))

print(power_numbers,squared_numbers)