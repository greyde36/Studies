def salary (hours_month,hard_day,milk_day,zona_hours):
    part_month=156.36*int(hours_month)
    hard_work=75.76*int(hard_day)
    milk=39.03*int(milk_day)
    premia=int(part_month)*0.3
    zona=122.77*int(zona_hours)
    gryz=94.31*hours_month
    gryz_zona=28.29*hours_month
    cash=part_month+hard_work+milk+premia+zona+gryz+gryz_zona
    return print('Зарплата с НДС:',int(cash),'рублей\n'
                 'Зарплата без НДС:',int(cash*0.87),'рублей')
salary(162,15,15,162)
salary(input('Введите количество рабочих часов за месяц: '),
       input('Введите количество тяжелых дней: '),
       input('Введите количество дней компенсации молока: '),
       input('Введите количество часов зональной надбавки: '))