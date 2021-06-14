my_file = open('task_2_text.txt', 'r', encoding='utf-8')
with open('task_2_text.txt') as f:
    text = f.readlines()
    size = len(text)
my_file = open('task_2_text.txt', 'r')
content = my_file.read()
content = content.split()
i = 1
for string in text:
    print(f"В строке {i} {len(string.split())} слова")
    i += 1
print(f"Общее количество слов - {len(content)}")
print("Количество строк", size)
