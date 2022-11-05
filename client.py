import requests


data = requests.post('http://127.0.0.1:5000/user/', json={'name': 'Stepan',
                                                           'password': 'king#YFJH*%^J865',
                                                           'email': 'stepan@mail.ru',
                                                          })
# data = requests.get('http://127.0.0.1:5000/user/1')


print(data.status_code)

