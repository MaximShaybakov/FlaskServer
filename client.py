import requests

data = requests.get('http://127.0.0.1:5000/user/3')

# data = requests.post('http://127.0.0.1:5000/user/', json={'name': 'Kolya',
#                                                            'password': 'jkhglkj^&*785HJjhg',
#                                                            'email': 'kolya@mail.ru',
#                                                           })
# data = requests.patch('http://127.0.0.1:5000/user/', json={'email': 'kolya@mail.ru'})
#
#
# data = requests.delete('http://127.0.0.1:5000/user/5')


# data = requests.get('http://127.0.0.1:5000/ads/1')

# data = requests.post('http://127.0.0.1:5000/ads/', json={'title': 'Simple advertisement',
#                                                            'content': 'Simple text',
#                                                            'user_id': 2,
#                                                           })
# data = requests.patch('http://127.0.0.1:5000/ads/1', json={'title': 'simple ads',
#                                                            'content': 'This could be your ad'
#                                                           })
# data = requests.delete('http://127.0.0.1:5000/ads/4')

print(data.status_code)
print(data.text)
