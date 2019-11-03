import sys
import pygame

from time import sleep
from bullet import Bullet
from alien import Alien

def check_events(ai_settings,screen,ship,aliens,bullets,play_button
		,stats,score):
	'''监视键盘与鼠标事件'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			save_high_score(stats)
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets
				,aliens,stats)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings,screen,ship,aliens,bullets
				,stats,play_button,mouse_x,mouse_y,score)

def check_play_button(ai_settings,screen,ship,aliens,bullets,stats
		,play_button,mouse_x,mouse_y,score):
	'''玩家单击Play按钮时开始游戏'''
	if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
		start_game(ai_settings,screen,ship,aliens,bullets,stats,score)

def start_game(ai_settings,screen,ship,aliens,bullets,stats,score):
	#隐藏光标
	pygame.mouse.set_visible(False)
	#重置游戏信息
	ai_settings.initialize_dynamic_settings()
	stats.reset_stats()
	score.prep_score()
	score.prep_level()
	score.prep_ships()
	#score.show_score()
	stats.game_active = True
	aliens.empty()
	bullets.empty()
	create_fleet(ai_settings,screen,ship,aliens)
	ship.center_ship()
	
		
def check_keydown_events(event,ai_settings,screen,ship,bullets,aliens,stats):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets,stats)
	elif event.key == pygame.K_q:
		save_high_score(stats)
		sys.exit()
	elif event.key == pygame.K_p and not stats.game_active:
		start_game(ai_settings,screen,ship,aliens,bullets,stats)
				
def fire_bullet(ai_settings,screen,ship,bullets,stats):
	'''发射子弹'''
	#创建一颗子弹，并加入到编组bullets中
	if len(bullets) < ai_settings.bullet_max_num:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
			
def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	
def update_screen(ai_settings,screen,ship,aliens,bullets,stats
		,play_button,score):
	'''更新屏幕上的图像，并切换到新屏幕'''
	screen.fill(ai_settings.bg_color)
	score.show_score()
	#重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
		
	ship.blitme()
	#对编组调用draw()时，Pygame自动绘制编组中的每个元素，绘制位置由元素的属性rect决定
	#这里在屏幕上绘制编组中的外星人
	aliens.draw(screen)
	
	if not stats.game_active:
		play_button.draw_button()
	
	pygame.display.flip()	

def update_bullets(ai_settings,screen,ship,aliens,bullets,stats,score):
	'''更新子弹的位置，并删除已消失子弹'''
	#此操作将调用 编组中每个bullet的update()
	bullets.update()
	#删除已消失的子弹，在for循环中删除列表的元素，使用copy
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	#检查是否有子弹击中外星人，若有则删除相应的子弹与外星人
	check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets
	,stats,score)
	
	
def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets
	,stats,score):
	#此方法检查bullets与aliens的rect是否重叠，若是，则以 bullet-alien的键值对方式
	#存入collisions字典，False:不删除，True：删除，分别对应bullets、aliens
	collisions = pygame.sprite.groupcollide(bullets,aliens,False,True)
	#collisions的每一个value是与bullet碰撞的aliens的列表	
	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points*len(aliens)
			score.prep_score()
		check_high_score(stats,score)
		
	if len(aliens) == 0:
		up_level(ai_settings,screen,ship,aliens,stats,score,bullets)
			
def up_level(ai_settings,screen,ship,aliens,stats,score,bullets):
	ai_settings.increase_speed()
	stats.level += 1
	score.prep_level()
	#删除现有的子弹并新建一群外星人
	bullets.empty()
	create_fleet(ai_settings,screen,ship,aliens)

def create_fleet(ai_settings,screen,ship,aliens):
	'''创建外星人舰队'''
	#创建一个外星人计算每行可容纳几个alien，外星人间距为外星人宽度
	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_alienx_x(ai_settings,alien.rect.width)
	number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
	
	#创建外星人群
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,row_number)

def get_number_alienx_x(ai_settings,alien_width):
	'''计算每行容纳的外星人数'''
	available_space_x = ai_settings.screen_width - alien_width
	number_aliens_x = int(available_space_x / (2*alien_width))
	return number_aliens_x
	
def get_number_rows(ai_settings,ship_height,alien_height):
	'''计算容纳外星人的行数'''
	available_space_y = (ai_settings.screen_height-(3*alien_height)-ship_height)
	number_rows = int(available_space_y / (2*alien_height))
	return number_rows
	
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	'''创建一个外星人并将其加入当前行'''
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2*alien_width*alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
	aliens.add(alien)
	
	
	
	
	
	
	
	
	
	
def check_events2(ai_settings,screen,my_role,bullets):
	'''监视键盘与鼠标事件'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events2(event,ai_settings,screen,my_role,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events2(event,my_role)

def check_keydown_events2(event,ai_settings,screen,my_role,bullets):
	if event.key == pygame.K_RIGHT:
		my_role.moving_right = True
	elif event.key == pygame.K_LEFT:
		my_role.moving_left = True
	elif event.key == pygame.K_UP:
		my_role.moving_top = True
	elif event.key == pygame.K_DOWN:
		my_role.moving_bottom = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,my_role,bullets)
		
def check_keyup_events2(event,my_role):
	if event.key == pygame.K_RIGHT:
		my_role.moving_right = False
	elif event.key == pygame.K_LEFT:
		my_role.moving_left = False
	elif event.key == pygame.K_UP:
		my_role.moving_top = False
	elif event.key == pygame.K_DOWN:
		my_role.moving_bottom = False
					
def update_bullets2(bullets,screen_rect):
	'''更新子弹的位置，并删除已消失子弹'''
	#此操作将调用 编组中每个bullet的update()
	bullets.update()
	#删除已消失的子弹，在for循环中删除列表的元素，使用copy
	for bullet in bullets.copy():
		if bullet.rect.right >= screen_rect.right:
			bullets.remove(bullet)

def update_aliens(ai_settings,stats,screen,bullets,aliens,ship,score):
	'''更新外星人群中的位置'''
	check_fleet_edges(aliens)
	aliens.update()
	#检查ship与alien之间的碰撞
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,stats,screen,bullets,aliens,ship,score)
	#检查是否到达底部
	check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,score)

def ship_hit(ai_settings,stats,screen,bullets,aliens,ship,score):
	'''响应飞船被撞击'''
	if stats.ships_left > 0:
		stats.ships_left -= 1
		#更新记分牌
		score.prep_ships()
		#清空外星人与子弹
		aliens.empty()
		bullets.empty()
		#当外星人被消除完，则提高游戏速度
		ai_settings.increase_speed()
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()
		#暂停
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)
	
def check_fleet_edges(aliens):
	'''检查外星人是否到达边缘'''
	for alien in aliens.sprites():
		if alien.check_edges():
			alien.change_direction()

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,score):
	'''是否有外星人到达底部'''
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings,stats,screen,bullets,aliens,ship,score)
			break

def check_high_score(stats,score):
	'''检查是否诞生了新的最高分'''
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		score.prep_high_score()
	
def get_high_score(stats):
	file_name = "high_score.txt"
	with open(file_name) as f_obj:
		content = f_obj.read()
	if not content:
		content = '0'
	high_score = int(content)
	stats.high_score = high_score

def save_high_score(stats):
	file_name = "high_score.txt"
	with open(file_name,"w") as f_obj:
		f_obj.write(str(stats.high_score))
		
	
