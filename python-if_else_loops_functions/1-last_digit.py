#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Son rəqəmin hesablanması (nümunə çıxışlarına uyğun olaraq)
last_digit = number % 10

# Mənfi ədədlərdə son rəqəmin işarəsini düzəltmək
# Məsələn: -626 % 10 = 4. Nümunə: -6.
if last_digit > 5 and number < 0:
    last_digit -= 10
# Qeyd: -9200 % 10 = 0 (düzgündür)

# Çıxış sətrinin başlanğıcı
output_string = "Last digit of {} is {}".format(number, last_digit)

# Şərtlərin yoxlanılması
if last_digit > 5:
    output_string += " and is greater than 5"
elif last_digit == 0:
    output_string += " and is 0"
elif last_digit < 6 and last_digit != 0:
    output_string += " and is less than 6 and not 0"

# Nəticəni çap etmək
print(output_string)
