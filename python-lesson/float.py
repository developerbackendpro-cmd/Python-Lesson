# 🔢 2️⃣ float (o‘nlik son)
# float — bu o‘nlik (kasrli) sonlar turi.
# Unda sonni kasr shaklida, butunligini aniqlash yoki 16-lik ko‘rinishga o‘tkazish metodlari mavjud.
# as_integer_ratio() – sonni kasr ko‘rinishida (surat, maxraj) qaytaradi
#-------------------------------------------------------------------------------------------------------------------------------#
a = 2.5
print(a.as_integer_ratio())
# (5, 2)
#-------------------------------------------------------------------------------------------------------------------------------#
# is_integer() – son butun bo‘lsa True qaytaradi
print((3.0).is_integer())
# True
#-------------------------------------------------------------------------------------------------------------------------------#
# hex() – sonning o‘n oltilik (hexadecimal) ko‘rinishini qaytaradi
print((10.5).hex())
# '0x1.5000000000000p+3'
#-------------------------------------------------------------------------------------------------------------------------------#
# fromhex() – hexdan floatga o‘tkazadi
print(float.fromhex('0x1.5000000000000p+3'))
# 10.5
#-------------------------------------------------------------------------------------------------------------------------------#