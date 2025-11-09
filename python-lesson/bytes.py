#-------------------------------------------------------------------------------------------------------------------------------#
# 🔢 6️⃣ bytes (o‘zgarmas baytlar ketma-ketligi)
# bytes — bu matn emas, balki baytlar (0–255 oraliqdagi sonlar) to‘plami.
# Asosan fayllar, kodlash, tarmoqlar bilan ishlashda qo‘llanadi.
#-------------------------------------------------------------------------------------------------------------------------------#
b = b'python'

# count() – nechta marta uchrashini qaytaradi
print(b.count(b'o'))
# 1

# find() – qayerda joylashganini qaytaradi
print(b.find(b't'))
# 2

# replace() – belgilarni almashtiradi
print(b.replace(b'p', b'P'))
# b'Python'

# split() – bo‘lish
print(b'spam eggs'.split())
# [b'spam', b'eggs']

# upper(), lower()
print(b'abc'.upper())
# b'ABC'

# startswith(), endswith()
print(b'file.txt'.endswith(b'.txt'))
# True

# join() – elementlarni birlashtiradi
print(b'-'.join([b'a', b'b']))
# b'a-b'

# translate() – belgilarni almashtirish jadvali bo‘yicha
tbl = bytes.maketrans(b'abc', b'123')
print(b'abc'.translate(tbl))
# b'123'
#-------------------------------------------------------------------------------------------------------------------------------#