class WifiEnabled:

  def connect_wifi(self):
    print("Connecting to WiFi...")

class BatteryPowered:

  def check_battery(self):
    print("Battery level is sufficient.")

class SmartSpeaker(WifiEnabled, BatteryPowered):

  def play_music(self):
    print("Playing music...")

speaker= SmartSpeaker()

speaker.connect_wifi()
speaker.check_battery()
speaker.play_music()

# MRO: Method Resolution Order