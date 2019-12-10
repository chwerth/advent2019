from math import floor

def calculate_fuel(mass):
    fuel_needed = floor(mass / 3) - 2
    if (fuel_needed <= 0):
        return 0
    return fuel_needed + calculate_fuel(fuel_needed)

fuel_file = open('input.txt', 'r')
mass_list = fuel_file.readlines()
total_fuel = 0
        
for mass in mass_list:
    total_fuel += calculate_fuel(int(mass))

print(total_fuel)
