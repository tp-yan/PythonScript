import pygame
from random import randint

class TargetRect():
	'''上下移动的矩形'''
	def __init__(self,sys_settings,screen):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.sys_settings = sys_settings
		self.width = sys_settings.target_rect_width
		self.height = sys_settings.target_rect_height
		self.color = sys_settings.target_rect_color
		self.speed = sys_settings.target_rect_speed
		#移动方向：上正下负
		self.direction = 1
		
		self.rect = pygame.Rect(0,0,self.width,self.height)
		self.rect.right = self.screen_rect.right
		self.rect.y = randint(0,self.screen_rect.height)
		self.y = float(self.rect.y)

	def update(self):
		'''更新位置'''
		self.y += self.speed*self.direction
		self.rect.y = self.y
		self.check_edges()
		
	def check_edges(self):
		'''检查是否达到屏幕边界'''
		if self.rect.bottom > self.screen_rect.bottom:
			self.rect.bottom = self.screen_rect.bottom
			self.change_direction()
		if self.rect.top < self.screen_rect.top:
			self.rect.top = self.screen_rect.top
			self.change_direction()
	
	def change_direction(self):
		self.direction *= -1
		
		
	def draw_target_rect(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
