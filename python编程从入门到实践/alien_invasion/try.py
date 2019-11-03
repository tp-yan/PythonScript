import sys

import pygame

from settings import Settings
from my_role import MyRole
from pygame.sprite import Group

import game_functions as gf
 
def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Try it!")
	
	my_role = MyRole(screen)
	bullets = Group()
	
	while True:
		gf.check_events2(ai_settings,screen,my_role,bullets)
		my_role.update()
		gf.update_bullets2(bullets,screen.get_rect())
		
		gf.update_screen(ai_settings,screen,my_role,bullets)

run_game()
