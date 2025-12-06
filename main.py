import warnings
# Suppress pkg_resources deprecation warning from dependencies like pygame
warnings.filterwarnings("ignore", category=UserWarning, message=".*pkg_resources is deprecated.*")

import pygame as pg
from source.main import main

if __name__=='__main__':
    main()
    pg.quit()