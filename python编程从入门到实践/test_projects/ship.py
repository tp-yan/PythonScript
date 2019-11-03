import pygame

class Ship():
	def __init__(self,sys_settings,screen):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.sys_settings = sys_settings
		self.speed = sys_settings.ship_speed
		
		self.img = pygame.image.load('images/ship_png.png')
		self.rect = self.img.get_rect()
		
		self.reset_position()
		
		self.moving_up = False
		self.moving_down = False

	def update(self):
		if self.moving_up and self.rect.top > 0:
			self.y -= self.speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.speed
		self.check_edges()
		self.rect.y = self.y
		
	def check_edges(self):
		if self.y < 0:
			self.y = 0
		elif self.y > self.screen_rect.bottom:
			self.y = self.screen_rect.bottom

	def draw_ship(self):
		self.screen.blit(self.img,self.rect)
		
	def reset_position(self):
		self.rect.left = self.screen_rect.left
		self.rect.centery = self.screen_rect.centery
		
		self.y = float(self.rect.y)
		
