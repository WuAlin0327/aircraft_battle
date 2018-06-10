import pygame
from random import *

class SmallEnemy(pygame.sprite.Sprite):
    
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("images/enemy1.png").convert_alpha()        
        #敌机毁灭动画
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy1_down1.png").convert_alpha(),\
            pygame.image.load("images/enemy1_down2.png").convert_alpha(),\
            pygame.image.load("images/enemy1_down3.png").convert_alpha(),\
            pygame.image.load("images/enemy1_down4.png").convert_alpha()\
            ])

        self.rect = self.image.get_rect()       #获得敌机尺寸
        self.width, self.height = bg_size[0],bg_size[1]     #限制敌机不超过屏幕大小
        self.speed = 5      #敌机移动速度
        self.active = True
        self.rect.left,self.rect.top = \
                        randint(0,self.width - self.rect.width), \
                        randint(-5 * self.height, 0)        #敌机随机生成位置
                        
    def move(self):     #敌机运动函数
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()
                
    def reset(self):     #初始化敌机位置
        self.active = True
        self.rect.left,self.rect.top = \
                    randint(0,self.width - self.rect.width), \
                    randint(-5 * self.height, 0)
                        
                        
#定义中型敌机
class MidEnemy(pygame.sprite.Sprite):
    energy = 8
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("images/enemy2.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy2_down1.png").convert_alpha(),\
            pygame.image.load("images/enemy2_down2.png").convert_alpha(),\
            pygame.image.load("images/enemy2_down3.png").convert_alpha(),\
            pygame.image.load("images/enemy2_down4.png").convert_alpha()\
            ])

        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0],bg_size[1]  
        self.speed = 2
        self.active = True
        self.rect.left,self.rect.top = \
                        randint(0,self.width - self.rect.width), \
                        randint(-10 * self.height, -self.height)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = MidEnemy.energy
        self.hit = False
                        
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()
                
    def reset(self):
        self.active = True
        self.energy = MidEnemy.energy
        self.rect.left,self.rect.top = \
                      randint(0,self.width - self.rect.width), \
                      randint(-10 * self.height, -self.height)
                      
#定义大型敌机
class BigEnemy(pygame.sprite.Sprite):  #中型敌机类
    energy = 20
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image1 = pygame.image.load("images/enemy3_n1.png").convert_alpha()
        self.image2 = pygame.image.load("images/enemy3_n2.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy3_hit.png").convert_alpha()

        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy3_down1.png").convert_alpha(),\
            pygame.image.load("images/enemy3_down2.png").convert_alpha(),\
            pygame.image.load("images/enemy3_down3.png").convert_alpha(),\
            pygame.image.load("images/enemy3_down4.png").convert_alpha(),\
            pygame.image.load("images/enemy3_down5.png").convert_alpha(),\
            pygame.image.load("images/enemy3_down6.png").convert_alpha()\
            ])

        self.rect = self.image1.get_rect() 
        self.width, self.height = bg_size[0],bg_size[1]  
        self.speed = 1
        self.active = True
        self.rect.left,self.rect.top = \
                        randint(0,self.width - self.rect.width), \
                        randint(-15 * self.height, -5 * self.height)
        self.mask = pygame.mask.from_surface(self.image1)
        self.energy = BigEnemy.energy
        self.hit = False
             

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()
                
    def reset(self):
        self.active = True
        self.energy = BigEnemy.energy
        self.rect.left,self.rect.top = \
                      randint(0,self.width - self.rect.width), \
                      randint(-15 * self.height, -5 * self.height)
