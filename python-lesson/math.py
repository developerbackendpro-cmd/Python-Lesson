#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 1. Qo‘shish (+)
a = 10
b = 5
natija = a + b
print("Qo'shish:", a, "+", b, "=", natija)
# Qo‘shish: 10 + 5 = 15
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 2. Ayirish (-)
a = 10
b = 5
natija = a - b
print("Ayirish:", a, "-", b, "=", natija)
# Ayirish: 10 - 5 = 5
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 3. Ko‘paytirish (*)
a = 10
b = 5
natija = a * b
print("Ko'paytirish:", a, "*", b, "=", natija)
# Ko‘paytirish: 10 * 5 = 50
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 4. Butun bo‘lish (//)
a = 10
b = 3
natija = a // b
print("Butun bo'lish:", a, "//", b, "=", natija)
# Butun bo‘lish: 10 // 3 = 3
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 5. Oddiy bo‘lish (/)
a = 10
b = 3
natija = a / b
print("Oddiy bo'lish:", a, "/", b, "=", natija)
# Oddiy bo‘lish: 10 / 3 = 3.3333333333333335
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 6. Qoldiq (%)
a = 10
b = 3
natija = a % b
print("Qoldiq:", a, "%", b, "=", natija)
# Qoldiq: 10 % 3 = 1
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 7. Daraja (**)
a = 2
b = 3
natija = a ** b
print("Daraja:", a, "**", b, "=", natija)
# Daraja: 2 ** 3 = 8
#-------------------------------------------------------------------------------------------------------------------------------#
# 🧮 1. sum() — yig‘indi hisoblash
# sum() funksiyasi ro‘yxat (yoki boshqa iteratsiya qilinadigan obyekt) ichidagi sonlarning yig‘indisini hisoblaydi.
sonlar = [3, 7, 10, 2]
natija = sum(sonlar)
print("Yig'indi:", natija)
# Yig‘indi: 22
#-------------------------------------------------------------------------------------------------------------------------------#
# 🔽 2. min() — eng kichik qiymat
# min() funksiyasi berilgan ro‘yxatdagi eng kichik sonni (yoki qiymatni) topadi.
sonlar = [3, 7, 10, 2]
kichik = min(sonlar)
print("Eng kichik son:", kichik)
# Eng kichik son 2
#-------------------------------------------------------------------------------------------------------------------------------#
# 🔼 3. max() — eng katta qiymat
# max() funksiyasi esa eng katta qiymatni topadi.
sonlar = [3, 7, 10, 2]
katta = max(sonlar)
print("Eng katta son:", katta)
# Eng katta son: 10
#-------------------------------------------------------------------------------------------------------------------------------#
# 1️⃣ abs() funksiyasi – sonning absolyut qiymatini topadi (ya'ni manfiy belgini olib tashlaydi)
son1 = -15   # bu manfiy son
natija1 = abs(son1)   # abs() uni musbatga aylantiradi
print("1. abs() →", son1, "ning absolyut qiymati:", natija1)
# 1. abs() → -15 ning absolyut qiymati: 15
#-------------------------------------------------------------------------------------------------------------------------------#
# 2️⃣ round() funksiyasi – sonni yaxlitlaydi (yaqin butun songa yoki kerakli o‘nlik xonagacha)
son2 = 4.6789
natija2 = round(son2)        # butun songa yaxlitlaydi → 5
natija3 = round(son2, 2)     # 2 xonagacha yaxlitlaydi → 4.68
print(son2, "butun songa yaxlitlansa:", natija2)
print(son2, "ikkita o'nlik xonagacha:", natija3)
# 4.6789 butun songa yaxlitlansa: 5
# 4.6789 ikkita o‘nlik xonagacha: 4.68
#-------------------------------------------------------------------------------------------------------------------------------#
# 3️⃣ pow() funksiyasi – darajaga oshirish
asos = 3       # bu asos (3)
daraja = 4     # bu daraja (4)
natija4 = pow(asos, daraja)   # 3⁴ = 3*3*3*3 = 81
print("3. pow() →", asos, "ning", daraja, "darajasi:", natija4)
# 3. pow() → 3 ning 4 darajasi: 81
#-------------------------------------------------------------------------------------------------------------------------------#

