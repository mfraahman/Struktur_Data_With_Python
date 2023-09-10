def is_palindrome(s):
    # Basis untuk rekursi: jika panjang string kurang dari atau sama dengan 1, maka itu adalah palindrom
    if len(s) <= 1:
        return True
    # Perbandingan karakter pertama dan terakhir
    if s[0] != s[-1]:
        return False
    # Rekursi: periksa bagian tengah string
    return is_palindrome(s[1:-1])

# Contoh penggunaan
input_string = "racecar"
if is_palindrome(input_string):
    print(f"{input_string} adalah palindrom.")
else:
    print(f"{input_string} bukan palindrom.")

# Contoh penggunaan kedua
input_string = "gohangasalamiimalasagnahog"
if is_palindrome(input_string):
    print(f"{input_string} adalah palindrom.")
else:
    print(f"{input_string} bukan palindrom.")