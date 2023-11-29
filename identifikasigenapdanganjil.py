def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Membuat bilangan acak dari 0 hingga 399
arr = list(range(400))

# Memisahkan bilangan ganjil dan genap
odd_numbers = [x for x in arr if x % 2 != 0]
even_numbers = [x for x in arr if x % 2 == 0]

# Mengurutkan bilangan ganjil dan genap
sorted_odd_numbers = quick_sort(odd_numbers)
sorted_even_numbers = quick_sort(even_numbers)

# Membuka file teks untuk penulisan
file = open("hasil.txt", "w")

# Menulis hasil bilangan ganjil ke dalam file
file.write("Bilangan Ganjil:\n")
for number in sorted_odd_numbers:
    file.write(str(number) + "\n")

# Menulis hasil bilangan genap ke dalam file
file.write("\nBilangan Genap:\n")
for number in sorted_even_numbers:
    file.write(str(number) + "\n")
    
# Menutup file
file.close()

print("Hasil telah ditulis ke dalam file hasil.txt")
