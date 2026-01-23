# tv_show.py file
# main program
from tv import TV

def main():
    # object creation
    print('Create TV set')
    my_tv = TV()

    print('Show TV status')
    my_tv.show_status()

    print('Turn TV on')
    my_tv.turn_on()

    print('Show TV status')
    my_tv.show_status()

    print('Change TV channel to 5')
    my_tv.set_channel(5)

    print('Show TV status')
    my_tv.show_status()

    print('Turn TV off')
    my_tv.turn_off()

    print('Show TV status')
    my_tv.show_status()

if __name__ == "__main__":
    main()
    