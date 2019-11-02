class Screen():
	
	@property
	def width(self):
		return self._width
	
	@width.setter
	def width(self,value):
		if value < 0:
			raise ValueError("width must bigger than 0")
		self._width = value
		
	@property	
	def height(self):
		return self._height
		
	@height.setter
	def height(self,value):
		if value < 0:
			raise ValueError("height must bigger than 0")
		self._height = value

	@property
	def resolution(self):
		return self._width*self._height
