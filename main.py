import re

phone_num = input("Введіть свій мобільний номер: ")
full_name = input("Введіть свій ПІБ: ")
e_mail = input("Введіть свою електронну пошту: ")
home_phone = input("Введіть cвій домашній номер телефону: ")

find = re.findall(r"^\+?380\d{9}$", phone_num)
find_1 = re.findall(r"^\s*\w{2,16}\s+\w{2,16}\s+\w{2,16}\s*$", full_name)
find_2 = re.findall(r"^\w+[\w_.]*\w+@\w{2,10}[.]\w{2,10}$", e_mail)
find_3 = re.findall(r"^\d{6}$", home_phone)

print(find)
print(find_1)
print(find_2)
print(find_3)

