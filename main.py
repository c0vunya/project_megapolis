import csv

with open('space.txt', encoding = 'utf8') as f:
    answer = list(csv.reader(f, delimiter = '*'))[1:]

    n_word = {}
    m_word = {}
    t_word = {}
    x_word = {}
    y_word = {}

    for ShipName, planet, coord_place, direction in answer:
        coord_x, coord_y = direction.split()
        n_word[ShipName] = ShipName[-3]
        m_word[ShipName] = ShipName[-2]
        t_word[ShipName] = len(planet)
        x_word[ShipName] = coord_x
        y_word[ShipName] = coord_y

    for el in answer:
        xx, yy = el[-2].split()
        if int(xx) == 0 or int(yy) == 0:
            if int(n_word[el[0]]) > 5:
                xx = int(n_word[el[0]]) + int(x_word[el[0]])
            else:
                xx = t_word[el[0]] - 4 * (int(n_word[el[0]]) + int(x_word[el[0]]))

            if int(m_word[el[0]]) > 3:
                yy = int(m_word[el[0]]) + t_word[el[0]] + int(y_word[el[0]])
            else:
                yy = -1 * int(m_word[el[0]]) * (int(n_word[el[0]]) + int(y_word[el[0]]))
            el[-2] = str(xx) + str(' ') + str(yy)

with open('space_new.txt', 'w', encoding = 'utf8', newline = '') as f:
    writer = csv.writer(f, delimiter = '*')
    writer.writerow(['ShipName','planet','coord_place','direction'])
    writer.writerows(answer)

with open('space_new.txt', encoding = 'utf8') as file:
    answer1 = list(csv.reader(file, delimiter='*'))[1:]
    for el in answer1:
        level = el[0]
        if 'V' in level[3]:
            x, y = el[-2].split()
            print(f'{el[0]} - ({int(x)}, {int(y)})')
