import sys
import pygame

from settings import Settings
import game_functions  as gf
from pygame.sprite import Group
from target_rect import TargetRect
from game_stats import GameStats
from button import Button
from ship import Ship

def run_game():
	pygame.init()
	sys_settings = Settings()
	
	screen = pygame.display.set_mode(
	(sys_settings.screen_width,sys_settings.screen_height))
	screen.fill(sys_settings.bg_color)
	pygame.display.set_caption("Test")
		
	play_button = Button(sys_settings,screen,"Play")
	stars = Group()
	#rains = Group()
	rackets = Group()
	bullets = Group()
	
	target = TargetRect(sys_settings,screen)
	ship = Ship(sys_settings,screen)
	
	gf.create_stars(sys_settings,screen,stars)
	gf.create_rackets(sys_settings,screen,rackets)
	#gf.create_stars(sys_settings,screen,rains)
	stats = GameStats(sys_settings)
	
	while True:
		gf.check_events(stars,rackets,play_button,stats,ship,bullets,sys_settings,screen)
		if stats.game_active:
			gf.update_stars(sys_settings,screen,stars,rackets,stats)
			gf.update_ship(ship)
			gf.update_rackets(rackets)
			gf.update_bullets(bullets,target,stats,sys_settings)
		gf.update_screen(sys_settings,screen,stars,rackets,stats,target
			,play_button,ship,bullets)
		if stats.game_active:
			if len(stars) <= 0:
				gf.create_stars(sys_settings,screen,stars)	
		#gf.update_screen(sys_settings,screen,rains)
		
run_game()
