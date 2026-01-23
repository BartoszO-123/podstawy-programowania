# tv.py file
# class definition
# class TV:
            
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False
        
    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1
            
    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
        
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
        
    def set_channels(self, channels_list):
        self.channels = channels_list
        print('Channels set')
        
    def show_channels(self):
        print('Channel list:')
        if not self.channels:
            print('TV not programmed, no available channels')
        for i in range(len(self.channels)):
            print(f'{i + 1}. {self.channels[i]}')
        
    def show_status(self):
        if self.is_on:
            if 1 <= self.channel_no <= len(self.channels):
                channel_name = self.channels[self.channel_no -1]
                print(f'Tv on, channel {self.channel_no}, {channel_name}, volume: {self.volume}')
            else:
                print(f'tv on, channel {self.channel_no}, volume: {self.volume}')
        else:
            print('Tv off')