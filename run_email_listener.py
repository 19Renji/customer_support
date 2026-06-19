import time

from services.email_listener import (
    process_emails
)

print(
    "Email Listener Started..."
)

while True:

    process_emails()

    time.sleep(
        30
    )