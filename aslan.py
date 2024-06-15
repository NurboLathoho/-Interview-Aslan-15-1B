'''13)Чтение файла и вывод его содержимого:
   Создайте программу, которая открывает текстовый файл и выводит его содержимое на экран.
14) Перезапись файла:
   Напишите программу, которая открывает файл, перезаписывает его содержимое новым текстом и сохраняет изменения.
20)Напишите лямбда-функцию, которая принимает на вход список пар чисел и возвращает список, содержащий суммы каждой пары.'''

# 13)
def num():
    file_name = input("Введите имя файла с текстом: ")

    try:
        with open(file_name, 'r') as file:
            # Читаем содержимое файла
            file_content = file.read()
            print("Содержимое файла:")
            print(file_content)
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except IOError:
        print(f"Ошибка ввода-вывода при работе с файлом '{file_name}'.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

num()

# 14) bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
def numu():
    file_name = input("Введите имя файла для редактирования: ")

    try:
        with open(file_name, 'w') as file:
            new_content = input("Введите новый текст для файла:\n")
            file.write(new_content)
        
        print(f"Файл '{file_name}' успешно обновлен.")
    
    except IOError:
        print(f"Ошибка ввода-вывода при работе с файлом '{file_name}'.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

numu()

  
# 20)32222222222222222222222222222222222222222222222222222222222222
  
num = [(1, 2), (3, 4), (5, 6), (7, 8)]
nums = list(map(lambda x: x[0] + x[1], num))

print(nums)

