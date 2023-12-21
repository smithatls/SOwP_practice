# Эта программа усредняет оценки в расчете на одного студента
students = int(input('Сколько у вас студентов? '))
test_scores = int(input('Сколько оценок должно быть в расчете на одного студента? '))
for student in range(students): # Пока студентов будет до students цикл выполняется! Несмотря на то что отсчет идёт
    # до последнего студента т.к. мы начинаем не с 1, а с 0
    total = 0  # Накопитель оценок

    print(f'Студент номер {student + 1}')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')

    for test in range(test_scores): # внутрненний цикл, принцип работы аналогичен внешнему
        print(f'Лабораторная работа номер {test + 1}', end='')
        score = float(input(': '))

        total += score

    average = total / test_scores

    print(f'Средний бал студента номер {student + 1}\n'
          f'Составляет {average: .1f}')
    print()