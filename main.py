



def show_all():
    file = open('sample.txt', 'r', encoding='UTF=8')
    data = file.readlines()
    print(data)
    file.close()
    #print(data[0])
    for i in data:
        print(i)
def add_contact():
    file = open('sample.txt', 'a', encoding='UTF=8')
    data = input("Введите фамилию, телефон, комментарий через точки с запятыми: ") #.split(';')
    file.write(data)
    #print('input data', data)



def main_menu():
    print("Main menu")
    print("1. Показать всю книгу")
    print("2. Добавить новую запись")
    print("3. Редактировать запись")
    print("4. Поиск контакта")
    print("5. Удалить контакт")
    print("6. Go back to main menu")

def find_contact():
    find_string = input("Введите запрос: ")
    file = open('sample.txt', 'r', encoding='UTF=8')
    data = file.readlines()
    for data_str in data:
        if find_string in data_str:
            print('found data = ', data_str)


def edit_contact():
    find_string = input("Введите запрос: ")
    replace_string = input("Введите замену: ")
    file= open('sample.txt', 'r', encoding='UTF-8')
    data = file.read()
    if find_string not in data:
        print("Контакт не найден")
        return
    new_data = data.replace(find_string, replace_string)
    file = open('sample.txt', 'w', encoding='UTF-8')
    file.write(new_data)
    print("Изменения успешно сохранены")
    file.close()

def delete_contact():
    find_string = input("Введите запрос: ")
    file = open('sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file = open('sample.txt', 'w', encoding='UTF-8')
    for line in data:
        if line.strip("\n") != find_string:
            file.write(line)
    file.close()
    print("Изменения успешно сохранены")


if __name__ == "__main__":
    main_menu()

    while True:
        choose = int(input('Введите пукт меню: '))
        if choose == 1:
            show_all()
        if choose == 2:
            add_contact()
        if choose == 3:
            edit_contact()
        if choose == 4:
            find_contact()
        if choose == 5:
            delete_contact()
        if choose == 6:
            main_menu()


"""""""""
file = open('sample.txt', 'r', encoding='UTF-8')
data = file.readlines()
print(data)
file.close()
"""""""""