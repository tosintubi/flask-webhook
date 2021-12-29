
import random
import time
import requests
import json
import uuid

from faker import Faker
from faker.providers import BaseProvider

import src.config.config


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
