class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels_list = []

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

    def set_channels(self, channels_list):
        self.channels_list = channels_list.copy()
    
    def show_channels(self):
        if len(self.channels_list) != 0:
            for i in range(len(self.channels_list)):
                print(f"{i+1}. {self.channels_list[i]}")
        else:
            print("No channels were set.")

my_tv = TV()
my_tv.show_status()
my_tv.turn_on()
my_tv.show_status
my_tv.show_channels()
my_tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
my_tv.show_channels()
my_tv.turn_off()
my_tv.show_status()        