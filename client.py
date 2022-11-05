import requests

# print()
data = requests.get('http://127.0.0.1:5000/user/1')
# , json={'name': 'Boris',
#                                                           'password': 'klhg#YFJH*%^J865',
#                                                           'email': 'boris@mail.ru',
#                                                           }, timeout=5, )

print(data.status_code)
print(data.text)
