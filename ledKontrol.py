from ota_update.main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
    ota_updater = OTAUpdater('https://github.com/erdcan/esp32Blink',main_dir='app', secrets_file="secrets.py")
    ota_updater.download_and_install_update_if_available('arduino', 'pic18f4550')

def start():
    # your custom code goes here. Something like this: ...
    # from main.x import YourProject
    # project = YourProject()
    # ...
    from machine import Pin
    from time import sleep

    led = Pin(2, Pin.OUT)
    while True:
        
        led.value(1)
        sleep(0.5)
        led.value(0)
        sleep(0.5)
    
def boot():
    download_and_install_update_if_available()
    start()


boot()
