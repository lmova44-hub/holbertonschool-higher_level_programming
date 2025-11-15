#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# 1. Son rəqəmi tapın
last_digit = number % 10

# 2. Mənfi ədədlər üçün korreksiya (nümunə çıxışı tələb edir ki, -98-in son rəqəmi -8 olsun)
# number < 0 olarsa VƏ son rəqəm 0-a bərabər deyilsə (0 % 10 həmişə 0-dır və düzgündür)
if number < 0 and last_digit != 0:
    last_digit -= 10

# 3. Şərtlərin yoxlanılması və çıxışın hazırlanması
output_suffix = ""

if last_digit > 5:
    output_suffix = " and is greater than 5"
elif last_digit == 0:
    output_suffix = " and is 0"
# last_digit < 6 AND last_digit != 0 üçün:
elif last_digit < 6 and last_digit != 0:
    output_suffix = " and is less than 6 and not 0"

# Nəticəni çap etmək
print("Last digit of {} is {}{}".format(number, last_digit, output_suffix))
