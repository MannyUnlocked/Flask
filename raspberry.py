import requests
import time
from gpiozero import Buzzer, Button
import threading

# Define the GPIO pin for the Buzzer
buzzer = Buzzer(4)  # Using GPIO4 for the buzzer

# Define the GPIO pin for the Limit Switch
limit_switch = Button(17, pull_up=True, bounce_time=0.1)  # Example: Using GPIO27 for the limit switch

passenger_present = False
payment_made = False

def beep_buzzer(times, beep_duration=0.1, pause_duration=0.05):
    for _ in range(times):
        buzzer.on()
        print("Buzzer on")
        time.sleep(beep_duration)  # Buzzer beeps for beep_duration seconds
        buzzer.off()
        print("Buzzer off")
        if _ < times - 1:  # Pause between beeps but not after the last beep
            time.sleep(pause_duration)


def switch_actuated():
    print("PASSENGER DETECTED\n")
    passenger_present = True


def monitor_switch():
    if not passenger_present:
        limit_switch.when_pressed = switch_actuated


def check_transaction_status():
    api_endpoint = 'https://flask-wtqv.onrender.com/transaction-stat'
    
    try:
        print("Sending GET request to:", api_endpoint)
        response = requests.get(api_endpoint)
        print("Response status code:", response.status_code)
        
        if response.status_code == 200:
            data = response.json()
            print("Response data:", data)
            beep_buzzer(2)
            payment_made = True
            return True
        else:
            print(f'Request failed with status code: {response.status_code}')



