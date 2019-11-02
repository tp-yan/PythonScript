import pygame
from pygame.sprite import Sprite

class Racket(Sprite):
	'''球拍，用于接住小球'''
	
	def __init__(self,sys_settings,screen):
		'''在屏幕底部创建绘制一个球拍'''
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		#在（0,0）处创建一个矩形
		self.rect = pygame.Rect(0,0,sys_settings.racket_width,
			sys_settings.racket_height)
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.color = sys_settings.racket_color
		
		self.x = float(self.rect.x)
		self.speed = sys_settings.racket_speed
		#移动方向
		self.direction = 1
		self.moving = False
		
	def update(self):
		'''更新球拍的位置'''
		if self.moving :
			self.x += self.direction*self.speed
			self.rect.x = self.x

		if self.rect.left < self.screen_rect.left:
			self.rect.left = self.screen_rect.left
		if self.rect.right > self.screen_rect.right:
			self.rect.right = self.screen_rect.right

		
	def draw_racket(self):
		'''绘制球拍'''
		pygame.draw.rect(self.screen,self.color,self.rect)
	
