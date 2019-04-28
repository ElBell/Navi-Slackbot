import bot
import requests
import json
from simplegist.simplegist import Simplegist

bot.Bot()
#
# print(gist.profile().listall())
#
# for i in range(10):
#     print(requests.get("https://api.github.com/users/ElBell/gists").text)
#     response = json.loads(requests.get("https://api.github.com/users/ElBell/gists").text)
#     for gistfound in response:
#         for key in gistfound['files'].keys():
#             if 'testingbot' in key:
#                 gist.profile().delete(id=gistfound["id"])
#
