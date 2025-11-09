#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ append() metodi
# append() -> Ro'yxat oxiriga yangi element qo'shadi
fruits = ['olma', 'banan']
fruits.append('uzum')  # yangi meva ro'yxat oxiriga qo'shildi
print(fruits)
# ['olma', 'banan', 'uzum']
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ insert() metodi
# insert(index, value) -> Belgilangan indexga elementni joylashtiradi
numbers = [1, 2, 4]
numbers.insert(2, 3)  # 2-indexga 3 raqami qo'shildi
print(numbers)
# [1, 2, 3, 4]
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ remove() metodi
# remove(value) -> Ro'yxatdan birinchi uchragan mos qiymatni o'chiradi
colors = ['qizil', 'yashil', 'ko\'k', 'yashil']
colors.remove('yashil')  # faqat birinchi 'yashil' o'chiriladi
print(colors)
# ['qizil', 'ko\'k', 'yashil']
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ pop() metodi
# pop(index) -> Belgilangan indexdagi elementni ro'yxatdan o'chirib, qaytaradi
names = ['Ali', 'Vali', 'Hasan']
removed = names.pop(1)  # 1-indexdagi 'Vali' o'chirildi
print(removed)  # 'Vali'
print(names)
# ['Ali', 'Hasan']
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ index() metodi
# index(value) -> Elementning birinchi uchragan indeksini qaytaradi
cities = ['Toshkent', 'Samarqand', 'Buxoro']
i = cities.index('Buxoro')  # 'Buxoro' nechinchi o'rinda?
print(i)
# 2
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ count() metodi
# count(value) -> Ro'yxatda berilgan qiymat necha marta uchrashini qaytaradi
nums = [1, 2, 2, 3, 2, 4]
cnt = nums.count(2)  # 2 raqami nechta?
print(cnt)
# 3
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ sort() metodi
# sort() -> Ro'yxatni o'sish tartibida saralaydi (asl ro'yxat o'zgaradi)
scores = [87, 95, 68, 100]
scores.sort()
print(scores)
# [68, 87, 95, 100]
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ reverse() metodi
# reverse() -> Ro'yxat elementlarini teskari tartibga o'giradi
letters = ['a', 'b', 'c']
letters.reverse()
print(letters)
# ['c', 'b', 'a']
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ copy() metodi
# copy() -> Ro'yxatning nusxasini yaratadi
original = [1, 2, 3]
duplicate = original.copy()
print(duplicate)
# [1, 2, 3]
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ clear() metodi
# clear() -> Ro'yxatdagi barcha elementlarni o'chiradi
data = [10, 20, 30]
data.clear()
print(data)
# []
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ extend() metodi
# extend(iterable) -> Ro'yxatga boshqa ro'yxat elementlarini qo'shadi
a = [1, 2]
b = [3, 4]
a.extend(b)  # a ro'yxatiga b ro'yxati qo'shildi
print(a)
# [1, 2, 3, 4]
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ Python’dagi list obyektiga tegishli rasmiy metodlar ro‘yxati:
# Bu ro‘yxat dir(list) natijasiga va Python dokumentatsiyasiga asoslangan.

# Metod	Vazifasi
# append()	Oxiriga element qo‘shish
# extend()	Boshqa iterable’ni elementlar bilan kengaytirish
# insert()	Belgilangan indexga element joylash
# remove()	Birinchi mos elementni o‘chirish
# pop()	Elementni o‘chirib, qiymatini qaytarish
# clear()	Barcha elementlarni o‘chirish
# index()	Element indeksini topish
# count()	Element nechta ekanligini sanash
# sort()	Tartiblash
# reverse()	Teskari tartiblash
# copy()	Ro‘yxat nusxasini olish
# ✅ Ya'ni, faqat 11 ta rasmiy metod bor.
#-------------------------------------------------------------------------------------------------------------------------------#
