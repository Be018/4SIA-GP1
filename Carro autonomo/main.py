import neat.config
import neat.nn.feed_forward
import neat.statistics
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
        self.velocidade = pygame.math.Vector2(0.5, 0)
        self.angulo = 0
        self.rotation_v = 3
        self.direction = 0
        self.alive = True
        self.radars = []
        
    def update(self):
        self.radars.clear()
        self.drive()
        self.rotate()
        for radar_angle in (-60, -30, 0, 30, 60): 
            self.radar(radar_angle)
        self.collision()
        self.data()
    
    def drive(self):
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
        
        while not screen.get_at((x, y)) == pygame.Color(34, 177, 76, 255) and length < 80:
            length += 1
            x = int(self.rect.center[0] + math.cos(math.radians(self.angulo + radar_angle)) * length)
            y = int(self.rect.center[1] - math.sin(math.radians(self.angulo + radar_angle)) * length)
            
        pygame.draw.line(screen, (255, 255, 255, 255), self.rect.center, (x, y), 1)
        pygame.draw.circle(screen, (0, 0, 255, 0), (x, y), 3)
        
        distance = int(math.sqrt(math.pow(self.rect.center[0] - x, 2)
                                 + math.pow(self.rect.center[1] - y, 2)))
        self.radars.append([radar_angle, distance])
        
    def data(self):
        input = [0, 0, 0, 0, 0]
        for i, radar in enumerate(self.radars):
            input[i] = int(radar[1])
        return input
    
def remove(index):
    cars.pop(index)
    ge.pop(index)
    nets.pop(index)
    

def eval_genomes(genomes, config):
    global cars, ge, nets

    cars = []
    ge = []
    nets = []

    for genome_id, genome in genomes:
        cars.append(pygame.sprite.GroupSingle(Car()))
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(track, (0, 0))

        if len(cars) == 0:
            break

        for i, car in enumerate(cars):
            ge[i].fitness += 1
            if not car.sprite.alive:
                remove(i)

        for i, car in enumerate(cars):
            output = nets[i].activate(car.sprite.data())
            if output[0] > 0.7:
                car.sprite.direction = 1
            if output[1] > 0.7:
                car.sprite.direction = -1
            if output[0] <= 0.7 and output[1] <= 0.7:
                car.sprite.direction = 0

        # Update
        for car in cars:
            car.draw(screen)
            car.update()
        pygame.display.update()


        


# NEAT
def run(config_path):
    global pop
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)

    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)

    pop.run(eval_genomes, 50)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)
