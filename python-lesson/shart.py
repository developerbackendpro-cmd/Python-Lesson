# 1 . if bitta yoki bir nechta bo‘lishi mumkin.
# 2 . elif har doim if yoki boshqa elifdan keyin keladi, va u faqat oldingi shartlar False bo‘lsa tekshiriladi.
# 3 . else esa shartsiz yakuniy variant, agar barcha shartlar False bo‘lsa, shu blok bajariladi.
# 4 . Siz elif va elsesiz ham ishlatishingiz mumkin, lekin agar elif yoki else ishlatilsa, ularni if bilan birga qo‘llash shart.
#-------------------------------------------------------------------------------------------------------------------------------#
# 1. if — может быть один или несколько.
# 2. elif — всегда идет после if или другого elif,
#    и проверяется только в том случае, если предыдущие условия были False.
# 3. else — это вариант без условия; он выполняется,
#    если все предыдущие условия оказались False.
# 4. Можно использовать if без elif и else,
#    но если применяются elif или else, то они должны идти вместе с if.

# | Operator | Ma’nosi (UZ)         | Значение (RU)              | Misol / Пример | Natija / Результат   |
# |----------|-----------------------|---------------------------|-----------------|---------------------|
# |   ==     | Tengmi?               | Равно?                    | 5 == 5          | True                |
# |   !=     | Teng emasmi?          | Не равно?                 | 5 != 3          | True                |
# |   >      | Katta                 | Больше                    | 5 > 3           | True                |
# |   <      | Kichik                | Меньше                    | 2 < 5           | True                |
# |   >=     | Katta yoki teng       | Больше или равно          | 5 >= 5          | True                |
# |   <=     | Kichik yoki teng      | Меньше или равно          | 3 <= 5          | True                |
# |----------|-----------------------|---------------------------|-----------------|---------------------|

yosh = 15
if yosh >= 18:
    print("Kattalar")
elif yosh >= 13:
    print("O'smir")
else:
    print("Bola")
# Natija: O‘smir

# 1. Tengmi? / Равно
x = 5
y = 5
if x == y:
    print("5 == 5")  # True
else:
    print("5 == 5")  # False

# 2. Teng emasmi? / Не равно
x = 5
y = 3
if x != y:
    print("5 != 3")  # True
else:
    print("5 != 3")  # False

# 3. Katta / Больше
x = 5
y = 3
if x > y:
    print("5 > 3")  # True
else:
    print("5 > 3")  # False

# 4. Kichik / Меньше
x = 2
y = 5
if x < y:
    print("2 < 5")  # True
else:
    print("2 < 5")  # False

# 5. Katta yoki teng / Больше или равно
x = 5
y = 5
if x >= y:
    print("5 >= 5")  # True
else:
    print("5 >= 5")  # False

# 6. Kichik yoki teng / Меньше или равно
x = 3
y = 5
if x <= y:
    print("3 <= 5")  # True
else:
    print("3 <= 5")  # False

# |----------|-------------------------------------------------------------|------------------------------------------------------|-----------------------|---------------------|
# | Operator | Ma’nosi (UZ)                                                | Значение (RU)                                        | Misol / Пример       | Natija / Результат   |
# |----------|-------------------------------------------------------------|------------------------------------------------------|-----------------------|---------------------|
# | and      | Ikkalasi ham True bo‘lsa True qaytaradi                     | Возвращает True, если оба значения True              | 5 > 3 and 10 > 5      | True                |
# | or       | Hech bo‘lmaganda bittasi True bo‘lsa True qaytaradi         | Возвращает True, если хотя бы одно значение True     | 5 > 3 or 2 > 5        | True                |
# | not      | Mantiqiy qiymatni teskarisiga o‘giradi                      | Переворачивает логическое значение на противоположное| not (5 > 3)           | False               |
# |----------|-------------------------------------------------------------|------------------------------------------------------|-----------------------|---------------------|

x = 5
y = 10
if x > 3 and y > 5:
    print("Ikkala shart ham to'g'ri")  # True
else:
    print("Kamida bittasi noto'g'ri")

x = 5
y = 2
if x > 3 or y > 5:
    print("Kamida bittasi to'g'ri")  # True
else:
    print("Ikkalasi ham noto'g'ri")

x = 5
if not (x > 10):
    print("x > 10 emas")  # True, chunki x > 10 noto‘g‘ri
else:
    print("x > 10 to'g'ri")
#-------------------------------------------------------------------------------------------------------------------------------#