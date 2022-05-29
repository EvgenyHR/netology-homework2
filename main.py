HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя)
show - напечатать все добавленные задачи."""
today = []
tomorrow = []
other = []
while True:
  command = input("Введите команду:")
  if command == "help":
    print(HELP)
  elif command == "show":
    print(today) 
    sep = print(tomorrow) 
    sep = print(other)
  elif command == "add":
    date = input("Введите дату:")
    if date == "сегодня":
      task1 = input("Введите задачу:")
      today.append(task1)
    elif date == "завтра":
      task2 = input("Введите задачу:")
      tomorrow.append(task2)
    else:
      task3 = input("Введите задачу:")
      other.append(task3)
    print("Задача добавлена")
  elif command == "exit":
    print("Спасибо за использование! До свидания!")
  else:
    print("Неизвестная команда")