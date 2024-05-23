import pygame
import os
import math
import sys
import neat

screen_width = 1008
screen_height = 675
screen = pygame.display.set_mode((screen_width, screen_height))

track = pygame.image.load(os.path.join("Assets", "Track.png"))

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load(os.path.join("Assets", "carro2.png"))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(100, 100))
        self.drive_state = False
        self.velocidade = pygame.math.Vector2(0.5, 0)
        self.angulo = 0
        self.rotation_v = 3
        self.direction = 0
        self.alive = True
        
    def update(self):
        self.drive()
        self.rotate()
        for radar_angle in (-60, -30, 0, 30, 60): 
            self.radar(radar_angle)
        self.collision()
    
    def drive(self):
        if self.drive_state:
                self.rect.center += self.velocidade * 6
    
    def collision(self):
        length = 20
        collision_r = [int(self.rect.center[0] + math.cos(math.radians(self.angulo + 18)) * length),
                       int(self.rect.center[1] - math.sin(math.radians(self.angulo + 18)) * length)]
        collision_l = [int(self.rect.center[0] + math.cos(math.radians(self.angulo - 18)) * length),
                       int(self.rect.center[1] - math.sin(math.radians(self.angulo - 18)) * length)]
        if screen.get_at(collision_r) == pygame.Color(34, 177, 76, 255) \
            or screen.get_at(collision_l) == pygame.Color(34, 177, 76, 255):
                self.alive = False
        pygame.draw.circle(screen, (0,255,255,0), collision_r, 4)
        pygame.draw.circle(screen, (0,255,255,0), collision_l, 4)
            
    
    def rotate(self):
        if self.direction == 1:
            self.angulo -= self.rotation_v
            self.velocidade.rotate_ip(self.rotation_v)
        if self.direction == -1:
            self.angulo += self.rotation_v
            self.velocidade.rotate_ip(-self.rotation_v)
            
        self.image = pygame.transform.rotozoom(self.original_image, self.angulo, 0.1)
        self.rect = self.image.get_rect(center = self.rect.center)
        
    def radar(self, radar_angle):
        length = 0
        x = int(self.rect.center[0])
        y = int(self.rect.center[1])
        
        while not screen.get_at((x, y)) == pygame.Color(34, 177, 76, 255) and length < 100:
            length += 1
            x = int(self.rect.center[0] + math.cos(math.radians(self.angulo + radar_angle)) * length)
            y = int(self.rect.center[1] - math.sin(math.radians(self.angulo + radar_angle)) * length)
            
        pygame.draw.line(screen, (255, 255, 255, 255), self.rect.center, (x, y), 1)
        pygame.draw.circle(screen, (0, 0, 255, 0), (x, y), 3)
        
car = pygame.sprite.GroupSingle(Car())


def eval_genomes():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(track, (0,0))
        
        #input
        user_input = pygame.key.get_pressed()
        if sum(pygame.key.get_pressed()) <= 1:
            car.sprite.drive_state = False
            car.sprite.direction = 0
        #drive
        if user_input[pygame.K_UP]:
            car.sprite.drive_state = True
            car.sprite.direction = 0
        #volante
        if user_input[pygame.K_RIGHT]:
            car.sprite.direction = 1
        
        if user_input[pygame.K_LEFT]:
            car.sprite.direction = -1
        #update
        car.draw(screen)  
        car.update()
        pygame.display.update() 
        
eval_genomes()
        
