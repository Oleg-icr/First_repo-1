import re

text = "Python - потужна; проста, універсальна: мова!"
pattern = r"[;,\-:!\s]+"
elements = re.split(pattern, text)

print(elements)
print(elements[:-1:])

print("--------------------------------------------------------------")

email = "username@domain.com"
pattern = r"(\w+)@(\w+\.\w+)"
i = re.search(pattern, email)

if i:
    user_name = i.group(1)
    domain_name = i.group(2)
    print("Ім'я користувача:", user_name)
    print("Домен:", domain_name)




