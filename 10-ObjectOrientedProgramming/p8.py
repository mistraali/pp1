"""
Identify at least 3 states and 3 behaviors for a telephone object. 
Then, for the listed states and behaviors, create a class with fields (attributes) and methods. 
Try to use verbs in method names as they describe activities. 
Finally, create a object, call its methods and display object’s properties.
"""

class Phone():
    def __init__(self,number,manufacturer,model):
        self.number = number
        self.manufacturer = manufacturer
        self.model = model
        self.is_on = False
    def turn_on_off(self):
        self.is_on = not(self.is_on)
        print("Device is", "ON" if self.is_on else "OFF")
    def make_a_call(self,number):
        if self.is_on:
            print(f"Calling {number}!")
            ...
        else:
            print("Unable to make a call. Device is off.")
    def send_a_text(self,text,number):
        if self.is_on:
            print(f"Sending \"{text}\" to {number}!")
            ...
        else:
            print("Unable to send a text. Device is off.")

my_phone = Phone(111222333,"Xiaomi","Redmi 10")

my_phone.turn_on_off()
my_phone.send_a_text("call me asap",222333444)
my_phone.turn_on_off()
my_phone.make_a_call(222333555)

    
