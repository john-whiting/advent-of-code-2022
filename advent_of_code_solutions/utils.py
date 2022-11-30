
import json
import os
import requests

current_directory = os.path.dirname(os.path.abspath(__file__))

def get_config():
    with open(os.path.join(current_directory, "../config.json"), 'r') as config_file:
        return json.loads(config_file.read())

def get_input_file(year: int, day: int) -> str:
    config = get_config()
    cookies = {'session': config["AdventOfCode"]["Settings"]["SessionToken"]}
    input_request = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies=cookies)
    return input_request.content.decode("UTF-8")