# 🔢 int — butun sonlar (integer)
# Python'da butun sonlar uchun 4 ta metod mavjud.
# int — bu butun qiymatlarni ifodalaydigan ma’lumot turi.
# U sonlarning uzunligini bitlarda aniqlash, baytga o‘tkazish, baytdan qaytarish kabi metodlarga ega.
#-------------------------------------------------------------------------------------------------------------------------------#
x = int(5.9)
print(x)
# 5
#-------------------------------------------------------------------------------------------------------------------------------#
# bit_length() – sonni ifodalash uchun nechta bit kerakligini qaytaradi
x = 15
print(x.bit_length())
# 4  (15 = 1111 → 4 bit)
#-------------------------------------------------------------------------------------------------------------------------------#
# to_bytes(length, byteorder) – sonni bayt ko‘rinishiga o‘tkazadi
y = 300
print(y.to_bytes(2, 'big'))
# b'\x01,'
#-------------------------------------------------------------------------------------------------------------------------------#
# from_bytes(bytes, byteorder) – baytlardan son hosil qiladi
b = (1).to_bytes(2, 'big')
print(int.from_bytes(b, 'big'))
# 1
#-------------------------------------------------------------------------------------------------------------------------------#