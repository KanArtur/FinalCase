from flask import Flask
import os
import json
import requests


app = Flask("server")
DEFAULT_CONFIG = {"port": 5555, "debug": True}

__dir__ = os.path.abspath(os.path.dirname(__file__))
data_dir = f"{__dir__}/data"
if not os.path.isdir(data_dir):
    os.mkdir(data_dir)


def read_config():
    home_dir = os.path.dirname(__file__)
    cfg_file = os.path.join(home_dir, "config.json")
    config = {**DEFAULT_CONFIG}
    try:
        with open(cfg_file) as f:
            data = json.load(f)
        config["port"] = data.get("port", DEFAULT_CONFIG["port"])
        config["debug"] = data.get("debug", DEFAULT_CONFIG["debug"])
    except (FileNotFoundError, json.JSONDecodeError):
        with open(cfg_file, "w") as fp:
            json.dump(DEFAULT_CONFIG, fp)
    return config


r = requests.get('https://dt.miet.ru/ppo_it_final', data={'key': '3uf6s2ym'})