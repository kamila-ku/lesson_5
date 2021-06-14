my_file = open('task_1.txt', 'w')
while True:
    string = input("Введите строку ")
    if string == '': break
    my_file.write(string + '\n')
my_file.close()