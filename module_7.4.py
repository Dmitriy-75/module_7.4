# Исходные данные:
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

#Расчеты
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

tasks_total = score_1+score_2
time_avg = round((team1_time+team2_time)/(score_1+score_2), 1)

#Использование %:
print('\nВ команде Мастера кода участников: %s !' % team1_num)
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num)+'\n')

#Использование format():
print('Команда Волшебники данных решила задач {}.'.format(score_2))
print('Волшебники данных решили задачи за {} с.'.format(team2_time)+'\n')

#Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg}  секунды на задачу!')




