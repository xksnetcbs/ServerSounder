import json
import time
from mcdreforged.api.all import *
import re
import os
import random
import MinecraftDataAPI
from playsound import playsound
'''
服务器坐标共享
'''

PLUGIN_METADATA = {
    'id': 'Playsound',
    'version': '1.3.7',
    'name': 'A Easy Minecraft Sweeper',
    'author': [
        'DC_Provide'
    ],
    'link': 'Nope...[doge]'
}
@new_thread(PLUGIN_METADATA['name'])

def on_player_joined(server,player,info):
    playsound('./plugins/sound/pj.mp3')
def on_player_left(server,info):
    playsound('./plugins/sound/pe.mp3')
def on_info(server,info):
    if info.is_user:
        playsound('./plugins/sound/info.mp3')
