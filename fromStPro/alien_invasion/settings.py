class Settings():
	'''保存游戏中的所有设置'''
	
	def __init__(self):
		'''初始化游戏设置'''
		'''在__init__中定义的属性，称为静态属性'''
		#屏幕设置
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (230,230,230)
		#飞船的横移速度,单位像素
		self.ship_limit = 2
		
		#子弹设置
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullet_max_num = 3
		
		#外星人
		self.alien_drop_speed = 30
		#游戏速度
		self.speed_scale = 1.1
		#外星人点数提高比例
		self.score_scale = 1.5
		
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		'''初始化 随游戏进行而变化的设置'''
		'''在__init__外定义的属性，称为动态属性'''
		self.ship_speed_factor = 0.5
		self.bullet_speed_factor = 2
		self.alien_speed_factor = 1
		#左右移动标志，1：右移，-1：左移
		self.fleet_direction = 1
		#一个外星人的分数
		self.alien_points = 50
		

	def increase_speed(self):
		'''提高速度'''
		self.ship_speed_factor *= self.speed_scale
		self.bullet_speed_factor *= self.speed_scale
		self.alien_speed_factor *= self.speed_scale
		self.alien_points = int(self.alien_points*self.score_scale)
