"""
    Stwórz funkcję, która przelicza temperaturę w stopniach Celsjusza na Fahrenheit, Rankine, Kelvin.
    Typ konwersji powinien być przekazany w parametrze temperature_type i uwzględniać błędne wartości.
"""


def konwersja(temperature, temperature_type):
    temperatura = float(temperature)

    kelvin = temperatura - 273.15
    fahrenheit = ((9 / 5) * temperatura) + 32
    rankine = fahrenheit + 459, 67

    if temperature_type == 'F':
        return fahrenheit
    elif temperature_type == 'R':
        return rankine
    elif temperature_type == 'K':
        return kelvin


celsjusz = float(input("Podaj temperaturę w stopniach Celsjusza: "))
print("Fahrenheit - F | Rankine - R | Kelvin - K")

typSkali = str()
while typSkali != 'F' or typSkali != 'R' or typSkali != 'K':
    typSkali = input("Podaj na jaką skalę chcesz przeliczyć temteraturę (F | R | K): ")

print(konwersja(celsjusz, typSkali))
