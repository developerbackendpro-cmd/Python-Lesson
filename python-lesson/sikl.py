# 🧠 1️⃣ Sikl (loop) nima?
# Sikl — bu bir xil amallarni bir necha marta takrorlaydigan kod bloki.
# Python’da 2 xil sikl mavjud:
# for sikli — elementlar bo‘yicha yuradi
# while sikli — shart bajarilguncha davom etadi
#-------------------------------------------------------------------------------------------------------------------------------#
# 🧠 1️⃣ Что такое цикл (loop)?
# Цикл — это блок кода, который выполняет одни и те же действия несколько раз.
# В Python существуют 2 вида циклов:
# цикл for — проходит по элементам
# цикл while — выполняется до тех пор, пока условие истинно
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 1️⃣ For sikli (oddiy shakl) / Цикл for (простая форма)
for i in range(5):
    print("Salom", i)
# Natija:
# Salom 0
# Salom 1
# Salom 2
# Salom 3
# Salom 4
# range(5) → 0 dan 4 gacha sonlarni beradi.
# Sikl har safar i ni oshirib, print() ni 5 marta bajaradi.
# Цикл каждый раз увеличивает переменную i и выполняет print() 5 раз.
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 2️⃣ For sikli bilan ro‘yxat ustida ishlash / Работа с циклом for по списку
ismlar = ["Dilshod", "Aziza", "Olim"]
for ism in ismlar:
    print("Salom,", ism)
# Natija:
# Salom, Dilshod
# Salom, Aziza
# Salom, Olim
# Sikl ismlar ro‘yxatidagi har bir elementni ketma-ket oladi
# Цикл последовательно получает каждый элемент из списка имён.
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 3️⃣ While sikli (oddiy shakl) / Цикл while (простая форма)
son = 1
while son <= 5:
    print("Son:", son)
    son = son + 1
# Natija:
# Son: 1
# Son: 2
# Son: 3
# Son: 4
# Son: 5
# while sikli son <= 5 sharti to‘g‘ri bo‘lsa, kodni qayta bajaradi.
# Har safar son 1 ga oshiriladi.
# Цикл while выполняет код, пока условие son <= 5 истинно.
# Каждый раз значение переменной son увеличивается на 1.
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 4️⃣ While siklida if bilan ishlatish / Использование if внутри цикла while
son = 1
while son <= 5:
    if son == 3:
        print("Bu maxsus son:", son)
    else:
        print("Oddiy son:", son)
    son = son + 1
# Natija:
# Oddiy son: 1
# Oddiy son: 2
# Bu maxsus son: 3
# Oddiy son: 4
# Oddiy son: 5
# if orqali har bir bosqichda shartni tekshirish mumkin.
# С помощью if можно проверять условие на каждом этапе.
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 5️⃣ break — siklni to‘xtatish / break — остановка цикла
for i in range(1, 10):
    if i == 5:
        print("Sikl to'xtadi!")
        break
    print("i =", i)
# Natija:
# i = 1
# i = 2
# i = 3
# i = 4
# Sikl to‘xtadi!
# break siklni butunlay to‘xtatadi, shart bajarilgandan so‘ng keyingi takrorlar ishlamaydi.
# break полностью останавливает цикл, и после выполнения условия дальнейшие повторения не выполняются.
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 6️⃣ continue — siklni keyingi aylanishga o‘tkazish / continue — переход к следующей итерации цикла
for i in range(1, 6):
    if i == 3:
        continue  # 3 ni tashlab o‘tadi / Пропускает число 3
    print("i =", i)
# Natija:
# i = 1
# i = 2
# i = 4
# i = 5
# continue siklni to‘xtatmaydi, lekin hozirgi bosqichni tashlab o‘tadi.
# continue не останавливает цикл, но пропускает текущий этап.
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 7️⃣ For sikli bilan if-elif-else ishlatish / Использование if-elif-else в цикле for
for i in range(1, 6):
    if i == 1:
        print("Birinchi son:", i)
    elif i == 5:
        print("Oxirgi son:", i)
    else:
        print("O'rta son:", i)
# Natija:
# Birinchi son: 1
# O‘rta son: 2
# O‘rta son: 3
# O‘rta son: 4
# Oxirgi son: 5
# if / elif / else sikl ichida turli holatlar uchun alohida natija beradi.
# if / elif / else внутри цикла дают отдельный результат для разных ситуаций.
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 8️⃣ While sikli bilan else ishlatish / Использование else с циклом while
son = 1
while son <= 3:
    print("Son:", son)
    son = son + 1
else:
    print("Sikl tugadi!")
# Natija:
# Son: 1
# Son: 2
# Son: 3
# Sikl tugadi!
# while sharti tugagach, else qismi faqat 1 marta ishlaydi. / Когда условие while заканчивается, блок else выполняется только один раз.
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 9️⃣ For sikli bilan else ishlatish / Использование else с циклом for
for i in range(3):
    print("Qiymat:", i)
else:
    print("Sikl yakunlandi!")
# Natija:
# Qiymat: 0
# Qiymat: 1
# Qiymat: 2
# Sikl yakunlandi!
# Agar break ishlatilmasa, else for tugagandan keyin avtomatik ishlaydi. / Если break не используется, блок else автоматически выполняется после завершения цикла for.
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 🔟 Ichma-ich sikl (nested loop) / Вложенный цикл (nested loop)
for i in range(1, 3):
    for j in range(1, 3):
        print("i =", i, ", j =", j)
# Natija:
# i = 1 , j = 1
# i = 1 , j = 2
# i = 2 , j = 1
# i = 2 , j = 2
# Bitta sikl ichida yana bir sikl bo‘lishi mumkin — bu nested loop deyiladi. Внутри одного цикла может быть ещё один цикл — это называется вложенным циклом (nested loop).
#-------------------------------------------------------------------------------------------------------------------------------#
# 🟢 1️⃣1️⃣ Shartli to‘xtovchi while (if bilan)
#    Условно останавливающийся while (с использованием if)
son = 1
while True:
    print("Son:", son)
    son = son + 1
    if son > 3:
        print("Sikl to'xtadi.")
        break
# Natija:
# Son: 1
# Son: 2
# Son: 3
# Sikl to‘xtadi.
# Bu cheksiz while (while True:) bo‘lib, if orqali shart bajarilganda break bilan to‘xtaydi.
# Это бесконечный цикл while (while True:), который останавливается с помощью break, когда условие в if выполняется.
#-------------------------------------------------------------------------------------------------------------------------------#