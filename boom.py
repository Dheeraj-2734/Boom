import pygame
import math
import random
from pygame import mixer

pygame.init()
window = pygame.display.set_mode((600,600))
pygame.display.set_caption("kjhgfdtyuiolkbvcx")

pygame.display.set_icon(pygame.image.load("spiderplant.png"))

#background music
# mixer.music.load("bg.wav")
# mixer.music.play(-1)

laser = mixer.Sound("buush.wav")
blast = mixer.Sound("buduk.wav")

#jet
jet_image = pygame.image.load("jet.xcf")
j_x=300
j_y=525
j_change=0

#laser
laser_image = pygame.image.load("laser.xcf")
l_x=300
l_y=525
l_status=True

#ship
ship_image = pygame.image.load("Ship.xcf")
s_x=[ ]
s_y=[ ]
s_change= [ ]

score =0
font = pygame.font.Font( 'freesansbold.ttf',30)
go = pygame.font.Font( 'freesansbold.ttf',30)
score_x=10
score_y=10

#number of ships on screen
mfs_count = 3
# mfs_count = int(input("number of ships"))
for i in range(mfs_count):
    s_x.append(random.randint(0, 550))
    s_y.append(random.randint(0, 50))
    s_change.append(0.1)


def jet_mc(x,y):
    window.blit(jet_image , (x,y))

def laser_mc(x,y):
    window.blit(laser_image , (x,y-15))

def show_score(x,y):
    sc = font.render("Score : " + str(score), True, (255,255,255))
    window.blit(sc, (x,y))

def game_over(x,y):
    you_lose = go.render("GAME OVER!", True, (255,255,255))
    window.blit(you_lose, (x,y))

def game_over_youwin(x,y):
    you_win = go.render("YOU WIN !", True, (255,255,255))
    window.blit(you_win, (x,y))

def ship_mf(x,y):
  window.blit(ship_image , (x,y))

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        #jet movements
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                j_change = -0.2
                
            if event.key == pygame.K_RIGHT:
                j_change = 0.2
            if event.key == pygame.K_SPACE:
               if l_status ==True :
                   laser.play()

               l_status=False


        if event.type==pygame.KEYUP:
             j_change = 0


    j_x += j_change

    if (l_status==True):
       l_x += j_change


    if (l_status==False):
        l_y -= 0.4

    if (l_y<0):
        l_y=j_y
        l_x=j_x
        l_status=True


    if j_x > 570:
        j_x -= 0.2
    if j_x < 0:
        j_x += 0.2

  
     

    window.fill((0,0,0))
    laser_mc(l_x,l_y)
    jet_mc(j_x,j_y)
    show_score(score_x,score_y)
    # ship_mf(s_x, s_y)
    for j in range(mfs_count)  :
        #collision
        dis = math.sqrt(math.pow((l_x - s_x[j]), 2) + math.pow((l_y - s_y[j]), 2))

        if dis<20:

            #score mode
        #     s_y[j] = -500
        #     score += 1                    
        #     blast.play()
        # if score == mfs_count:
        #     game_over_youwin(300, 300)

              
           #toggle between these ^ two \/ by commenting the other

            #endless mode
            s_y[j] = 0
            s_x[j] = random.randint(0, 550)
            score += 1
            blast.play()
      


        s_x[j] += s_change[j]

        if s_x[j] > 570:
            s_change[j]= -0.1
            s_y[j]+= 32
        if s_x[j] < 0:
            s_change[j] = 0.1
            s_y[j] += 32


        if s_y[j] > 500:
            game_over(300, 300)
        ship_mf(s_x[j], s_y[j])
    pygame.display.update()