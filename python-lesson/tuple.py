#-------------------------------------------------------------------------------------------------------------------------------#
# Python’dagi tuple — bu tartiblangan (ordered) va o‘zgarmas (immutable) elementlar to‘plami.
# Ya’ni, yaratib bo‘linganidan keyin elementlarini o‘zgartirib, qo‘shib yoki o‘chirib bo‘lmaydi.
# ✅ 1. count()
# count(value) → Ko‘rsatilgan qiymat tuple ichida nechta marta borligini qaytaradi
raqamlar = (1, 2, 2, 3, 2)
print(raqamlar.count(2))
# 💬 2 soni tuple ichida 3 marta mavjud.
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 2. index()
# index(value) → Qiymat qayerda birinchi marta uchrashini qaytaradi (indeksini)
mevalar = ('olma', 'banan', 'olma', 'gilos')
print(mevalar.index('olma'))  # 0
# 💬 olma birinchi marta 0-indexda joylashgan.
#-------------------------------------------------------------------------------------------------------------------------------#
# 📊 Yakuniy rasmiy ro‘yxat:
# №	Metod	Vazifasi
# 1	count()	Berilgan qiymat nechta marta borligini hisoblaydi
# 2	index()	Qiymatning birinchi indeksini qaytaradi