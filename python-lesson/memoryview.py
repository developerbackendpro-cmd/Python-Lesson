#-------------------------------------------------------------------------------------------------------------------------------#
# 🔢 8️⃣ memoryview (xotiradagi obyektni ko‘rish)
# memoryview — bu baytlar obyektini nusxa olmasdan o‘qish yoki tahrirlash imkonini beradi.
# Juda katta fayllar bilan ishlashda tezlikni oshiradi.
#-------------------------------------------------------------------------------------------------------------------------------#
data = bytearray(b'Python')
m = memoryview(data)
# tobytes() – xotirani baytga aylantiradi
print(m.tobytes())
# b'Python'
#-------------------------------------------------------------------------------------------------------------------------------#
# tolist() – ro‘yxat ko‘rinishida qaytaradi
print(m.tolist())
# [80, 121, 116, 104, 111, 110]
#-------------------------------------------------------------------------------------------------------------------------------#
# cast() – xotira formatini o‘zgartiradi (masalan 'B' = bayt)
print(m.cast('B'))
# <memoryview at 0x...>
#-------------------------------------------------------------------------------------------------------------------------------#
# readonly – obyekt faqat o‘qish uchunmi?
print(m.readonly)
# False
#-------------------------------------------------------------------------------------------------------------------------------#
