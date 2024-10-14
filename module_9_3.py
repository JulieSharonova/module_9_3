first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(k) - len(i) for k, i in zip(first, second) if len(k) != len(i))
second_result = (len(first[j]) == len(second[j]) for j in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))