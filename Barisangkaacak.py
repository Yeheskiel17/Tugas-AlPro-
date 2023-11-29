# Buatlah 100 angka acak dalam rentang bilangan 0 - 399
import random

for _ in range(100):
    angka = [random.randint(0, 399) for _ in range(100)]


# Memasukkan angka kedalam file teks
with open("random.txt", "w") as file:
    for number in angka:
        file.write(str(number) + "\n")