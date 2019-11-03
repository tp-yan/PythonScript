
class Settings():
	'''全局系统设置'''
	
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (255,255,255)
		
		self.drop_speed = 0.4
		
		#球拍设置
		self.racket_width = 100
		self.racket_height = 5
		self.racket_color = (122,0,0)
		self.racket_speed = 1
		self.racket_limit = 3
		
		#目标矩形设置
		self.target_rect_width = 10
		self.target_rect_height = 100
		self.target_rect_color = (0,0,255)
		
		
		#button类的设置
		self.button_width = 100
		self.button_height = 40
		self.button_color = (0,255,0)
		self.button_txt_color = (255,255,255)
		
		#击中次数
		self.hit_times = 0
		
		#bullet设置
		self.bullet_width = 10
		self.bullet_height = 2
		self.bullet_color = (255,0,0)
		
		#游戏速度
		self.speed_scale = 1.2
		
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		#ship的设置
		self.ship_speed = 0.5
		self.bullet_speed = 1
		self.target_rect_speed = 0.5
		
	def increase_speed(self):
		self.ship_speed *= self.speed_scale
		self.bullet_speed *= self.speed_scale
		self.target_rect_speed *= self.speed_scale
		
