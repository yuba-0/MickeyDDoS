import json
import random


# Get random IP
def random_IP():
    ip = []
    for _ in range(0, 4):
        ip.append(str(random.randint(1, 255)))
    return ".".join(ip)


# Get random referer
def random_referer():
    with open("tools/1c1a5da287e29e2408f3d72b71926361/referers.txt", "r") as referers:
        referers = referers.readlines()
    return random.choice(referers)


# Get random user agent
def random_useragent():
    with open("tools/1c1a5da287e29e2408f3d72b71926361/user_agents.json", "r") as agents:
        user_agents = json.load(agents)["agents"]
    return random.choice(user_agents)
