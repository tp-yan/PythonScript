import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,sys_settings,screen,ship):
		super().__init__()
		self.screen = screen 
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect(0,0,
			sys_settings.bullet_width,sys_settings.bullet_height)
		self.rect.right = ship.rect.right
		self.rect.centery = ship.rect.centery
		self.color = sys_settings.bullet_color
		self.speed = sys_settings.bullet_speed
		
		self.x = float(self.rect.x)
		
	def update(self):
		self.x += self.speed
		self.rect.x = self.x

	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
	
	def check_edges(self):
		return self.rect.right > self.screen_rect.right
