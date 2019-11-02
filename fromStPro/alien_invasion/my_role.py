import pygame

class MyRole():
	def __init__(self,screen):
		'''将自定义图像绘制在屏幕中央'''
		self.screen = screen
		#加载图片
		self.image = pygame.image.load('images/my_role.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.left = self.screen_rect.left
		self.rect.centery = self.screen_rect.centery
		
		#移动标志
		self.moving_right = False
		self.moving_left = False
		self.moving_top = False
		self.moving_bottom = False
		
	def update(self):
		'''根据移动标志调整位置,并限制在屏幕内'''
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += 1
		if self.moving_left and self.rect.left > 0:
			self.rect.centerx -= 1
		if self.moving_top and self.rect.top > 0:
			self.rect.centery -= 1
		if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += 1
			
	def blitme(self):
		'''在指定位置绘制图像'''
		self.screen.blit(self.image,self.rect)
		
