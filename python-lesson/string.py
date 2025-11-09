#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 1. capitalize()
# Birinchi harfni katta qiladi, qolganlarini kichik
s = "python"
print(s.capitalize())
# Python
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 2. casefold()
# Matnni to‘liq kichik harflarga o‘giradi (hatto tilga xos harflar uchun ham)
# Nemis tilidagi "ß" harfi casefold() da "ss" ga aylanadi.
# Bu Python (va Unicode) standarti bo‘yicha to‘g‘ri bo‘lgan kengaytirilgan kichiklashtirish (case folding) qoidasi.

s = "Straße"
print(s.casefold())
# strasse
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 3. center(width)
# Matnni markazga joylashtiradi (berilgan uzunlikka)
s = "Python"
print(s.center(10))
# '  Python  '
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 4. count(substring)
# Necha marta uchrashini hisoblaydi
s = "banana"
print(s.count('a'))
# 3
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 5. endswith(sub)
# Matn shu qism bilan tugaydimi?
s = "hello.py"
print(s.endswith('.py'))
# True
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 6. startswith(sub)
# Matn shu qism bilan boshlanadimi?
s = "python"
print(s.startswith('py'))
# True
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 7. expandtabs(tabsize)
# \t belgilarini bo‘shliqlarga almashtiradi
s = "a\tb\tc"
print(s.expandtabs(4))
# 'a   b   c'
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 8. find(sub)
# Substring qayerda boshlanadi? Topilmasa -1
s = "python"
print(s.find('th'))
# 2
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 9. rfind(sub)
# Oxiridan boshlab substringni qidiradi
s = "banana"
print(s.rfind('a'))
# 5
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 10. index(sub)
# Substringni topadi (topilmasa xatolik)
s = "python"
print(s.index('t'))
# 2
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 11. rindex(sub)
# Oxiridan substringni topadi (topilmasa xatolik)
s = "banana"
print(s.rindex('a'))
# 5
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 12. isalnum()
# Harflar yoki raqamlardan iboratmi?
s = "abc123"
print(s.isalnum())
# True
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 13. isalpha()
# Faqat harflardan iboratmi?
s = "abc"
print(s.isalpha())
# True
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 14. isdigit()
# Faqat raqamlardan iboratmi?
s = "12345"
print(s.isdigit())
# True
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 15. islower()
# Faqat kichik harflarmi?
s = "hello"
print(s.islower())
# True
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 16. isupper()
# Faqat katta harflarmi?
s = "HELLO"
print(s.isupper())
# True
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 17. isspace()
# Faqat bo‘shliq (space, tab) bormi?
s = "   \t"
print(s.isspace())
# True
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 18. istitle()
# Har bir so‘z katta harf bilan boshlanadimi?
s = "Hello World"
print(s.istitle())
# True
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 19. isnumeric()
# Faqat raqamlar (raqam belgilar, rim raqamlari) bormi?
s = "Ⅻ"
print(s.isnumeric())
# True
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 20. isdecimal()
# Faqat 0–9 oraliqdagi raqamlar bormi?
s = "123"
print(s.isdecimal())
# True
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 21. join(iterable)
# Elementlarni bitta matnga birlashtiradi
s = "-"
print(s.join(['a', 'b', 'c']))
# a-b-c
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 22. split()
# Matnni so‘zlarga ajratadi
s = "hello world"
print(s.split())
# ['hello', 'world']
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 23. rsplit()
# O‘ngdan boshlab bo‘lish
s = "a,b,c"
print(s.rsplit(',', 1))
# ['a,b', 'c']
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 24. partition()
# Belgilangan belgiga bo‘ladi → (oldi, ajratuvchi, qoldiq)
s = "hello:world"
print(s.partition(':'))
# ('hello', ':', 'world')
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 25. rpartition()
# Oxirgi uchragan ajratuvchiga qarab bo‘linadi
s = "a:b:c"
print(s.rpartition(':'))
# ('a:b', ':', 'c')
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 26. lower(), upper(), title(), capitalize(), swapcase()
s = "hello WORLD"
print(s.lower())      # hello world
print(s.upper())      # HELLO WORLD
print(s.title())      # Hello World
print(s.capitalize()) # Hello world
print(s.swapcase())   # HELLO world
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 27. ljust(width[, fillchar])
# Matnni chapga siljitadi, o'ngini to‘ldiradi
s = "kitob"
print(s.ljust(10, '-'))
# 'kitob-----'
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 28. rjust(width[, fillchar])
# Matnni o‘ngga siljitadi, chapini to‘ldiradi
s = "kitob"
print(s.rjust(10, '*'))
# '*****kitob'
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 29. zfill(width)
# Chap tomonini 0 bilan to‘ldiradi
s = "42"
print(s.zfill(5))
# '00042'
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 30. lstrip([chars])
# Matn boshidan berilgan belgilarni o‘chiradi
s = "---salom---"
print(s.lstrip("-"))
# 'salom---'
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 31. rstrip([chars])
# Matn oxiridan belgilarni o‘chiradi
s = "---salom---"
print(s.rstrip("-"))
# '---salom'
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 32. strip([chars])
# Boshidan ham, oxiridan ham belgilangan belgilarni olib tashlaydi
s = "---salom---"
print(s.strip("-"))
# 'salom'
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 33. replace(old, new[, count])
# Matndagi eski belgilarni yangisiga almashtiradi
s = "olma va olma"
print(s.replace("olma", "nok"))
# 'nok va nok'
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 34. splitlines([keepends])
# Matnni satrlar bo‘yicha ajratadi
s = "Salom\ndunyo\nPython"
print(s.splitlines())
# ['Salom', 'dunyo', 'Python']
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 35. encode(encoding='utf-8')
# Matnni baytlarga kodlaydi
s = "salom"
print(s.encode())
# b'salom'
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 36. format(*args, **kwargs)
# Matn ichiga qiymat joylash uchun ishlatiladi
s = "Mening ismim {} va yoshim {}"
print(s.format("Ali", 21))
# 'Mening ismim Ali va yoshim 21'
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 37. format_map(mapping)
# Lug‘at orqali formatlash
info = {'ism': 'Ali', 'yosh': 21}
s = "Ismi: {ism}, Yoshi: {yosh}"
print(s.format_map(info))
# 'Ismi: Ali, Yoshi: 21'
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 38. translate(table)
# Belgilarni berilgan jadval bo‘yicha almashtiradi
table = str.maketrans("ae", "12")
print("salom".translate(table))
# s1lom
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 39. maketrans(x, y)
# translate() uchun jadval yaratadi
tr = str.maketrans("abc", "123")
print("abcabc".translate(tr))
# 123123
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 40. isidentifier()
# Matn Python identifikator bo‘la oladimi?
print("ism1".isidentifier())
# True
print("1ism".isidentifier())
# False
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 41. isprintable()
# Matn faqat chop etish mumkin bo‘lgan belgilarni o‘z ichiga olganmi?
print("salom".isprintable())
# True
print("salom\n".isprintable())
# False
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 42. isascii()
# Matn faqat ASCII belgilaridangina iboratmi?
print("abc123".isascii())
# True
print("salom😊".isascii())
# False
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 43. removeprefix(prefix)
# Matn boshidagi prefix'ni olib tashlaydi (agar mavjud bo‘lsa)
s = "python3.11"
print(s.removeprefix("python"))
# '3.11'
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 44. removesuffix(suffix)
# Matn oxiridagi suffix'ni olib tashlaydi (agar mavjud bo‘lsa)
s = "filename.txt"
print(s.removesuffix(".txt"))
# 'filename'
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 45. swapcase()
# Har bir harfni katta ↔ kichik o‘zgartiradi
s = "Salom DUNYO"
print(s.swapcase())
# sALOM dunyo
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 46. title()
# Har bir so‘zni bosh harf bilan yozadi
s = "python dasturlash tili"
print(s.title())
# 'Python Dasturlash Tili'
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 47. capitalize()
# Faqat birinchi harfni katta qiladi
s = "python dastur"
print(s.capitalize())
# 'Python dastur'
#-------------------------------------------------------------------------------------------------------------------------------#
# 📊 Yakuniy rasmiy ro‘yxat: string metodlari soni = 47 ta
# Kategoriya	Metodlar
# Harf tekshiruvi	isalpha, isdigit, isnumeric, isalnum, isupper, islower, isspace, istitle, isdecimal, isidentifier, isascii, isprintable
# Matn formatlash	upper, lower, title, capitalize, swapcase, casefold
# Joylashtirish	center, ljust, rjust, zfill
# Bo‘lish va birlashtirish	split, rsplit, splitlines, partition, rpartition, join
# Qidirish	find, rfind, index, rindex, startswith, endswith, count
# O‘chirish	strip, lstrip, rstrip, removeprefix, removesuffix
# Almashtirish	replace, translate, maketrans
# Formatlash	format, format_map
# Kodlash	encode
#-------------------------------------------------------------------------------------------------------------------------------#

