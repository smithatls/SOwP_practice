import circle
import rectangle

AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5


def main():
    choice = 0

    while choice != QUIT_CHOICE:
        display_menu()

        choice = int(input('Choice variants: '))

        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input('Pribnt radius'))
            print(f'{circle.area(radius)}')


def display_menu():
    print('MENU')
    print('pechataio 1 - 5')


main()
