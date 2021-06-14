num = ('Один', 'Два', 'Три', 'Четыре')
try:
    with open("task_4_text.txt", 'r') as fhs:
        lines = fhs.readlines()
    numbers = [int(line[-2]) for line in lines if line != '\n']
    content = "\n".join(f'{num[n - 1]} - {n}' for n in numbers)
    with open("task_4_new.txt", 'w') as fhd:
        fhd.write(content)
except IOError as e:
    print(e)
except (ValueError, IndexError):
    print("Неконсистентные данные")
