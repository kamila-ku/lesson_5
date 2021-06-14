my_file = "task_6_text.txt"
if __name__ == "__main__":
    subjects = {}
    try:
        with open(my_file, encoding='utf-8') as fh:
            lines = fh.readlines()

        for line in lines:
            data = line.replace('(', ' ').split()

            subjects[data[0][:-1]] = sum(
                int(i) for i in data if i.isdigit()
            )
    except IOError as e:
        print(e)
    except ValueError:
        print("Неконсистентные данные")
    print(subjects)