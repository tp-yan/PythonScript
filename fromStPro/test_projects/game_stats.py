class GameStats():
	def __init__(self,sys_settings):
		self.sys_settings = sys_settings
		self.game_active = False
		self.reset_stats()
		
	def reset_stats(self):
		self.rackets_left = self.sys_settings.racket_limit
		self.hit_times = self.sys_settings.hit_times
