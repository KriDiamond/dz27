def add_list():
    user_string = input("Введите элементы списка через пробелы: ")
    user_list = [int(num) for num in user_string.split()]
    return user_list


def show_info_about_user_list(user_list):
    user_set = set(user_list)
    print(f"""
Введенный список элементов: {user_list}
Количество элементов в введенном списке: {len(user_list)}

Список уникальных элементов: {user_set}
Количество элементов в введенном списке: {len(user_set)}""")


user_list = add_list()
show_info_about_user_list(user_list)