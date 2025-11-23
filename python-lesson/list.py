#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ append() metodi
# append() -> Ro'yxat oxiriga yangi element qo'shadi
# ✅ Метод append()
# append() → добавляет новый элемент в конец списка
fruits = ['olma', 'banan']
fruits.append('uzum')  # yangi meva ro'yxat oxiriga qo'shildi / новый фрукт добавлен в конец списка
print(fruits)
# ['olma', 'banan', 'uzum']
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ insert() metodi
# insert(index, value) -> Belgilangan indexga elementni joylashtiradi
# ✅ Метод insert()
# insert(index, value) → вставляет элемент в указанный индекс
numbers = [1, 2, 4]
numbers.insert(2, 3)  # 2-indexga 3 raqami qo'shildi / В индекс 2 добавлено число 3
print(numbers)
# [1, 2, 3, 4]
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ remove() metodi
# remove(value) -> Ro'yxatdan birinchi uchragan mos qiymatni o'chiradi
# ✅ Метод remove()
# remove(value) → удаляет из списка первое найденное соответствующее значение
colors = ['qizil', 'yashil', 'ko\'k', 'yashil']
colors.remove('yashil')  # faqat birinchi 'yashil' o'chiriladi / будет удалён только первый «yashil»
print(colors)
# ['qizil', 'ko\'k', 'yashil']
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ pop() metodi
# pop(index) -> Belgilangan indexdagi elementni ro'yxatdan o'chirib, qaytaradi
# ✅ Метод pop()
# pop(index) → удаляет элемент по указанному индексу и возвращает его
names = ['Ali', 'Vali', 'Hasan']
removed = names.pop(1)  # 1-indexdagi 'Vali' o'chirildi / Элемент 'Vali' по индексу 1 был удалён
print(removed)  # 'Vali'
print(names)
# ['Ali', 'Hasan']
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ index() metodi
# index(value) -> Elementning birinchi uchragan indeksini qaytaradi
# ✅ Метод index()
# index(value) → возвращает индекс первого найденного элемента
cities = ['Toshkent', 'Samarqand', 'Buxoro']
i = cities.index('Buxoro')  # 'Buxoro' nechinchi o'rinda? / На каком месте находится «Buxoro»?
print(i)
# 2
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ count() metodi
# count(value) -> Ro'yxatda berilgan qiymat necha marta uchrashini qaytaradi
# ✅ Метод count()
# count(value) → возвращает, сколько раз указанное значение встречается в списке
nums = [1, 2, 2, 3, 2, 4]
cnt = nums.count(2)  # 2 raqami nechta? / Сколько раз встречается число 2?
print(cnt)
# 3
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ sort() metodi
# sort() -> Ro'yxatni o'sish tartibida saralaydi (asl ro'yxat o'zgaradi)
# ✅ Метод sort()
# sort() → сортирует список по возрастанию (исходный список изменяется)
scores = [87, 95, 68, 100]
scores.sort()
print(scores)
# [68, 87, 95, 100]
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ reverse() metodi
# reverse() -> Ro'yxat elementlarini teskari tartibga o'giradi
# ✅ Метод reverse()
# reverse() → разворачивает элементы списка в обратном порядке
letters = ['a', 'b', 'c']
letters.reverse()
print(letters)
# ['c', 'b', 'a']
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ copy() metodi
# copy() -> Ro'yxatning nusxasini yaratadi
# ✅ Метод copy()
# copy() → создаёт копию списка
original = [1, 2, 3]
duplicate = original.copy()
print(duplicate)
# [1, 2, 3]
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ clear() metodi
# clear() -> Ro'yxatdagi barcha elementlarni o'chiradi
# ✅ Метод clear()
# clear() → удаляет все элементы из списка
data = [10, 20, 30]
data.clear()
print(data)
# []
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ extend() metodi
# extend(iterable) -> Ro'yxatga boshqa ro'yxat elementlarini qo'shadi
# ✅ Метод extend()
# extend(iterable) → добавляет в список элементы из другого списка
a = [1, 2]
b = [3, 4]
a.extend(b)  # a ro'yxatiga b ro'yxati qo'shildi / к списку a был добавлен список b
print(a)
# [1, 2, 3, 4]
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ Python’dagi list obyektiga tegishli rasmiy metodlar ro‘yxati:
# Bu ro‘yxat dir(list) natijasiga va Python dokumentatsiyasiga asoslangan.
# ✅ Официальный список методов, относящихся к объекту list в Python:
# Этот список основан на результате dir(list) и документации Python.
#-------------------------------------------------------------------------------------------------------------------------------#
# | №  |   Metod       | Vazifasi (UZ)                                  | Функция (RU)                                  |
# | -- | ------------- | ---------------------------------------------- | --------------------------------------------- |
# | 1  |   append()    | Oxiriga element qo‘shish                       | Добавление элемента в конец                   |
# | 2  |   extend()    | Boshqa iterable elementlari bilan kengaytirish | Расширение списка элементами другого iterable |
# | 3  |   insert()    | Belgilangan indexga element joylash            | Вставка элемента по указанному индексу        |
# | 4  |   remove()    | Birinchi mos elementni o‘chirish               | Удаление первого подходящего элемента         |
# | 5  |   pop()       | Elementni o‘chirib, qiymatini qaytarish        | Удаление элемента и возврат его значения      |
# | 6  |   clear()     | Barcha elementlarni o‘chirish                  | Удаление всех элементов                       |
# | 7  |   index()     | Element indeksini topish                       | Поиск индекса элемента                        |
# | 8  |   count()     | Element nechta ekanligini sanash               | Подсчёт количества элементов                  |
# | 9  |   sort()      | Tartiblash                                     | Сортировка                                    |
# | 10 |   reverse()   | Teskari tartiblash                             | Обратная сортировка                           |
# | 11 |   copy()      | Ro‘yxat nusxasini olish                        | Получение копии списка                        |
#-------------------------------------------------------------------------------------------------------------------------------#
# ✅ Ya'ni, faqat 11 ta rasmiy metod bor / То есть существует всего 11 официальных методов
#-------------------------------------------------------------------------------------------------------------------------------#