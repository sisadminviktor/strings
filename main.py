#9.14 Дано слово. Вывести на экран его последний символ.
# n = input()
# a =n[-1]
# print(a)

#9.15. Дано слово. Вывести на экран его k-й символ.
# word = input()
# symbol = int(input())
# print(word[symbol-1])

#9.16. Дано слово. Определить, одинаковы ли второй и четвертый символы в нем.
# n = input()
# if n[2]==n[4]:
#     print("yes")
# else:
#     print("no")

#9.24. Из слова яблоко путем "вырезок" и "склеек" его букв получить слова блок и око.
# a ="яблоко"
# b= a[1:5]
# c = a[3:6]
# print(b)
# print(c)

#9.38. Дано слово из 12 букв. Поменять местами его трети следующим образом:
#первую треть слова разместить на месте третьей, вторую треть — на месте первой, третью треть — на месте второй;

# s = input("слово из 12 букв")
# a = s[0:4]
# b = s[4:8]
# c = s[8:12]
# res = b+c+a
# print(res)

#9.41. Дано название футбольного клуба. Напечатать его на экране "столбиком".
# n = input()
# for i in n:
#     print(i)

#9.59. Дано предложение. Определить число букв о в нем.
# n = input("введите предложение")
# res = n.count('o')
# print(res)

#9.76.(b) Дано предложение, в котором имеется несколько букв е. Найти:
# n = input()
# res = n.index("e")
# print(res)

# дана строка.Вывести ее в обратном порядке.
# n = input()
# res = n[::-1]
# print(res)