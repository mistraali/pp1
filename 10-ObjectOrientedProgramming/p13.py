class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1

    def turn_on(self):
        if not(self.is_on):
            self.is_on = True
            #print("TV is now ON")
    
    def turn_off(self):
        if self.is_on:
            self.is_on = False
            #print("TV is now OFF")
    
    def show_status(self):
        print("TV is", f"on, channel {self.channel_no}" if self.is_on else "off")

    def new_channel(self, new_no):
        self.channel_no = new_no

my_tv = TV()
my_tv.show_status()
my_tv.turn_on()
my_tv.show_status()
my_tv.new_channel(5)
my_tv.show_status()
my_tv.turn_off()
my_tv.show_status()      