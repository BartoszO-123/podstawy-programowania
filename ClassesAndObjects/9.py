# Tv.py file
# class definition
class Tv:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        
    def turn_off(self):
        self.is_on = False
        
    def turn_on(self):
        self.is_on = True
        
    def show_status(self):
        if self.is_on:
            print(f'Tv on, channel {self.channel_no}')
        else:
            print('Tv off')
            