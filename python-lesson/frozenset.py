#-------------------------------------------------------------------------------------------------------------------------------#
# frozenset — bu set kabi elementlar to‘plami, lekin o‘zgartirib bo‘lmaydigan (immutable).
# Ya’ni add(), remove() kabi metodlari yo‘q.
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 1. copy()
fs = frozenset({1, 2, 3})
print(fs.copy())
# frozenset({1, 2, 3})
# 🔄 O‘zgarmas nusxasini beradi.
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 2. difference(*others)
fs1 = frozenset({1, 2, 3})
fs2 = frozenset({2})
print(fs1.difference(fs2))
# frozenset({1, 3})
# 🔍 Faqat fs1da bor, boshqalarda yo‘q elementlar.
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 3. intersection(*others)
fs1 = frozenset({1, 2, 3})
fs2 = frozenset({2, 4})
print(fs1.intersection(fs2))
# frozenset({2})
# 🔗 Umumiy elementlar.
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 4. isdisjoint(other)
fs1 = frozenset({1, 2})
fs2 = frozenset({3, 4})
print(fs1.isdisjoint(fs2))
# True
# ❌ Umumiy elementi yo‘qmi?
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 5. issubset(other)
fs1 = frozenset({1, 2})
fs2 = frozenset({1, 2, 3})
print(fs1.issubset(fs2))
# True
# 🔽 To‘liq ichida bormi?
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 6. issuperset(other)
fs1 = frozenset({1, 2, 3})
fs2 = frozenset({2, 3})
print(fs1.issuperset(fs2))
# True
# 🔼 To‘liq qamrab olganmi?
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 7. symmetric_difference(other)
fs1 = frozenset({1, 2, 3})
fs2 = frozenset({2, 4})
print(fs1.symmetric_difference(fs2))
# frozenset({1, 3, 4})
# 🔁 Faqat birida bor, ikkalasida birgalikda bo‘lmaganlar.
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 8. union(*others)
fs1 = frozenset({1, 2})
fs2 = frozenset({2, 3})
print(fs1.union(fs2))
# frozenset({1, 2, 3})
# 🔗 To‘plamlar birlashmasi.
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 9. __contains__() → in operatori
fs = frozenset({1, 2, 3})
print(2 in fs)
# True
# 🔍 Element bor-yo‘qligini tekshiradi.
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 10. __len__() → len()
fs = frozenset({1, 2, 3})
print(len(fs))
# 3
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 11. __iter__() → for orqali aylanish
fs = frozenset({1, 2, 3})
for i in fs:
    print(i)
# 1
# 2
# 3
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 12. __eq__(other) → == operatori
fs1 = frozenset({1, 2, 3})
fs2 = frozenset({1, 2, 3})
print(fs1 == fs2)
# True
# 🟢 To‘plamlar bir xil elementlarga ega bo‘lsa, == True beradi.
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 13. __ne__(other) → != operatori
fs1 = frozenset({1, 2, 3})
fs2 = frozenset({2, 3})
print(fs1 != fs2)
# True
# 🔴 Elementlar bir xil bo‘lmasa, != True beradi.
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 14. __lt__(other) → < operatori (strict subset)
fs1 = frozenset({1, 2})
fs2 = frozenset({1, 2, 3})
print(fs1 < fs2)
# True
# 📉 fs1 — fs2ning strict qismini bildiradi.
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 15. __le__(other) → <= operatori (subset)
fs1 = frozenset({1, 2, 3})
fs2 = frozenset({1, 2, 3})
print(fs1 <= fs2)
# True
# ✅ fs1 — fs2ga teng yoki kichik qism bo‘lishi mumkin.
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 16. __gt__(other) → > operatori (strict superset)
fs1 = frozenset({1, 2, 3})
fs2 = frozenset({1, 2})
print(fs1 > fs2)
# True
# 📈 fs1 — fs2ni to‘liq o‘z ichiga olgan bo‘lsa, True.
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ 17. __ge__(other) → >= operatori (superset)
fs1 = frozenset({1, 2, 3})
fs2 = frozenset({1, 2, 3})
print(fs1 >= fs2)
# True
# 🟰 fs1 — fs2ga teng yoki kattaroq bo‘lishi mumkin.
#-------------------------------------------------------------------------------------------------------------------------------#
# 📊 Yakuniy ro‘yxat: frozenset metodlari = 17 ta
# №	Metod	Vazifasi
# 1	copy()	Nusxa olish
# 2	difference()	Farqni olish
# 3	intersection()	Kesishma
# 4	isdisjoint()	Umumiy elementi yo‘qmi
# 5	issubset()	Subsetmi?
# 6	issuperset()	Supersetmi?
# 7	symmetric_difference()	Umumiy bo‘lmaganlar
# 8	union()	Birlashma
# 9	in, __contains__()	A’zolikni tekshirish
# 10	len(), __len__()	Uzunlik
# 11	__iter__()	Takrorlash
# 12	__eq__	==	Tenglik
# 13	__ne__	!=	Teng emaslik
# 14	__lt__	<	Kichik (subset)
# 15	__le__	<=	Kichik yoki teng
# 16	__gt__	>	Katta (superset)
# 17	__ge__	>=	Katta yoki teng (superset)
#-------------------------------------------------------------------------------------------------------------------------------#