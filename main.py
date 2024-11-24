import sum_squares as ss

a = input("Please enter your starting number: ")
b = input("Now enter your ending number: ")

for _ in range(int(a), int(b)):
    ss.test_sum_squares(int(_))