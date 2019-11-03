import pygame.font

class Button():
	'''按钮：带标签的矩形'''
	
	def __init__(self,ai_settings,screen,msg):
		'''初始化按钮的属性'''
		self.screen = screen
		self.screen_rect = screen.get_rect()
		#设置按钮的尺寸以及其他属性
		self.width,self.height = 200,50
		self.fill_color = (0,255,0)
		self.text_color = (255,255,255)
		#None：字体用默认格式，48：字体大小
		self.font = pygame.font.SysFont(None,48)
		
		#创建按钮的rect对象并居中
		self.rect = pygame.Rect(0,0,self.width,self.height)
		self.rect.center = self.screen_rect.center
		#按钮的标签
		self.prep_msg(msg)
		
	def prep_msg(self,msg):
		'''将msg渲染为图像，在按钮上居中'''
		self.msg_img = self.font.render(msg,True,self.text_color,
						self.fill_color)
		self.msg_img_rect = self.msg_img.get_rect()
		self.msg_img_rect.center = self.rect.center
	
	def draw_button(self):
		#绘制按钮
		self.screen.fill(self.fill_color,self.rect)
		#绘制文本图像
		self.screen.blit(self.msg_img,self.msg_img_rect)
		
