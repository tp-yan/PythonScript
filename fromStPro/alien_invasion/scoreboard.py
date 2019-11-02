import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
	'''显示得分信息的类'''
	
	def __init__(self,ai_settings,screen,stats):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		
		self.font = pygame.font.SysFont(None,48)
		self.txt_color = (30,30,30)

		self.prep_imgs()
	
	def prep_imgs(self):
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()
		
	def prep_score(self):
		#将得分转换为图像
		#round让小数精确到指定位数，若是负数指定为10的多少次方倍，
		#在2.x中round返回的总是小数  -1:即将数圆整到10的倍数
		rounded_score = round(self.stats.score,-1)
		#格式化字符串：在 数字-->字符串 过程中插入逗号
		score_str = "{:,}".format(rounded_score)
		#score_str = str(self.stats.score)
		self.score_img = self.font.render(score_str,True,self.txt_color
			,self.ai_settings.bg_color)
		
		#将得分放在屏幕右上角
		self.score_rect = self.score_img.get_rect()
		self.score_rect.right = self.screen_rect.right-20
		self.score_rect.top = 20
		
	def prep_high_score(self):
		high_score = int(round(self.stats.high_score,-1))
		high_score_str = "{:,}".format(high_score)
		self.high_score_img = self.font.render(high_score_str,True,
			self.txt_color,self.ai_settings.bg_color)
		#最高分放在屏幕中央
		self.high_score_rect = self.high_score_img.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.screen_rect.top
		
	def prep_level(self):
		'''将当前等级转换为图像'''
		self.level_img = self.font.render(str(self.stats.level),True
			,self.txt_color,self.ai_settings.bg_color)
		#将等级放在当前得分下面
		self.level_img_rect = self.level_img.get_rect()
		self.level_img_rect.right = self.score_rect.right
		self.level_img_rect.top = self.score_rect.bottom + 10
		
	def prep_ships(self):
		'''显示剩下的飞船'''
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings,self.screen)
			ship.rect.x = 10 + ship_number*ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
	
	def show_score(self):
		self.screen.blit(self.score_img,self.score_rect)
		self.screen.blit(self.high_score_img,self.high_score_rect)
		self.screen.blit(self.level_img,self.level_img_rect)
		#绘制飞船
		self.ships.draw(self.screen)
