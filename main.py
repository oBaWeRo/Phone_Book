import sqlite3

# Создаем глобальные константы для управления циклом.
UC_MIN = 1
UC_MAX = 6
EXIT = 6
class PhoneBook: # Создаем класс который работает с базой данных
  def __init__(self):

    with sqlite3.connect('phonebook.db') as self.__conn:
      self.__cur = self.__conn.cursor()
      self.__cur.execute('''CREATE TABLE IF NOT EXISTS Entries (PhoneID INTEGER PRIMARY KEY NOT NULL,
  Name TEXT,
  PhoneNumber TEXT)''')
      self.__user_choice = 0

      while self.__user_choice != EXIT: # Данный цикл будет продолжаться до тех пор пока
        # пользователь не захочет выйти.
        self.__show_menu()
        self.__user_choice = int (input('Введите пункт меню: ')) #Данный атрибут данных
        # управляет циклом получая выбранный вариант от пользователя.
        print()

        if self.__user_choice == 1:
          name = input('Введите имя для привязки номера: ')
          phone = int (input('Введите номер телефона без пробелов: '))

          self.__cur.execute(''' Insert Into Entries (Name,PhoneNumber)
          Values (?,?)''',
                      (name,phone))
          print('Данные успешно добавлены.')
          print()

        if self.__user_choice == 2:
          phone = int (input('Введите номер телефона: '))
          self.__cur.execute('''  Select * From Entries Where PhoneNumber == ? ''',
                      (phone,))

          results = self.__cur.fetchall()
          for row in results:
            print(f'Результаты поиска: {row[0]} {row[1]} {row[2]}')
          print()

        if self.__user_choice == 3:
          name = input('Введите имя к которому привязан номер: ')
          phone = int (input('Ведите новый номер телефона: '))

          self.__cur.execute(''' Update Entries Set PhoneNumber = ? Where Name == ? ''',
                      (phone,name))

          results = self.__cur.rowcount
          if results > 0:
            print('Изменения успешно сохранены.')

          else:
            print('Такого имени не существует.')
          print()

        if self.__user_choice == 4:
          name = input('Введите имя к которому привязан номер: ')
          self.__cur.execute(''' Select PhoneNumber From Entries Where Name == ? ''',
                      (name,))
          results = self.__cur.fetchone()

          if results != None:
            print(f'Проверьте номер: {results[0]}')
            choice = input('Вы действительно хотите удалить этот номер (д\н): ')
            if choice.lower() == 'д':
              self.__cur.execute(''' Delete From Entries Where Name == ?''',
                          (name,))
              print('Данные успешно удалены.')

          else:
            print(f'Такого имени {name} не существует.')

        if self.__user_choice == 5:
          self.__show_all_numbers()

        if self.__user_choice < UC_MIN or self.__user_choice > UC_MAX:
          print('Введите пункт меню от 1 до 6.')
          print()

  def __show_menu(self): # Создаем меню.
    print()
    print('Добро пожаловать в программу "PHONEBOOK V.1.0"')
    print('1. Добавить новый номер')
    print('2. Найти человека по номеру телефона')
    print('3. Изменить номер телефона')
    print('4. Удалить номер телефона')
    print('5. Показать все номера телефонов')
    print('6. Выйти из программы')
    print()

  def __show_all_numbers(self):
    self.__cur.execute(''' Select * From Entries ''')
    results = self.__cur.fetchall()

    for row in results:
      print(f'ID: {row[0]} Имя пользователя: {row[1]} Номер телефона: {row[2]}')

# Создаем точку входа.
if __name__ == '__main__':
  phonebook = PhoneBook()