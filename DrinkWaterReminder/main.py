import time
from plyer import notification
while True:
    notification.notify(
        title="Drink Water Reminder",
        message="Please sip some water to stay hydrated!",
        timeout=10  # Notification stays for 10 seconds
    )
    time.sleep(3600)  # Wait for 1 hour before sending the next notification