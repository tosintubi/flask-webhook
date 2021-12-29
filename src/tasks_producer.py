
import random
import time
import requests
import json
import uuid

from faker import Faker
from faker.providers import BaseProvider

from src.config import config


# Definde TaskProvider
class TaskProvider(BaseProvider):

    def task_priority(self):
        severity_levels =[
            'LOW', 'MODERATE', 'MAJOR', 'CRITICAL'
        ]
        return severity_levels[random.randint(0, len(severity_levels)-1)]

#Create a Faker instance and seedint o have same results every time we execure the return data in english
fake_tasks = Faker('en_US')

#Seeding the fake task so its reproducible
fake_tasks.seed_instance(25)

fake_tasks.add_provider(TaskProvider)


# Generate a fake task
def produce_task(batch_id, task_id):
    # Compose Message fake task
    message = {
        'batch_id':batch_id,
        'id': task_id,
        'owner':fake_tasks.unique.name(),
        'priority': fake_tasks.task_priority()
    }
    return message


def send_webhook(msg):
    """Sends a webhook to the specified URL

    Args:
        msg ([type]): Task details
    """

    try:
        # Post webhook Message
        response = requests.post(
            config.WEBHOOK_RECEIVER_URL, 
            data=json.dumps(
                obj=msg,
                sort_keys=True,
                default=str)
            ,headers={'Content-Type':'application/json'},
            timeout=1.0)
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print(f"An HTTP error occured: {error.message}")
    except requests.exceptions.ConnectionError as error:
         print(f"A Connection error occured: {error.message}")
    except requests.exceptions.Timeout as error:
        print(f"A Timeout error occured: {error.message}")
    except requests.exceptions.RequestException as error:
         print(f"An Unknown error occured: {error.message}")
    else:
        return response.status_code
