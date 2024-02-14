import csv

with open('space.txt', encoding = 'utf8') as f:
    reader = list(csv.DictReader(f, delimiter = '*', quotechar = '"'))

    request = input()
    while request != 'stop':
        for el in reader:
            if el['ShipName'] == request:
                pan = el['planet']
                directions = el['direction']
                print(f'Корабль {request} был отправлен с планеты: {pan} и его направление движения было: {directions}')
                break
        else:
            print('error.. er.. ror..')
