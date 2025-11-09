# 📘 Python'dagi Asosiy Maʼlumot Turlari (Data Types)
# Python dasturlash tilida har bir qiymat maʼlum bir data type (maʼlumot turi) ga ega. Quyida Pythonʼdagi asosiy
# (built-in) va eng ko‘p ishlatiladigan maʼlumot turlarining ro‘yxati va izohi keltirilgan:
# Python dasturlash tilida rasmiy (built-in) asosiy maʼlumot turlari soni: ✅ 11 ta asosiy data type mavjud.
#-------------------------------------------------------------------------------------------------------------------------------#
# 1. int – Butun son (integer)
integers = 42
# 🔹 Butun sonlar uchun ishlatiladi: ... -3, -2, -1, 0, 1, 2, 3 ...
# 🔹 Matematik amallar, sikllar, indekslar uchun ishlatiladi.
#-------------------------------------------------------------------------------------------------------------------------------#
# 2. float – O‘nlik son (floating point number)
floats = 3.14
# 🔹 O‘nlik nuqtali sonlar uchun ishlatiladi: 3.0, -0.75, 100.01
# 🔹 Foizlar, ilmiy hisob-kitoblar, aniqlik kerak bo‘lgan joylarda.
#-------------------------------------------------------------------------------------------------------------------------------#
# 3. str – Matn (string)
string = "Anvar"
# 🔹 Matnli ifodalar: "salom", 'Python', "123" (raqam bo‘lsa ham, matn sifatida).
# 🔹 Harflar, gaplar, foydalanuvchi ismlari, fayl nomlari uchun ishlatiladi.
#-------------------------------------------------------------------------------------------------------------------------------#
# 4. bool – Mantiqiy qiymat (boolean)
haqiqat = True
# 🔹 Faqat ikki qiymat: True (rost), False (yolg‘on)
# 🔹 Shartli operatorlarda (if, while) ishlatiladi.
#-------------------------------------------------------------------------------------------------------------------------------#
# 5. NoneType – Hech qanday qiymat emas
javob = None
# 🔹 None maxsus qiymat bo‘lib, o‘zgaruvchiga hali hech narsa berilmaganligini bildiradi.
# 🔹 Bo‘sh qiymat, vaqtincha qiymat yoki default holatlarda ishlatiladi.
#-------------------------------------------------------------------------------------------------------------------------------#
# 6. list – Ro‘yhat (list)
# Python'dagi list — bu tartiblangan, o‘zgaruvchan (mutable) ma'lumotlar to‘plami bo‘lib,
# ichida har xil turdagi elementlar saqlanishi mumkin.
aralash = [
    'salom',                  # str
    42,                       # int
    3.14,                     # float
    True,                     # bool
    False,                    # bool
    None,                     # NoneType
    {'Ism': 'Anvar'},         # dict
    ('Hello World',),         # tuple
    [1, 2, 3],                # list
    {1, 2, 3},                # set
    frozenset([4, 5, 6]),     # frozenset
    2 + 3j                    # complex
]
# 🧠 list — [] kvadrat qavslar yordamida yaratiladi va elementlar vergul bilan ajratiladi.
#-------------------------------------------------------------------------------------------------------------------------------#
# 7. tuple – O‘zgarmas ro‘yhat (tuple)
koordinata = (12.5, 8.3)
# 🔹 Listga o‘xshaydi, lekin o‘zgartirib bo‘lmaydi (immutable).
# 🔹 Qattiq tuzilgan maʼlumotlar uchun: koordinatalar, holatlar.
#-------------------------------------------------------------------------------------------------------------------------------#
# 8. set – To‘plam (set)
raqamlar = {1, 2, 3}
# 🔹 Tartibsiz va takrorlanuvchi qiymatlarsiz to‘plam.
# 🔹 Unikal qiymatlar to‘plamini saqlaydi.
# 🔹 {element1, element2, ...}
#-------------------------------------------------------------------------------------------------------------------------------#
# 9. frozenset – O‘zgarmas set
muzlatilgan = frozenset([1, 2, 3])
# 🔹 set kabi, lekin uni o‘zgartirib bo‘lmaydi.
# 🔹 Hashable object sifatida ishlatiladi (dictionary key sifatida, etc).
#-------------------------------------------------------------------------------------------------------------------------------#
# 10. dict – Lug‘at (dictionary)
talaba = {"ism": "Anvar", "yosh": 25}
# 🔹 Kalit-qiymat juftliklaridan iborat o‘zgaruvchan tip.
# 🔹 {key: value} formatida yoziladi.
# 🔹 Juda keng qo‘llaniladi: foydalanuvchi ma’lumotlari, sozlamalar, JSON parsing
#-------------------------------------------------------------------------------------------------------------------------------#
# 11. complex – Kompleks son
z = 2 + 3j
# 🔹 Matematik kompleks sonlar (haqiqiy + xayoliy qismlar).
# 🔹 Ilmiy va muhandislik hisob-kitoblarida qo‘llaniladi.
#-------------------------------------------------------------------------------------------------------------------------------#
# 🧾 Yakuniy eslatma:
# Python'dagi bu maʼlumot turlari bilan siz har qanday turdagi maʼlumotni ifodalay olasiz.
# Quyida ularning qisqa jamlanmasi:
#
# Turi	Nomi	Misol
# int	Butun son	42
# float	O‘nlik son	3.14
# str	Matn	"Hello"
# bool	Mantiqiy	True, False
# NoneType	Bo‘sh qiymat	None
# list	Ro‘yhat	[1, 2, 3]
# tuple	O‘zgarmas ro‘yhat	(4, 5)
# set	To‘plam	{1, 2}
# frozenset	O‘zgarmas to‘plam	frozenset([1, 2])
# dict	Lug‘at	{"ism": "Ali"}
# complex	Kompleks son	2 + 3j