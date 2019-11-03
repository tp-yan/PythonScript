import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	'''单个外星人类'''
	
	def __init__(self,ai_settings,screen):
		'''初始化外星人并设置其初始值'''
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		#加载外星人图像，并设置其rect属性
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		#每个外星人都在屏幕左上角
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		#存储外星人准确的位置
		self.x = float(self.rect.x)
		#移动方向
		self.direction = 1
		
	def blitme(self):
		'''在指定位置绘制外星人'''
		self.screen.blit(self.image,self.rect)
		
	def update(self):
		'''向右移外星人'''
		if self.x < self.ai_settings.screen_width:
			self.x += (self.ai_settings.alien_speed_factor*
						self.direction)
			self.rect.x = self.x

	def check_edges(self):
		'''外星人是否碰到屏幕边缘'''
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		if self.rect.left <= 0:
			return True
	
	def change_direction(self):
		'''碰到边时，改变方向并下降一定距离'''
		self.direction *= -1
		self.rect.y += self.ai_settings.alien_drop_speed
		
