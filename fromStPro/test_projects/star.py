import pygame
from random import randint
from pygame.sprite import Sprite

#Sprite:精灵类，继承Sprite的类可被放入Group实例中，即能同时操作编组中的所有元素
class Star(Sprite):
	def __init__(self,sys_settings,screen):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.sys_settings = sys_settings
		self.image = pygame.image.load('images/ball.png')
		#获得图像外接矩形，并设置矩形的x,y坐标
		self.rect = self.image.get_rect()
		self.rect.x = randint(0,self.screen_rect.width)
		self.rect.y = 0
		#self.rect.x = self.rect.width
		#self.rect.y = self.rect.height
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def random_justice(self):
		random_origin = randint(50,100)
		random_number = randint(-50,random_origin)
		#self.x += random_number
		self.rect.y += random_number
		#self.rect.x = self.x

	def update(self):
		self.y += self.sys_settings.drop_speed
		self.rect.y = self.y
		#self.rect.y = self.y
	
	def check_bottom(self):
		'''是否超出底部'''
		screen_rect = self.screen.get_rect()
		return self.rect.top >= screen_rect.bottom
