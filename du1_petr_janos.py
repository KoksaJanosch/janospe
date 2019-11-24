import math


# Výpočet poledníků:
def poledniky(R, meritko):
    poledniky_list = []
    # poledníky v rozsahu -180 až po 180, po 10
    for poledniky_deg in range(-180, 190, 10):
        poledniky_x = round(R * (math.radians(poledniky_deg)) * 100000 / meritko, 1)  # vzorec s přepočtem
        # nesmí být větší jak metr
        if poledniky_x > 100 or poledniky_x < - 100:
            poledniky_list.append('-')
        else:
            poledniky_list.append(poledniky_x)
    # vrátí konečný seznam s poledníky
    return(poledniky_list)


# Výpočet rovnoběžek:
def rovnobezky(R, meritko):
    rovnobezky_list = []
    # rovnoběžky v rozsahu -90 až 90
    for rovnobezky_deg in range(-90, 100, 10):
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
                rovnobezky_list.append('-')
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
    # vrátí konečný seznam s rovnoběžkami
    return (rovnobezky_list)


# UŽIVATELSKÉ VSTUPY:

# Výběr zobrazení: musí být z nabídky, jinak upozorní a znovu se ptá
while True:
    zobrazeni_vyber = input('Zadejte zobrazení (L/A/B/M): ').upper()
    if zobrazeni_vyber == 'L' or zobrazeni_vyber == 'A' or zobrazeni_vyber == 'B' or zobrazeni_vyber == 'M':
        break
    else:
        print('Musíte použít zobrazení z nabídky!')

# Zvolení měřítka: musí být větší jak 0, jinak upozorní a znovu ptá
while True:
    meritko = int(input('Zadejte měřítko:  '))
    if meritko == 0 or meritko < 0:
        print('Měřítko musí být větší jak 0.')
    else:
        break

# Zvolení poloměru: musí být kladný, pro Zemi zadat 0
while True:
    R = float(input('Zadejte poloměr (pro Zemi zadejte nulu): '))
    if R == 0:
        R = float(6371.11)
        break
    elif R < 0:
        print('Poloměr musí být kladný.')
    else:
        break

rovnobezky_seznam = rovnobezky(R, meritko)
poledniky_seznam = poledniky(R, meritko)

print('Rovnoběžky: ', rovnobezky_seznam)
print('Poledníky: ', poledniky_seznam)
