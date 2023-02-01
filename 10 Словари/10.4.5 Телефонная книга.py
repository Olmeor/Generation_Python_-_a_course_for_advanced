# Телефонная книга
# Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера.
#
# У каждого из друзей Тимура может быть один или более телефонных номеров. Напишите программу, которая поможет Тимуру
# находить все номера определённого друга.

# put your python code here
contacts = {}
for _ in range(int(input())):
    phone, name = input().lower().split()
    contacts.setdefault(name, []).append(phone)
for _ in range(int(input())):
    print(*contacts.get(input().lower(), ['абонент не найден']))
