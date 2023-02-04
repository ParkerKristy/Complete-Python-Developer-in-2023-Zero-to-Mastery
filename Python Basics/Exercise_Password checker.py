username = input('What is your username?\n')
password = input('What is your password?\n')
password_lenght = len(password)
secret_pasword = password_lenght * '*'

print(f"Hello {username}, your password {secret_pasword} is {password_lenght} letters long.")