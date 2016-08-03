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

yess= False
noo= False
bar_choice=False
table_choice=False
stealth = False
strength = False
magic = False
manipulation = False
hp=100

pygame.display.set_caption("Run of Infringement")

# Loop until the user clicks the close button.
done = False

#Functions
def draw(hp):
    pygame.draw.rect(screen, GREEN, (green_x, 20, green_l, 360), 0)
    box = pygame.draw.rect(screen, WHITE, (white_x, 25, white_l, 350), 0)
    pygame.draw.rect(screen, GREEN, (green_x, 420, green_l, 160), 0)
    pygame.draw.rect(screen, BLACK, (white_x, 425, white_l, 150), 0)
    if hp == 100:
        pygame.draw.rect(screen, MAGENTA, (625, 425, 50, 150), 0)  # the starting HP
    elif hp == 75:
        pygame.draw.rect(screen, MAGENTA, (625, 425, 50, 112), 0)  # the HP -25
    elif hp == 50:
        pygame.draw.rect(screen, MAGENTA, (625, 425, 50, 74), 0)  # the HP -50
    elif hp == 25:
        pygame.draw.rect(screen, MAGENTA, (625, 425, 50, 36), 0)  # the HP -75
    elif hp == 0:
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
        draw(100)
        for i in range(len(textput_wrap)):
            text_printer(i,textput_wrap)
#startlist of sprites and backgrounds
        if animationlist[0] == 1:
            img0 = pygame.image.load("spr_and_bgs/intro_screen.jpg")
            screen.blit(img0, (25, 25))
        if animationlist[1]==1:
            img1 = pygame.image.load(".png")
            screen.blit(img1, (25, 25))
        if animationlist[2]==1:
            img2 = pygame.image.load(".png")
            screen.blit(img2, (25, 25))
        if animationlist[3]==1:
            img3 = pygame.image.load(".png")
            screen.blit(img3, (25, 25))
        if animationlist[4] == 1:
            img4 = pygame.image.load(".png")
            screen.blit(img4, (25, 25))
        if animationlist[5] == 1:
            img5 = pygame.image.load(".png")
            screen.blit(img5, (25, 25))
        if animationlist[6] == 1:
            img6 = pygame.image.load(".png")
            screen.blit(img6, (25, 25))
        if animationlist[7] == 1:
            img7 = pygame.image.load(".png")
            screen.blit(img7, (25, 25))
        if animationlist[8] == 1:
            img8 = pygame.image.load(".png")
            screen.blit(img8, (25, 25))
        if animationlist[9] == 1:
            img9 = pygame.image.load(".png")
            screen.blit(img9, (25, 25))
        if animationlist[10] == 1:
            img10 = pygame.image.load(".png")
            screen.blit(img10, (25, 25))
        if animationlist[11] == 1:
            img11 = pygame.image.load(".png")
            screen.blit(img11, (25, 25))
        if animationlist[12] == 1:
            img12 = pygame.image.load(".png")
            screen.blit(img12, (25, 25))
        if animationlist[13] == 1:
            img13 = pygame.image.load(".png")
            screen.blit(img13, (25, 25))
        if animationlist[14] == 1:
            img14 = pygame.image.load(".png")
            screen.blit(img14, (25, 25))
        if animationlist[15] == 1:
            img15 = pygame.image.load(".png")
            screen.blit(img15, (25, 25))
        pygame.display.flip()

def yesno(inputed):
    pygame.event.get()
    textput_wrap=textwrap.wrap(inputed,65)
    while yess==False and noo==False:
        pygame.event.get()
        if pygame.key.get_pressed()[pygame.K_x]==1:
            sys.exit()
        screen.fill(BLACK)
        draw(100)
        for i in range(len(textput_wrap)):
            text_printer(i,textput_wrap)
        pygame.event.get()
        if pygame.key.get_pressed()[pygame.K_y]:
            yess=True
        elif pygame.key.get_pressed()[pygame.K_n]:
            noo=True
        pygame.display.flip()


clock = pygame.time.Clock()

#The story code goes here
text_intro= "You wake up with little recollection of who you are. Your surroundings are unfamiliar. Before you are four costumes, each promising to endow you with a new identity. Which do you choose? (1/2/3/4)"
    #class text 
