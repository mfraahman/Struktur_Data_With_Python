def has_more_vowels_than_consonants(s):
    # Jika string kosong, kembalikan False
    if s == "":
        return False
    
    # Inisialisasi hitungan huruf vokal dan huruf konsonan
    vowel_count = 0
    consonant_count = 0
    
    # Ambil huruf pertama dari s
    first_letter = s[0]
    
    # Jika huruf adalah huruf vokal, tambahkan 1 ke hitungan huruf vokal
    if first_letter.lower() in "aeiou":
        vowel_count += 1
    # Jika huruf adalah huruf konsonan, tambahkan 1 ke hitungan huruf konsonan
    else:
        consonant_count += 1
    
    # Panggil fungsi has_more_vowels_than_consonants rekursif dengan sisa string (tanpa huruf pertama)
    return has_more_vowels_than_consonants(s[1:]) 

# Contoh Penggunaan 
input_string = "apakah yang kau lakukan"
if has_more_vowels_than_consonants(input_string):
    print(f"{input_string} has more vowels than consonants.")
else:
    print(f"{input_string} does not have more vowels than consonants.")
