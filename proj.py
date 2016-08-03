import pygame,time, sys,textwrap

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

#Functions
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
    ycord = 388
    while len(words) > 0:
        max = min(60, len(words))
        tag = words[0:max]
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(tag, 1, WHITE)
        ycord += 15
        screen.blit(label, (25, ycord))
        words = words[max:]

def text_printer(textnumber,wrapped_text):
    myfont=pygame.font.SysFont("monospace",15)
    label=myfont.render(wrapped_text[textnumber],1,WHITE)
    screen.blit(label,(30,425+15*textnumber))

def mainstory(textput,animationlist):
    pygame.event.get()
    textput_wrap=textwrap.wrap(textput,65)
    while pygame.key.get_pressed()[pygame.K_SPACE]==0:
        pygame.event.get()
        if pygame.key.get_pressed()[pygame.K_x]==1:
            sys.exit()
        screen.fill(BLACK)
        draw()
        for i in range(len(textput_wrap)):
            text_printer(i,textput_wrap)
#startlist of sprites and backgrounds
        if animationlist[0]==1:
            img1=pygame.image.load("spr_and_bgs/intro_screen.jpg")
            screen.blit(img1,(10,10))

        # if animationlist[1]==1:
            
        # if animationlist[2]==1:
           
        # if animationlist[3]==1:
        pygame.display.flip()
       
        

 

# intro = pygame.image.load("intro_screen.png")
# box.blit(pygame.transform.scale(intro, (white_x, 25)), white_l, 350)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#The story code goes here
text_intro= "You wake up with little recollection of who you are. Your surroundings are unfamiliar. Before you are four costumes, each promising to endow you with a new identity. Which do you choose? (1/2/3/4)"
text1="Our father who art in heaven hollowed by thy name thy kingdom come they will be done on earth as it is in heaven."
text2="thy kingdom come, thy will be done, on earth as it is in heaven, give us this day our daily bread"
text3= "and forgive us from our trespasses, as we forgive those who tresspass against us."

#intro
# mainstory(text_intro,[1])
# time.sleep(0.5)
# -------- Main Program Loop -----------

pygame.event.get()
while pygame.key.get_pressed()[pygame.K_SPACE]==0:
    pygame.event.get()
    # --- Main event loop
    screen.fill(BLACK)
    draw()
    img1=pygame.image.load("spr_and_bgs/intro_screen.jpg")
    screen.blit(img1,(25,25))
    pygame.event.get()
    textput_wrap=textwrap.wrap(text_intro,65)
    for i in range(len(textput_wrap)):
        text_printer(i,textput_wrap)
    if pygame.key.get_pressed()[pygame.K_x]==1:
        sys.exit()

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
        imgstea=pygame.image.load("spr_and_bgs/Stealth_Bio.jpg")
        screen.blit(imgstea,(25,25))
        text("CHOOSE STEALTH")
    elif strength==True:
        imgstre=pygame.image.load("spr_and_bgs/Strength_Bio.jpg")
        screen.blit(imgstre,(25,25))
        text("CHOOSE STRENGTH")
    elif magic==True:
        imgmag=pygame.image.load("spr_and_bgs/Magic_Bio.jpg")
        screen.blit(imgmag,(25,25))
        text("CHOOSE MAGIC")
    elif manipulation==True:
        imgmanip=pygame.image.load("spr_and_bgs/Charisma_Bio.jpg")
        screen.blit(imgmanip,(25,25))
        text("CHOOSE MANIPULATION")
    else:
        text("")
    pygame.display.flip()
    pygame.event.get()
    if pygame.key.get_pressed()[pygame.K_SPACE]==1:
        done=True


#Story
time.sleep(1)
mainstory(text1,[0])
time.sleep(1)
mainstory(text2,[0])
time.sleep(1)
mainstory(text3,[0])

# --- Game logic should go here --- #
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
   

pygame.display.flip()
# --- Go ahead and update the screen with what we've drawn.
# pygame.display.flip()

# --- Limit to 60 frames per second
clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE