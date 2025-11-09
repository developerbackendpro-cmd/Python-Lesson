#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 1. get()
# get(key) → Kalitga mos qiymatni qaytaradi. Kalit bo'lmasa xatolik chiqarmaydi, balki None qaytaradi.
talaba = {'ism': 'Ali', 'yosh': 21}
print(talaba.get('ism'))
print(talaba.get('familiya'))
# 'Ali'
# None
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 2. keys()
# keys() → Barcha kalitlarni chiqaradi
talaba = {'ism': 'Ali', 'yosh': 21}
print(talaba.keys())
# dict_keys(['ism', 'yosh'])
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 3. values()
# values() → Barcha qiymatlarni chiqaradi
talaba = {'ism': 'Ali', 'yosh': 21}
print(talaba.values())
# dict_values(['Ali', 21])
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 4. items()
# items() → Har bir juftlikni (key, value) tarzida chiqaradi
talaba = {'ism': 'Ali', 'yosh': 21}
print(talaba.items())
# dict_items([('ism', 'Ali'), ('yosh', 21)])
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 5. update()
# update(dict2) → Boshqa lug‘atdagi juftliklarni birinchisiga qo‘shadi (yoki yangilaydi)
talaba = {'ism': 'Ali'}
talaba.update({'yosh': 21, 'kurs': 3})
print(talaba)
# {'ism': 'Ali', 'yosh': 21, 'kurs': 3}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 6. pop()
# pop(key) → Kalitga mos juftlikni o‘chiradi va qiymatini qaytaradi
talaba = {'ism': 'Ali', 'yosh': 21}
yosh = talaba.pop('yosh')
print(yosh)
print(talaba)
# 21
# {'ism': 'Ali'}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 7. popitem()
# popitem() → Oxirgi qo‘shilgan juftlikni o‘chiradi va (kalit, qiymat) juftligini qaytaradi
talaba = {'ism': 'Ali', 'yosh': 21}
oxirgi = talaba.popitem()
print(oxirgi)
print(talaba)
# ('yosh', 21)
# {'ism': 'Ali'}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 8. setdefault()
# setdefault(key, default) → Kalit mavjud bo‘lmasa, yangi qiymat bilan qo‘shadi. Mavjud bo‘lsa, mavjud qiymatni qaytaradi.
talaba = {'ism': 'Ali'}
talaba.setdefault('yosh', 21)  # 'yosh' mavjud emas, shuning uchun qo‘shiladi
print(talaba)
# {'ism': 'Ali', 'yosh': 21}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 9. clear()
# clear() → Lug‘atdagi barcha elementlarni o‘chiradi
talaba = {'ism': 'Ali', 'yosh': 21}
talaba.clear()
print(talaba)
# {}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 10. copy()
# copy() → Lug‘atning nusxasini yaratadi
asli = {'ism': 'Ali', 'yosh': 21}
nusxa = asli.copy()
print(nusxa)
# {'ism': 'Ali', 'yosh': 21}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 11. fromkeys()
# fromkeys(keys, value) → Berilgan kalitlar bilan yangi lug‘at yaratadi va har biriga bir xil qiymat beradi
kalitlar = ['ism', 'yosh', 'kurs']
yangi = dict.fromkeys(kalitlar, "ma'lum emas")
print(yangi)
# {'ism': 'ma’lum emas', 'yosh': 'ma’lum emas', 'kurs': 'ma’lum emas'}
#-------------------------------------------------------------------------------------------------------------------------------#
# 📊 Yakuniy ro‘yxat: dict metodlar soni = 11 ta
# №	Metod	Vazifasi
# 1	get()	Xavfsiz qiymat olish
# 2	keys()	Barcha kalitlar
# 3	values()	Barcha qiymatlar
# 4	items()	Barcha (kalit, qiymat) juftliklari
# 5	update()	Yangilash yoki kengaytirish
# 6	pop()	Kalit bo‘yicha o‘chirish
# 7	popitem()	Oxirgi elementni o‘chirish
# 8	setdefault()	Yo‘q bo‘lsa, yangi kalit-qiymat qo‘shish
# 9	clear()	Tozalash
# 10 copy()	Nusxa olish
# 11 fromkeys()	Kalitlar ro‘yxatidan yangi lug‘at yasash
#-------------------------------------------------------------------------------------------------------------------------------#