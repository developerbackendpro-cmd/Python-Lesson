#-------------------------------------------------------------------------------------------------------------------------------#
# Python’dagi set — bu takrorlanmaydigan, tartibsiz elementlar to‘plami.
# Set ichida har bir element noyob bo‘ladi, ya’ni dublikatlarga ruxsat berilmaydi.
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 1. add()
# Yangi element qo‘shadi
sonlar = {1, 2}
sonlar.add(3)
print(sonlar)
# {1, 2, 3}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 2. clear()
# To‘plamni bo‘shatadi
mevalar = {'olma', 'banan'}
mevalar.clear()
print(mevalar)
# set()
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 3. copy()
# Set nusxasini yaratadi
asli = {1, 2, 3}
yangi = asli.copy()
print(yangi)
# {1, 2, 3}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 4. discard(x)
# Elementni o‘chiradi. Topilmasa — xatolik chiqarmaydi.
mevalar = {'olma', 'banan'}
mevalar.discard('olma')
mevalar.discard('nok')  # mavjud emas, lekin xatolik yo‘q
print(mevalar)
# {'banan'}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 5. remove(x)
# Elementni o‘chiradi. Topilmasa — xatolik chiqaradi.
mevalar = {'olma', 'banan'}
mevalar.remove('banan')
print(mevalar)
# {'olma'}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 6. pop()
# Tasodifiy elementni o‘chiradi va qaytaradi
sonlar = {1, 2, 3}
o = sonlar.pop()
print(sonlar)
# {2, 3}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 7. update()
# Setni boshqa iterabledagi elementlar bilan kengaytiradi
a = {1, 2}
a.update([3, 4])
print(a)
# {1, 2, 3, 4}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 8. union()
# Ikkita setni birlashtiradi (takrorlanmas)
a = {1, 2}
b = {2, 3}
print(a.union(b))
# {1, 2, 3}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 9. intersection()
# Umumiy (kesishuvchi) elementlarni qaytaradi
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))
# {2, 3}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 10. difference()
# Faqat `a` da bor, `b` da yo‘q elementlar
a = {1, 2, 3}
b = {2, 4}
print(a.difference(b))
# {1, 3}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 11. symmetric_difference()
# Ikkalasida ham bor, lekin umumiy bo‘lmagan elementlar
a = {1, 2, 3}
b = {2, 4}
print(a.symmetric_difference(b))
# {1, 3, 4}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 12. intersection_update()
# Faqat umumiy elementlarni qoldiradi
a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)
print(a)
# {2, 3}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 13. difference_update()
# `a` dan `b`dagi elementlarni o‘chiradi
a = {1, 2, 3}
b = {2, 4}
a.difference_update(b)
print(a)
# {1, 3}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 14. symmetric_difference_update()
# Umumiy bo‘lganlarni olib tashlab, boshqa elementlar bilan yangilaydi
a = {1, 2, 3}
b = {2, 4}
a.symmetric_difference_update(b)
print(a)
# {1, 3, 4}
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 15. isdisjoint()
# Umumiy element yo‘qmi?
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))
# True
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 16. issubset()
# `a` — `b` ning qismi (subset)mi?
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))
# True
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 17. issuperset()
# `a` — `b` ni to‘liq o‘z ichiga oladimi?
a = {1, 2, 3}
b = {2, 3}
print(a.issuperset(b))
# True
#-------------------------------------------------------------------------------------------------------------------------------#
# 📊 Yakuniy ro‘yxat: set metodlari = 17 ta
# №	Metod	Vazifasi
# 1	add()	Element qo‘shish
# 2	clear()	Hammasini o‘chirish
# 3	copy()	Nusxa olish
# 4	discard()	Elementni o‘chirish (xatolik chiqarmaydi)
# 5	remove()	Elementni o‘chirish (xatolik chiqaradi)
# 6	pop()	Istalgan elementni o‘chirib qaytaradi
# 7	update()	Setni kengaytiradi
# 8	union()	Birlashtirish
# 9	intersection()	Kesishma
# 10 difference()	Farq
# 11 symmetric_difference()	Umumiy bo‘lmaganlar
# 12 intersection_update()	Faqat umumiylarini qoldiradi
# 13 difference_update()	Farqni o‘rniga yozadi
# 14 symmetric_difference_update()	Umumiy bo‘lmaganlar bilan yangilaydi
# 15 isdisjoint()	Umumiy elementi yo‘qmi?
# 16 issubset()	Subset ekanini tekshiradi
# 17 issuperset()	Superset ekanini tekshiradi
#-------------------------------------------------------------------------------------------------------------------------------#
