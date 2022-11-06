import requests

data = requests.get('http://127.0.0.1:5000/user/4')

# data = requests.post('http://127.0.0.1:5000/user/', json={'name': 'Vasya',
#                                                            'password': 'jkhglkj^&*785HJjhg',
#                                                            'email': 'vasya@mail.ru',
#                                                           })
# data = requests.delete('http://127.0.0.1:5000/user/1')


# data = requests.get('http://127.0.0.1:5000/ads/1')

# data = requests.post('http://127.0.0.1:5000/ads/', json={'title': 'Simple advertisement',
#                                                            'content': 'Simple text',
#                                                            'user_id': 2,
#                                                           })
# data = requests.patch('http://127.0.0.1:5000/ads/4', json={'content': 'Simple text',
#                                                            'user_id': 3,
#                                                           })


print(data.status_code)
print(data.text)

