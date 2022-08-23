"""
CRUD

Create
Read - Retrieve
Update
Delete
"""

# a = {'id': 36262, 'title': 'Платье', 'price': 2000, 'description': 'Красивое платье', 'created_at': '23.08.2022'}
# print(a)
# a['title'] = 'велосипед'
# del a

# ***************************************************************************************

import shelve
from datetime import datetime
from settings import FILENAME

"""
db = {
    '45372': {
        'title:': 'Apple Iphone 13'
        'price:': 98000,
        'description': 'Very good phone',
        'created_ad': '23.08.22 18:54'
    }
}
"""


def create():
    """
    This function create new product in DataBase
    """
    id_ = datetime.now().strftime('%H%M%S')
    title = input('  --->  Введите название товара: ')
    price = int(input('  --->  Введите стоимость товара: '))
    description = input('  --->  Введите описание товара: ')
    created_at = datetime.now().strftime('%d.%m.%y %H:%M')
    with shelve.open(FILENAME) as db:
        db[id_] = {
            'title': title,
            'price': price,
            'description': description,
            'created_at': created_at
        }
    print(f'  --->  Товар {title} ({id_}) успешно добавлен!')

def delete_data():
    """
    This function removes any product by ID from the DataBase
    """
    with shelve.open(FILENAME) as db:
        print("""
          --->  Список доступных ID для удаления:""", list(db.keys()))
        id_ = input('  --->  Введите ID товара: ')
        try:
            delete_el = db.pop(id_)
            title = delete_el['title']
            print(f'  --->  Товар {title} ({id_}) успешно удален!')
        except KeyError:
            print(f'  --->  Указанный ID ({id_}) не существует')

def clear_data():
    """
    This function completely clears the DataBase
    """
    with shelve.open(FILENAME) as db:
        db.clear()
        print('-------------------------------------------------------------------------------')
        print(f'  --->  База данных успешно очищена!')
        print('-------------------------------------------------------------------------------')

def get_all_data():
    """
    This function prints a summary of all products in the DataBase.
    """
    with shelve.open(FILENAME) as db:
        for key, value in db.items():
            print('-------------------------------------------------------------------------------')
            print('ID:', key, '|', 'Наименование:', value['title'], '|', 'Цена:', value['price'])
            print('-------------------------------------------------------------------------------')

def retrieve_prod():
    """
    This function prints full description of the product for the given ID.
    """
    with shelve.open(FILENAME) as db:
        print("""
          --->  Список доступных ID:""", list(db.keys()))
        id_ = input('  --->  Введите ID товара, который Вам интересен: ')
        for key, value in db.items():
            if key == id_:
                print('-------------------------------------------------------------------------------')
                print('ID:', id_, '|', 'Наименование:', value['title'], '|', 'Описание:', value['description'], '|', 'Цена:', value['price'], '|', 'Создано:', value['created_at'])
                print('-------------------------------------------------------------------------------')

def update_data():
    """
    This function updates the data in the DataBase by ID.
    """
    with shelve.open(FILENAME, writeback=True) as db:
        print("""
          --->  Список доступных ID:""", list(db.keys()))
        id_ = input('  --->  Введите ID товара: ')
        try:
            prod = db[id_]
            prod['title'] = input('  --->  Введите новое название ') or prod['title']
            prod = db[id_]
            prod['price'] = input('  --->  Введите новую стоимость ') or prod['price']
            prod = db[id_]
            prod['description'] = input('  --->  Введите новое описание ') or prod['description']
        except KeyError:
            print(f'  --->  Указанный ID: {id_} не существует')
    print(f'  --->  Товар ({id_}) успешно обновлен!')

print("""                     
                            Добро пожаловать в Makers Store
                        Введите операцию, которую хотите совершить:""")

while True:
    operation = input("""
            1. create   - создать новый продукт
            2. delete   - удалить продукт по id
            3. list     - получить список всех продуктов
            4. retrieve - получить продукт по id
            5. clear    - очистить базу данных
            6. update   - изменить данные
            7. exit     - выйти из программы 
            
            Введите операцию: """)
    if operation == 'exit':
        print("""
                       ---> До свидания! С уважением Makers Store. <---""")
        break
    if operation == 'create':
        create()
    elif operation == 'list':
        get_all_data()
    elif operation == 'delete':
        delete_data()
    elif operation == 'retrieve':
        retrieve_prod()
    elif operation == 'clear':
        clear_data()
    elif operation == 'update':
        update_data()
    else:
        print('Вы выбрали неверное действие! Попробуйте еще раз или нажмите exit для выхода')