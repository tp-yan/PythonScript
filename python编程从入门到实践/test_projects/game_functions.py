import pygame
import sys
from star import Star
from rain import Rain
from racket import Racket
from game_stats import GameStats
from bullets import Bullet


def check_events(stars,rackets,play_button,stats,ship,bullets,sys_settings,screen):
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			events_keydown(event,stars,rackets,ship,bullets,stats,sys_settings,screen)
		if event.type == pygame.KEYUP:
			events_keyup(event,rackets,ship)
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos()
			check_play_button(play_button,mouse_x,mouse_y,stats,ship,sys_settings)
			
		
def check_play_button(play_button,mouse_x,mouse_y,stats,ship,sys_settings):
	if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
		pygame.mouse.set_visible(False)
		stats.reset_stats()
		stats.game_active = True
		ship.reset_position()
		sys_settings.initialize_dynamic_settings()
		
		
def events_keydown(event,stars,rackets,ship,bullets,stats,sys_settings,screen):
	'''按键按下事件'''
	if event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_z:
		random_justice_stars(stars)	
	elif event.key == pygame.K_RIGHT:
		change_racket_direction(rackets,True)
	elif event.key == pygame.K_LEFT:
		change_racket_direction(rackets,False)
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		if stats.game_active:
			fire_bullet(bullets,sys_settings,screen,ship)

def fire_bullet(bullets,sys_settings,screen,ship):
	if len(bullets) <= 0:
		bullet = Bullet(sys_settings,screen,ship)
		bullets.add(bullet)
		
def events_keyup(event,rackets,ship):
	if event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False
	for racket in rackets.sprites():
		racket.moving = False
	
	
def change_racket_direction(rackets,right):
	for racket in rackets.sprites():
		racket.moving = True
		if right :
			racket.direction = 1
		else:
			racket.direction = -1

def update_screen(sys_settings,screen,stars,rackets,stats,target,play_button,ship,bullets):
	screen.fill(sys_settings.bg_color)
	stars.draw(screen)
	ship.draw_ship()
	if stats.game_active:
		target.update()
	target.draw_target_rect()
	for racket in rackets.sprites():
		racket.draw_racket()
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	if not stats.game_active:
		play_button.draw_button()
	
	pygame.display.flip()

def create_stars(sys_settings,screen,stars):
	star = Star(sys_settings,screen)
	number_stars = get_number_star(sys_settings.screen_width,star.rect.width)
	number_rows = get_number_row(sys_settings.screen_height,star.rect.height)
	
	for row_number in range(number_rows):
		for star_number in range(number_stars):
			create_star(sys_settings,screen,stars,row_number,star_number)
			
def create_star(sys_settings,screen,stars,row_number,star_number):
	star = Star(sys_settings,screen)
	'''
	star_width = star.rect.width
	star_height = star.rect.height
	star.rect.x = star_width + 2*star_width*star_number
	star.rect.y = star_height + 2*star_height*row_number
	'''
	stars.add(star)
	
def get_number_star(screen_width,star_width):
	avilable_star_x = screen_width - star_width
	number_star = int(avilable_star_x / (2*star_width))
	number_star = 1
	return number_star
	
def get_number_row(screen_height,star_height):
	available_star_y = screen_height - star_height
	number_row = int(available_star_y / (2*star_height)/ 2)
	number_row = 1
	return number_row

def random_justice_stars(stars):
	for star in stars.sprites():
		star.random_justice()
	
def update_stars(sys_settings,screen,stars,rackets,stats):
	stars.update()
	for star in stars.copy():
		if star.check_bottom():
			stats.rackets_left -= 1
			stars.remove(star)
	collisions = pygame.sprite.groupcollide(stars,rackets,True,False)
	#check_stars_bottom(stars,screen,stats)	
	'''
	if stats.rackets_left <= 0:
		stats.game_active = False
		pygame.mouse.set_visible(True)
		return 0
	'''
		
	if len(stars) < 0:
		create_stars(sys_settings,screen,stars)
	
def create_rackets(sys_settings,screen,rackets):
	racket = Racket(sys_settings,screen)
	rackets.add(racket)
		
def check_stars_bottom(stars,screen,stats):
	screen_rect = screen.get_rect()
	for star in stars.sprites():
		if star.rect.bottom >= screen_rect.bottom:
			stats.rackets_left -= 1
			 
def update_ship(ship):
	ship.update()
	
def update_rackets(rackets):
	rackets.update()
	
def update_bullets(bullets,target,stats,sys_settings):
	bullets.update()
	check_bullet_target(bullets,target,stats,sys_settings)
	for bullet in bullets.copy():
		if bullet.check_edges():
			bullets.remove(bullet)
		
def check_bullet_target(bullets,target,stats,sys_settings):
	bullet = pygame.sprite.spritecollideany(target,bullets)
	if bullet:
		stats.hit_times += 1
		bullets.remove(bullet)
	#print("hit_times:",stats.hit_times)
	if stats.hit_times >= 3:
		sys_settings.increase_speed()
		stats.hit_times = 0
		print("速度提高")
		#stats.game_active = False
		#pygame.mouse.set_visible(True)
	
