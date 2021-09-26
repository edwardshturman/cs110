def kinetic_energy(mass, velocity):
    result = ((velocity ** 2) * mass) / 2
    return result


def main():
    mass = float(input('Enter the mass (kg): '))
    velocity = float(input('Enter the velocity (m/s): '))
    result = kinetic_energy(mass, velocity)
    print('The object\'s kinetic energy: ' + format(result, '.2f') + 'kgm^2/s^2')


main()
