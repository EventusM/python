month = int(input('Введите месяц года от 1 до 12: '))
month_start = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель',
               5: 'май', 6: 'июнь', 7: 'июль', 8: 'август',
               9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
month_list = [ 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
               'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
if month in month_start:
    print(f'{month}-й месяц года - это {month_start[month]}')
    print(f'{month}-й месяц года - это {month_list[month - 1]}')
else:
    print('некорректный номер')

