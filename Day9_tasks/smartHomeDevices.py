'''
Smart Home Devices (Multiple Inheritance)
A smart home device may have both WiFi connectivity and Voice control features.
Create classes WiFiDevice and VoiceAssistant, and a class SmartSpeaker that
inherits from both using multiple inheritance
'''
class WiFiDevice:
    def connect_wifi(self):
        print("Wifi Connected")
        
class VoiceAssistant:
    def activate_VoiceAsst(self):
        print("Voice Assistant Activated")
    def give_command(self,command):
        print(f"Executing Command:{command}")
        
class SmartSpeaker(WiFiDevice,VoiceAssistant):
    def Music(self):
        print("Playing Music...")
        
sp=SmartSpeaker()
sp.connect_wifi()
sp.activate_VoiceAsst()
sp.give_command("Play music")
sp.Music()


