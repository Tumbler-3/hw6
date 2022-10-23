import re

with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
    content = file.read()

def show_emails():
    email_list = re.findall(r'\w+@\w+\W\w+\.{0,1}\w+', content)
    with open('email.txt', 'w', encoding='utf-8') as file:
        for email in email_list:
            file.write(f'{email}\n')
    email_file = open('email.txt', 'r').read()
    print(email_file)

def show_files():    
    file_list = re.findall(r'\s\w+\.\w{3,4}', content)
    with open('files.txt', 'w', encoding='utf-8') as file:
        for files in file_list:
            file.write(f'{files}\n')
    file_file = open('files.txt', 'r').read()
    print(file_file)

def show_colors():    
    color_list = re.findall(r'#\w+', content)
    with open('colors.txt', 'w', encoding='utf-8') as file:
        for color in color_list:
            file.write(f'{color}\n')
    color_file = open('colors.txt', 'r').read()
    print(color_file)

def menu():
    x = ''
    print('''Веедите числа от 1 до 4:
        1 - считать и сохранить почту
        2 - считать и сохранить названия файлов
        3 - считать и сохранить цвета
        4 - выйти
        ''')
    while True:
        try:
            x = int(input('Число: '))
        except:
            print('Введите число - не букву')
        break

    if x == 1:
        show_emails()
    elif x == 2:
        show_files()
    elif x == 3:
        show_colors()
    elif x == 4:
        return 4
    else:
        print(f'\nНеверное число')

while True:
    y = menu()
    if y == 4:
        break