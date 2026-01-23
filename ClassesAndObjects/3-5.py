# tv_show.py file
# main program
from tv import TV

def main():
    # object creation
    print('Create TV set')
    my_tv = TV()

    my_tv.turn_on()
    
    print('Show TV status:')
    my_tv.show_status()

    channels = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "TVN Turbo"]
    my_tv.set_channels(channels)

    my_tv.show_status()

    my_tv.set_channel(2)
    my_tv.show_status()

    my_tv.set_channel(4)
    my_tv.show_status()

    my_tv.set_channel(7)
    my_tv.show_status()

    my_tv.set_channel(10)
    my_tv.show_status()

    my_tv.turn_off()
    my_tv.show_status()
    
if __name__ == '__main__':
    main()
    