# Код начинается здесь ...
import random as rnd
negativ_numbers = []
with open("nums.txt", "w", encoding="utf-8") as file:
    for i in range(0, 20):
        file.write(str(rnd.randint(-100, 101)) + " ")
with open("nums.txt", "r", encoding="utf-8") as file:
    numbers = file.read()
    numbers = numbers.split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    print(sum(numbers))
with open("negative.txt", "w", encoding="utf-8") as file:
    for i in range(len(numbers)):
        if int(numbers[i]) < 0:
            negativ_numbers.append(numbers[i])
            file.write(str(numbers[i]) + " ")
if len(negativ_numbers) > 0:
    print("Negative values were found, reading from file: ", end="")
    print(negativ_numbers)
