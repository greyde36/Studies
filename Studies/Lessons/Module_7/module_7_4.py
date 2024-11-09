team1_num=5
team2_num=6
score_2=42
score_1=40
team1_magic='Волшебники'
team2_master='Мастера'
team1_time=18015.2
# %
print('В команде %s кода участников: %d!' % (team2_master, team1_num))
print('Итого сегодня в командах участников: %d и %d!' % (team1_num,team2_num))
# format
print('Команда {} данных решила задач: {}'.format(team1_magic,score_2))
print('{1} данных решили задачи за {0}'.format(team1_time,team1_magic))
# f''
print(f'Команды решили {score_1} и {score_2} задач')
if score_2>score_1:
    challenge_result = team2_master
else:
    challenge_result = team1_magic
print(f'Результат битвы: победа команды {challenge_result}!')
tasks_total=score_1+score_2
time_avg=team1_time/score_1
print(f'Сегодня было решено {tasks_total}, в среднем по {time_avg} секунды на задачу!')