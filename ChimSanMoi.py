import pygame, sys, random, os
from pygame.locals import *



SCRENN_HEIGHT = 500
SCREEN_WEIGHT = 1000

BIRD_HEIGHT = 30
BIRD_WEIGHT = 30

FOOD_HEIGHT = 40
FOOD_WEIGHT = 40

SCORE_HEIGHT = 50
SCORE_WEIGHT = 60
pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
DISPLAYSUR = pygame.display.set_mode((SCREEN_WEIGHT, SCRENN_HEIGHT))
pygame.display.set_caption('chim_san_moi')

SPAWN_INTERVAL = 1000

class Bird():
    def __init__(self):
        self.x = 0
        self.y = (SCRENN_HEIGHT - BIRD_HEIGHT)/2
        self.w = BIRD_WEIGHT
        self.h = BIRD_HEIGHT
        self.speed = 5

    def draw(self):
        birdSurface = pygame.Surface((30, 30), SRCALPHA)
        birdRect = pygame.draw.rect(birdSurface, (255, 0, 0), (0, 0, 30 , 30), 2)
        DISPLAYSUR.blit(birdSurface, (self.x, self.y))

    def update(self, butonUp, butonDown):
        if butonUp == True:
            self.y -= self.speed
        if butonDown == True:
            self.y += self.speed
        if self.y < 0:
            self.y = 0
        if self.y  + self.h > SCRENN_HEIGHT:
            self.y = SCRENN_HEIGHT - self.h

class Food():
    def __init__(self, img_path):
        pygame.sprite.Sprite.__init__(self)
        self.w = FOOD_WEIGHT
        self.h = FOOD_WEIGHT
        self.speed = 3
        self.img = pygame.image.load(img_path).convert_alpha()
        self.img= pygame.transform.scale(self.img,( random.randint(20, 30), random.randint(20, 30)))                    
        self.rect = self.img.get_rect()
        self.rect.x = SCREEN_WEIGHT + self.rect.width
        self.rect.y = random.randint(0, SCRENN_HEIGHT - self.rect.height - 200)
    def draw(self, DISPLAYSUR):
        DISPLAYSUR.blit(self.img, self.rect)
    
    def move(self):
        self.rect.x -= self.speed

    def is_off_creen(self):
        return self.rect.x + self.rect.width < 0
    def update(self):
        pass
        
images = []

food_paths = [
    'keo1.jpg', 
    'rsz_11keo2.jpg',
    'rsz_keodatbiet.jpg'
]


spawn_timer = 0
bird = Bird()
butonUp =False
butonDown = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                butonUp = True
            if event.key == pygame.K_DOWN:
                butonDown = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                butonUp = False
            if event.key == pygame.K_DOWN:
                butonDown = False

    DISPLAYSUR.fill((0, 0, 0))   
    
    bird.draw()
    bird.update(butonUp, butonDown)
    
    spawn_timer += fpsClock.get_time()
    if spawn_timer >= SPAWN_INTERVAL:
        food_path = random.choices(food_paths, weights= [0.4, 0.4, 0.2])
        images.append(Food(random.choice(food_path)))
        spawn_timer = 0

    for img in images:
        img.move()

    images = [img for img in images if not img.is_off_creen()]

    for img in images:
        img.draw(DISPLAYSUR)

    pygame.display.update()
    fpsClock.tick(FPS)
