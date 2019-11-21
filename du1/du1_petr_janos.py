import math

R = int(6371.11)


# Výpočet poledníků:
def poledniky():
    poledniky_list = []
    # poledníky v rozsahu -180 až po 180, po 10
    xx = range(-180, 190, 10)
    for poledniky_deg in xx:
        poledniky_x = round(R * (math.radians(poledniky_deg)) * 100000 / meritko, 1)  # vzorec s přepočtem
        # nesmí být větší jak metr
        if poledniky_x > 100 or poledniky_x < - 100:
            poledniky_list.append('-')
        else:
            poledniky_list.append(poledniky_x)
    # vypíše konečný seznam s poledníky
    print('Poledníky: ')
    print(poledniky_list)

# Výpočet rovnoběžek:
def rovnobezky():
    rovnobezky_list = []
    # rovnoběžky v rozsahu -90 až 90
    xx = range(-90, 100, 10)
    for rovnobezky_deg in xx:
        # výběr vzorce dle zvoleného zobrazení
        if zobrazeni_vyber == 'L':
            rovnobezky_y = round(R * (math.sin(math.radians(rovnobezky_deg))) * 100000 / meritko, 1)
        elif zobrazeni_vyber == 'A':
            rovnobezky_y = round(R * (math.radians(rovnobezky_deg)) * 100000 / meritko, 1)
        elif zobrazeni_vyber == 'B':
            rovnobezky_y = round((2 * R) * math.tan(((math.radians(rovnobezky_deg)) / 2)) * 100000 / meritko, 1)
        elif zobrazeni_vyber == 'M':
            # dělit nulou nelze
            if rovnobezky_deg == 90:
                break
            else:
                rovnobezky_y = round(R * math.log(1 / math.tan(math.radians((90 - rovnobezky_deg) / 2)))
                                     * 100000 / meritko, 1)
        else:
            quit()
        # nesmí být větší jak metr
        if rovnobezky_y > 100 or rovnobezky_y < - 100:
            rovnobezky_list.append('-')
        else:
            rovnobezky_list.append(rovnobezky_y)
    # vypíše konečný seznam s rovnoběžkami
    print('Rovnoběžky: ')
    print(rovnobezky_list)


# UŽIVATELSKÉ VSTUPY:
# zobrazení musí být z nabídky, jinak upozorní a znovu se ptá
while True:
    zobrazeni_vyber = input('Zadejte zobrazení (L/A/B/M): ').upper()
    if zobrazeni_vyber == 'L' or zobrazeni_vyber == 'A' or zobrazeni_vyber == 'B' or zobrazeni_vyber == 'M':
        break
    else:
        print('Musíte použít zobrazení z nabídky!')

# měřítko musí být větší jak 0, jinak upozorní a znovu ptá
while True:
    meritko = int(input('Zadejte měřítko:  '))
    if meritko == 0 or meritko < 0:
        print('Měřítko musí být větší jak 0.')
    else:
        break

rovnobezky()
poledniky()
