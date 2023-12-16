class TV():
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        if not(self.is_on):
            self.is_on = True
            #print("TV is now ON")
    
    def turn_off(self):
        if self.is_on:
            self.is_on = False
            #print("TV is now OFF")
    
    def show_status(self):
        print("TV is", "on" if self.is_on else "off")

my_tv = TV()
my_tv.show_status()
my_tv.turn_on()
my_tv.show_status()
my_tv.turn_off()
my_tv.show_status()        