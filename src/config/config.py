import os


# Secret key to be used to securely sign the session
SECRET_KEY = os.environ.get('SECRET_KEY')

# Min number of tasks to generate
MIN_NBR_TASKS = 1

# Max number of tasks to generate
MAX_NBR_TASKS = 100

# Time to wait when producing tasks
WAIT_TIME = 1

# Webhook endpoint mapping to the listener
WEBHOOK_RECEIVER_URL = os.environ.get('WEBHOOK_RECEIVER_URL')

# Map to REDIS server port
BROKER_URL = os.environ.get('BROKER_URL')
