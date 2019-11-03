import pygame.font

class Button():
	'''由文字图像与按钮矩形合成'''
	def __init__(self,sys_settings,screen,msg):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.width,self.height = sys_settings.button_width,sys_settings.button_height
		self.bg_color = sys_settings.button_color
		self.txt_color = sys_settings.button_txt_color
		#用于 文字-->图像
		self.font = pygame.font.SysFont(None,48)
		
		self.rect = pygame.Rect(0,0,self.width,self.height)
		self.rect.center = self.screen_rect.center
		#将文字转换为图像
		self.prep_msg(msg)
	
	def prep_msg(self,msg):
		self.msg_img = self.font.render(msg,True,self.txt_color)
		self.msg_img_rect = self.msg_img.get_rect()
		self.msg_img_rect.center = self.rect.center
	
	def draw_button(self):
		#用指定颜色填充rect区域
		self.screen.fill(self.bg_color,self.rect)
		#screen.blit:将图像输出到屏幕，pygame.draw.rect:直接在屏幕上绘制图案
		self.screen.blit(self.msg_img,self.msg_img_rect)
