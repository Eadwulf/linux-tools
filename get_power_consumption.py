import os


def get_file_value(filepath):
    with open(filepath) as file:
        value = int(file.readline().strip('\n'))
    return value/1000000


def get_power():
    current = get_file_value('/sys/class/power_supply/BAT1/current_now')
    voltage = get_file_value('/sys/class/power_supply/BAT1/voltage_now')
    return (current*voltage)


if __name__ == '__main__':
    print(f'{get_power():.4f} Watts')
