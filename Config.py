import json
import logging

logging.basicConfig(level=logging.INFO)
def config():
    with open('.\config.json', 'r') as f:
        config = json.load(f)
    f.close()
    return config