textstealth_chose="You choose Frankina of the Stealth class. You check your pockets, finding a ninja star and an amulet that seems valuable. You hang the amulet around your neck."
textstrength_chose="You choose Farra of the Strength class. You check your pockets, finding a mysterious potion and an amulet that seems valuable. You hang the amulet around your neck."
textmagic_chose= "You choose Asenath of the Magic class. You check your pockets, finding a philosopher’s stone and an amulet that seems valuable. You hang the amulet around your neck."
textcharisma_chose= "You choose Tempest of the Charisma class. You check your pockets, finding a magic dictionary and an amulet that seems valuable. You hang the amulet around your neck."
    
stealth_mugging = "With your swiftness and ability to dodge oncoming punches from attackers, you evade the attackers and break into a sprint, leaving them far behind."
strength_mugging = "With your impeccable strength and intimidation, you overpower the mugger and move on your way, each step increasing the distance between you and their prone forms."
magic_mugging = "You panic, doubtful of your ability to defeat the attackers. To your surprise and relief, the philosopher’s stone begins to glow in your pocket, surely a sign of your nascent magical powers. Before you get a chance to do anything, however, the reprobates overpower you. As they drag you along with them, you hear something about a tavern and… a witch hunt? No, surely not."
charisma_mugging = "You know you’re not the strongest person around, but words can be powerful too. So you insinuate that you possess powerful magic, thinking that’ll scare the attackers off. But if anything, that only seems to spur them on, and the reprobates overpower you. As they drag you along with them, you hear something about a tavern and… a witch hunt? No, surely not. You’re innocent!"
    

    #main text
main_mugging= "After walking for some time along a path that leads through a heavily forested area, you begin to feel uneasy. Suddenly, two menacing figures jump out from among the foliage, blocking your way forward."
main_tavern ="As you keep walking, you see a small light in the distance. You keep walking, and eventually you are close enough to see that the light is emanating from the window of a small establishment, which you decide to enter. It turns out to be a tavern, its brightly lit interior brimming with rowdy patrons who have claimed nearly every spot at the rough-hewn wooden tables and bar. You scan the room and identify only two open seats; do you choose to sit at the bar or the table in the corner? (bar/table?)"
main_tablestealth= "You head over to the table in the far corner of the room. After introducing yourself to the people in your vicinity, you order a hearty meal. They ask about your dangerous travels and you explain that you have seen more of the world than you ever wished to, fearsome fauna and threatening terrain. Impressed, they tell you that in a nearby castle lives a dragon, and that it has been terrorizing this town for years. “You seem up for an adventure!” the woman to your left declares. “And there’s a dragon that needs slaying, a bounty on its head that needs claiming. What do you say?” You pause to consider. (y/n?)"
main_tablestealth_yes= " “Why not?” you hear yourself saying. You wouldn’t mind an influx of money. You linger for a while longer, then pay for your food and head out the door to begin the long journey to the castle."
main_tablestealth_no = " “I think not!” you tell them. The topic changes, and you while away the night with the other tavern-goers in a blur of drinks and merriment. After some time, the woman across from you makes a comment of a polemic nature. You take offense and respond indignantly. She challenges you to a fight with the condition that the loser must fight the dragon. Of course, you lose. In your defense, you’re not at your stealthiest right now. Gathering your wounded pride and your meager belongings, you leave the tavern and begin the long journey to the castle."
main_tablestrength= "You head over to the table in the far corner of the room. After introducing yourself to the people in your vicinity, you order a hearty meal. They admire your armour and ask you about your travels. You explain that you have seen more of the world than you ever wished to, fearsome fauna and threatening terrain. Before long, you are the talk of the tavern, and everyone seems to have crowded around your table. They tell you about the dragon that terrorizes their town, offering you riches for its defeat. Under the pressure of the crowd, there’s no answer you can give but yes.  You leave the tavern with their indistinct, supportive shouts at your back. It’ll be a long journey to the castle, but when you return, it’ll be as a hero. "

main_bar= "You stride to the bar and take the last seat. After introducing yourself to the bartender, you explain that you have traveled to many lands, seen many things. At a sudden pang of hunger, you order some food which you promptly devour. The bartender watches you with amusement. Belatedly, you realize that you don’t have any money. You sheepishly say as much when he asks for payment, thinking he might be lenient. Seemingly without any regard for what you just said, he tells you that a dragon has been terrorizing this town for many years. You look at him, baffled, until you realize his meaning. “Me? Kill a dragon? To pay for my food? You must be joking!” He stares at you solemnly, and you realize he’s dead serious. After an uncomfortable moment, you acquiesce. If the mission was that dangerous, he wouldn’t send you, right? Before you leave, he spots the golden amulet hanging around your neck. “That looks valuable,” he says. “Why don’t I hold on to it until you return?” Once more, you have no choice but to agree, and with that, he rudely shoves you out the door. Guess it’s time to kill a dragon. “Head to the castle!” he yells after you. Very helpful, isn’t he? "
main_magicwitch = ""
main_charismawitch =""
# -------- Main Program Loop -----------

