

molar_conc = float(input("Введите молярную концентрацию: "))
volume = float(input("Введите объём: "))
molar_mass = float(input("Введите молярную массу в единицах гр/моль: "))
mass = molar_conc * volume * molar_mass
print(f' Масса равна  {mass}')

