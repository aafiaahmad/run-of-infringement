import pygame,time, sys

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (107, 251, 216)
MAGENTA = (225, 41 ,124)

pygame.init()

# Set the width and height of the screen [width, height]
length = 700
width = 600
size = (length, width)
screen = pygame.display.set_mode(size)

green_x=20
white_x=25
green_l=660
white_l=650

stealth = False
strength = False
magic = False
manipulation = False
hp=100

pygame.display.set_caption("Run of Infringement")

# Loop until the user clicks the close button.
done = False

def draw():
    pygame.draw.rect(screen, GREEN, (green_x, 20, green_l, 360), 0)
    box=pygame.draw.rect(screen, WHITE, (white_x, 25, white_l, 350), 0)
    pygame.draw.rect(screen, GREEN, (green_x, 420,green_l, 160), 0)
    pygame.draw.rect(screen, BLACK, (white_x, 425,white_l, 150), 0)
    if hp==100:
        pygame.draw.rect(screen, MAGENTA, (625, 425, 50, 150), 0)  # the starting HP
    elif hp==75:
        pygame.draw.rect(screen, MAGENTA, (625, 425, 50, 112), 0)# the HP -25



    elif hp==50:
        pygame.draw.rect(screen, MAGENTA, (625, 425, 50, 74), 0)  # the HP -50
    elif hp==25:
        pygame.draw.rect(screen, MAGENTA, (625, 425, 50, 36), 0)  # the HP -75
    elif hp==0:
        pygame.draw.rect(screen, MAGENTA, (625, 425, 50, 1), 0)  # the HP -100
    myfont = pygame.font.SysFont("monospace", 25)
    label = myfont.render("HP", 1, WHITE)
    screen.blit(label, (635, 425))

def text(words):
    ycord = 400
    while len(words) > 0:
        max = min(60, len(words))
        tag = words[0:max]
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(tag, 1, WHITE)
        ycord += 15
        screen.blit(label, (25, ycord))
        words = words[max:]

    # myfont = pygame.font.SysFont("monospace", 15)
    # label = myfont.render(words, 1, WHITE)
    # screen.blit(label, (25, 400))


def text_1(words):
    ycord = 420
    while len(words) > 0:
        max = min(60, len(words))
        tag = words[0:max]
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(tag, 1, WHITE)
        ycord += 15
        screen.blit(label, (28, ycord))
        words = words[max:]

def mainstory(textput,animationlist):
    pygame.event.get()
    while pygame.key.get_pressed()[pygame.K_SPACE]==0:
        pygame.event.get()
        if pygame.key.get_pressed()[pygame.K_x]==1:
            sys.exit()
        screen.fill(BLACK)
        draw()
        text_1(textput)
        if animationlist[0]==1:
            pygame.draw.rect(screen,(0,255,255),(50,50,50,50))
        if animationlist[1]==1:
            pygame.draw.rect(screen,(244,33,11),(100,100,100,100))
        pygame.display.flip()
        

# screen.fill(BLACK)
#                     draw()
# text("The story has begun")
# pygame.display.flip()

# intro = pygame.image.load("intro_screen.png")
# box.blit(pygame.transform.scale(intro, (white_x, 25)), white_l, 350)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#The story code goes here
texty= "Hello"
text1="Our father who art in heaven hollowed by thy name thy kingdom come they will be done on earth as it is in heaven."
text2="thy kingdom come, thy will be done, on earth as it is in heaven, give us this day our daily bread"
text3= "and forgive us from our trespasses, as we forgive those who tresspass against us."

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    mainstory(texty,[1,0])
    time.sleep(1)
    mainstory(text1,[0,1])
    time.sleep(1)
    mainstory(text2,[0,0])
    time.sleep(1)
    mainstory(text3,[0,0])
    # --- Game logic should go here
    y=0
    n=0
    if pygame.key.get_pressed()[pygame.K_y]!=0:
        y=1
    elif pygame.key.get_pressed()[pygame.K_n]!=0:
        n=1
    elif pygame.key.get_pressed()[pygame.K_i]!=0:
        i=1
    

    # --- Screen-clearing code goes here
    # screen.fill(BLACK)
    # draw()
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    draw()
    if pygame.key.get_pressed()[pygame.K_1]!= 0:
        stealth=True
        costume=stealth
        strength=False
        magic=False
        manipulation=False
    elif pygame.key.get_pressed()[pygame.K_2]!= 0:
        strength=True
        costume=strength
        stealth=False
        magic=False
        manipualtion=False
    elif pygame.key.get_pressed()[pygame.K_3]!= 0:
        magic=True
        costume=magic
        stealth=False
        strength=False
        manipulation=False
    elif pygame.key.get_pressed()[pygame.K_4]!= 0:
        manipulation=True
        costume=manipulation
        stealth=False
        strength=False
        magic=False

    if stealth==True:
        text("YOU CHOSE STEALTH")
    elif strength==True:
        text("YOU CHOSE STRENGTH")
    elif magic==True:
        text("YOU CHOSE MAGIC")
    elif manipulation==True:
        text("YOU CHOSE MANIPULATION")
    else:
        text("")

## THIS IS THE BASIC FORMAT FOR RECEIVING USER INPUT AND USING THAT INPUT TO CONTINUE THE STORY PROGRESSION ##
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         done = True
    #     if event.type==pygame.KEYDOWN:
    #         if event.key==pygame.K_SPACE:
    #             while not done:
    #                 mainstory(text1)

    #                 for event in pygame.event.get():
    #                     if event.type == pygame.QUIT:
    #                         done = True
    #                     if event.type == pygame.KEYDOWN:
    #                         if event.key == pygame.K_SPACE:
    #                             while not done:
    #                                 mainstory(text2)

    #                                 for event in pygame.event.get():
    #                                     if event.type == pygame.QUIT:
    #                                         done = True
    #                                     if event.type == pygame.KEYDOWN:
    #                                         if event.key == pygame.K_SPACE:
    #                                             while not done:
    #                                                 mainstory(text3)

    #                                         if event.key == pygame.K_f:
    #                                             while not done:
    #                                                 text("YOU KILLED HIM")


    pygame.display.flip()
    # --- Go ahead and update the screen with what we've drawn.
    # pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE