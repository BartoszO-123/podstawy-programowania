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

    my_tv.increase_volume()
    my_tv.increase_volume()
    print('\nVolume increased 2 times')
    
    print('Show TV status:')
    my_tv.show_status()
    
    for _ in range(12): 
        my_tv.increase_volume()
    print("Cannot increase volume over 10.")
    my_tv.show_status()    
    
    print()

    my_tv.decrease_volume()
    print('Volume decreased 1 times')
    
    my_tv.show_status()
    
    my_tv.turn_off()
    my_tv.show_status()
    
if __name__ == '__main__':
    main()
    