import requests

print()
data = requests.post('http://127.0.0.1:5000/user/', json={'name': 'Stepan',
                                                        'password': 'klhg#YFJH*%^J865',
                                                        'email': 'stepan@mail.ru',
                                                        })

print(data.status_code)
print(data.text)
