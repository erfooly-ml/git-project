users = {}
id = input('enter your username')
password = input('enter your password')
if id in users.key:
    print(f'welcome {id}')
else:
    print('sorry, you have to sign in first')
