def salary (hours_month,hard_day,milk_day,zona_hours):
    part_month=156.36*hours_month
    hard_work=75.77*hard_day
    milk=39.03*milk_day
    premia=part_month*0.3
    zona=122.77*zona_hours
    gryz=94.31*hours_month
    gryz_zona=28.29*hours_month
    cash_NDS=part_month+hard_work+milk+premia+zona+gryz+gryz_zona
    cash_no_NDS =((cash_NDS)*0.87)*0.7
    return print('Зарплата с НДС:',round(cash_NDS,2),'рублей\n'
                 'Зарплата без НДС:',round(cash_no_NDS,2),'рублей')
salary(162,15,15,162)