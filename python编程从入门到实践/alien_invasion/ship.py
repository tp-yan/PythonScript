import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self,ai_settings,screen):
		'''初始化飞船并设置其初始位置'''
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		#加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#将每艘新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#用于保存小数值的坐标，因为rect属性只能保存整数
		self.center_x = float(self.rect.centerx)
		
		#移动标志
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		'''根据移动标志调整飞船的位置,并限制在屏幕内'''
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center_x += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center_x -= self.ai_settings.ship_speed_factor
		self.rect.centerx = self.center_x
		
	def blitme(self):
		'''在指定位置绘制飞船'''
		self.screen.blit(self.image,self.rect)
	
	def center_ship(self):
		'''使飞船屏幕居中'''
		self.center_x =  self.screen_rect.centerx
		self.rect.centerx = self.center_x
