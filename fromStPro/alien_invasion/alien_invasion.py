import sys
import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	#创建Play按钮
	play_button = Button(ai_settings,screen,"Play")
	
	#创建一艘飞船
	ship = Ship(ai_settings,screen)
	#创建用于存储子弹的编组,Group类 类似于列表
	bullets = Group()
	aliens = Group()
	#创建一个外星人
	#alien = Alien(ai_settings,screen)
	#创建一群外星人
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	#游戏统计信息实例
	stats = GameStats(ai_settings)
	gf.get_high_score(stats)
	score = Scoreboard(ai_settings,screen,stats)
	
	#开始游戏的主循环
	while True:
		#监视键盘与鼠标事件
		gf.check_events(ai_settings,screen,ship,aliens,bullets
			,play_button,stats,score)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,ship,aliens,bullets
				,stats,score)
			gf.update_aliens(ai_settings,stats,screen,bullets,aliens
				,ship,score)
		
		#每次循环时都重新绘制屏幕
		gf.update_screen(ai_settings,screen,ship,aliens,bullets,stats
			,play_button,score)
		
run_game()
