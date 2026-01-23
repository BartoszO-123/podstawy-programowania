class Phone:
    def __init__(self, model, battery, storage):
        self.model = model
        self.battery = battery
        self.storage = storage
        self.is_locked = True

    def unlock(self):
        self.is_locked = False
        print(f'{self.model} unlocked.')

    def download_file(self, size):
        self.storage -= size
        print(f'File downloaded, remaning storage: {self.storage}GB')

    def charge(self):
        self.battery = 100
        print(f'Phone charged to {self.battery}%')

my_phone = Phone('Xiaomi Redmi Note 5', 50, 10.0)

my_phone.unlock()
my_phone.download_file(0.2)
my_phone.charge()

print(f'\n{my_phone.model}\nBattery: {my_phone.battery}%\nAvaliable storage: {my_phone.storage}GB\n')
