#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = number % 10

# Mənfi ədədlər üçün korreksiya
if number < 0 and last_digit != 0:
    last_digit -= 10

output_suffix = ""

if last_digit > 5:
    output_suffix = " and is greater than 5"
elif last_digit == 0:
    output_suffix = " and is 0"
# last_digit < 6 AND last_digit != 0 üçün:
elif last_digit < 6 and last_digit != 0:
    # Bu uzun sətri dəyişəndə saxlayırıq
    output_suffix = " and is less than 6 and not 0"

# Çıxış sətrini qısa tuturuq.
print("Last digit of {} is {}{}".format(
    number, last_digit, output_suffix))
