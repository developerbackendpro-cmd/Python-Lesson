# Funksiya – bu biror ishni bajaradigan kod blokidir.
# Vazifalari va ishlatilishi:
# 1. Kodni qayta-qayta ishlatmaslik uchun.
# 2. Katta dasturlarni bo‘laklarga ajratish.
# 3. Murakkab hisob-kitoblarni yoki ish jarayonlarini soddalashtirish.
# 4. Parametrlar yordamida turli qiymatlar bilan ishlash.
# 5. Natija qaytarish yoki ma’lumotni tahlil qilish.
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 1️⃣ Oddiy (parametrsiz, qiymat qaytarmaydigan) funksiya
def salom_ber():
    print("Assalomu alaykum, talaba !")
salom_ber()
# Natija:
# Assalomu alaykum, talaba!
# ☑️ Funksiya hech qanday ma’lumot olmaydi, faqat xabar chiqaradi.
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 2️⃣ Parametrli, qiymat qaytarmaydigan funksiya
def salom_ber(ism):
    print("Salom,", ism)
salom_ber("Dilshod")
# Natija:
# Salom, Dilshod
# ☑️ Parametr sifatida ism olinadi va chiqariladi
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 3️⃣ Ikkita sonni qo‘shuvchi funksiya
def yigindi(a, b):
    natija = a + b
    print("Yig'indi:", natija)
yigindi(3, 5)
# Natija:
# Yig‘indi: 8
# ☑️ Funksiya ikki sonni qabul qiladi va ularning yig‘indisini chiqaradi.
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 4️⃣ Sukut (default) qiymatli funksiya
def salom_ber(ism="Mehmon"):
    print("Salom,", ism)
salom_ber()
salom_ber("Aziza")
# Natija:
# Salom, Mehmon
# Salom, Aziza
# ☑️ Agar parametr uzatilmasa — “Mehmon” ishlatiladi.
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 5️⃣ *args bilan (ko‘p sonlarni qo‘shish)
def yigindi(*sonlar):
    natija = sum(sonlar)
    print("Jami:", natija)
yigindi(2, 3, 5, 10)
# Natija:
# Jami: 20
# ☑️ sum() barcha sonlarni qo‘shadi
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 6️⃣ **kwargs bilan (ma’lumotlarni chiqarish)
def talaba_info(**malumot):
    print(malumot)
talaba_info(ism="Dilshod", yosh=56, kurs=4)
# Natija:
# {'ism': 'Dilshod', 'yosh': 56, 'kurs': 4}
# ☑️ **malumot argumentlarni lug‘at (dict) ko‘rinishida oladi.
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 7️⃣  Lambda (sodda bir qatorli funksiya)
salom = lambda ism: print("Salom,", ism)
salom("Olim")
# Izoh: lambda qisqa anonim funksiya,
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 8️⃣ Funksiya ichida funksiya (soddalashtirilgan)
def tashqi():
    def ichki():
        print("Ichki funksiya ishladi")
    ichki()
tashqi()
# Natija:
# Ichki funksiya ishladi
# ☑️ Ichki funksiya faqat tashqi funksiyada ishlaydi.
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 9️⃣ Funksiyani boshqa funksiyaga uzatish
def salom_ayt():
    print("Assalomu alaykum!")
def bajar(f):
    f()
bajar(salom_ayt)
# Natija:
# Assalomu alaykum!
# ☑️ Bu yerda funksiya boshqa funksiyaga uzatilgan va ichida chaqirilgan.
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 🔟 Rekursiv funksiya (soddalashtirilgan)
# Bu funksiya o‘zini ichida chaqiradi, bu juda muhim mavzu (ayniqsa faktorial, fibonachchi kabi misollarda).
# Va bu Python’dagi funksiyalarning o‘rta-darajadagi turi hisoblanadi.

def hisobla(son):
    if son > 0:
        print(son)
        hisobla(son - 1)  # o‘zini qayta chaqiradi
hisobla(5)
# Natija:
# 5
# 4
# 3
# 2
# 1
# ☑️ Funksiya o‘zini ichida chaqirib, sonni kamaytirib chiqaradi.
# Har chaqirilganda son 1 ga kamayadi, 0 bo‘lganda to‘xtaydi.
#-------------------------------------------------------------------------------------------------------------------------------#