pygame.event.get()
while pygame.key.get_pressed()[pygame.K_SPACE]==0:
    pygame.event.get()
    # --- Main event loop
    screen.fill(BLACK)
    draw(100)
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

    if stealth == True:
        screen.fill(BLACK)
        draw(100)
        imgstea = pygame.image.load("spr_and_bgs/Stealth_Bio.jpg")
        screen.blit(imgstea, (25, 25))
        text("CHOOSE STEALTH")
        textput_wrap = textwrap.wrap(textstealth_chose, 65)
        for i in range(len(textput_wrap)):
            text_printer(i, textput_wrap)
    elif strength == True:
        screen.fill(BLACK)
        draw(100)
        imgstre = pygame.image.load("spr_and_bgs/Strength_Bio.jpg")
        screen.blit(imgstre, (25, 25))
        text("CHOOSE STRENGTH")
        textput_wrap = textwrap.wrap(textstrength_chose, 65)
        for i in range(len(textput_wrap)):
            text_printer(i, textput_wrap)
    elif magic == True:
        screen.fill(BLACK)
        draw(100)
        imgmag = pygame.image.load("spr_and_bgs/Magic_Bio.jpg")
        screen.blit(imgmag, (25, 25))
        text("CHOOSE MAGIC")
        textput_wrap = textwrap.wrap(textmagic_chose, 65)
        for i in range(len(textput_wrap)):
            text_printer(i, textput_wrap)
    elif manipulation == True:
        screen.fill(BLACK)
        draw(100)
        imgmanip = pygame.image.load("spr_and_bgs/Charisma_Bio.jpg")
        screen.blit(imgmanip, (25, 25))
        text("CHOOSE MANIPULATION")
        textput_wrap = textwrap.wrap(textcharisma_chose, 65)
        for i in range(len(textput_wrap)):
            text_printer(i, textput_wrap)
    else:
        text("")
    pygame.display.flip()
    pygame.event.get()
    if pygame.key.get_pressed()[pygame.K_SPACE]==1:
        done=True


#Story
time.sleep(0.5)
mainstory(main_mugging,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

#mugging
time.sleep(0.5)
if stealth == True:
    mainstory(stealth_mugging,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
elif strength == True: 
    mainstory(strength_mugging,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
elif magic == True: 
    mainstory(magic_mugging,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
elif manipulation == True: 
    mainstory(charisma_mugging,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
time.sleep(0.5)

#tavern and witch hunt 
if stealth == True:
    #can use for y and n
    pygame.event.get()
    textput_wrap=textwrap.wrap(main_tavern,65)
    while table_choice==False and bar_choice==False:
        pygame.event.get()
        if pygame.key.get_pressed()[pygame.K_x]==1:
            sys.exit()
        screen.fill(BLACK)
        draw(100)
        for i in range(len(textput_wrap)):
            text_printer(i,textput_wrap)
        pygame.event.get()
        if pygame.key.get_pressed()[pygame.K_t]:
            table_choice=True
        elif pygame.key.get_pressed()[pygame.K_b]:
            bar_choice=True
        pygame.display.flip()
    if table_choice:
        mainstory(main_tablestealth, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif bar_choice:
        mainstory(main_bar, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

if strength == True:
    pygame.event.get()
    textput_wrap=textwrap.wrap(main_tavern,65)
    while table_choice==False and bar_choice==False:
        pygame.event.get()
        if pygame.key.get_pressed()[pygame.K_x]==1:
            sys.exit()
        screen.fill(BLACK)
        draw(100)
        for i in range(len(textput_wrap)):
            text_printer(i,textput_wrap)
        pygame.event.get()
        if pygame.key.get_pressed()[pygame.K_t]:
            table_choice=True
        elif pygame.key.get_pressed()[pygame.K_b]:
            bar_choice=True
        pygame.display.flip()
    
    if table_choice:
        yesno(main_tablestrength)

    elif bar_choice:
        mainstory(main_bar, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

elif magic == True: 
    mainstory(magic_mugging,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
elif manipulation == True: 
    mainstory(charisma_mugging,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
time.sleep(0.5)




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