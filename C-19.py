def rearrange_even_odd(sequence):
    even = []  # List untuk bilangan genap
    odd = []   # List untuk bilangan ganjil

    for item in sequence:
        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)

    return even + odd  # Menggabungkan bilangan genap dan ganjil

# Contoh penggunaan
sequence = [-5, 10, 3, 7, 42, 99, 22, -1]
result = rearrange_even_odd(sequence)
print(result)
