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

fir= False 
sec = False 
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
    myfont=pygame.font.SysFont("monospace", 15)
    label=myfont.render(wrapped_text[textnumber],1,WHITE)
    screen.blit(label,(30,425+15*textnumber))

def text_printer_long(textnumber,wrapped_text):
    myfont=pygame.font.SysFont("monospace", 12)
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

def yesno(inputed, yeschoice, nochoice):
    pygame.event.get()
    textput_wrap=textwrap.wrap(inputed,65)
    yess=False
    noo=False
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
    if yess:
        time.sleep(0.5)
        mainstory(yeschoice, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

    elif noo:
        time.sleep(0.5)
        mainstory(nochoice, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])       

def tavern_choice(inputed,fir,sec,choice1,choice1_1,choice1_2):
    pygame.event.get()
    textput_wrap=textwrap.wrap(inputed,65)
    print(fir)
    print(sec)
    while fir==False and sec==False:
        pygame.event.get()
        if pygame.key.get_pressed()[pygame.K_x]==1:
            sys.exit()
        screen.fill(BLACK)
        draw(100)
        for i in range(len(textput_wrap)):
            text_printer(i,textput_wrap)
        pygame.event.get()
        if pygame.key.get_pressed()[pygame.K_t]:
            fir=True
        elif pygame.key.get_pressed()[pygame.K_b]:
            sec=True
        pygame.display.flip()
    if fir:
        time.sleep(0.5)
        yesno(choice1,choice1_1,choice1_2)
    elif sec:
        time.sleep(0.5)
        mainstory(main_barp1, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        time.sleep(0.5)
        mainstory(main_barp2, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])   

def choice(inputed,fir,sec,choice1, choice1p2, choice2, choice2p2):
    pygame.event.get()
    textput_wrap=textwrap.wrap(inputed,65)
    print(fir)
    print(sec)
    while fir==False and sec==False:
        pygame.event.get()
        if pygame.key.get_pressed()[pygame.K_x]==1:
            sys.exit()
        screen.fill(BLACK)
        draw(100)
        for i in range(len(textput_wrap)):
            text_printer(i,textput_wrap)
        pygame.event.get()
        if pygame.key.get_pressed()[pygame.K_t]:
            fir=True
        elif pygame.key.get_pressed()[pygame.K_b]:
            sec=True
        pygame.display.flip()
    if fir:
        time.sleep(0.5)
        mainstory(choice1, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        time.sleep(0.5)
        mainstory(choice1p2, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif sec:
        time.sleep(0.5)
        mainstory(choice2, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        time.sleep(0.5)
        mainstory(choice2p2, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])  


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
main_tablestrength= '''You head over to the table in the far corner of the room. 
After introducing yourself to the people in your vicinity, you order a hearty meal. 
They admire your armour and ask you about your travels. You explain that you have seen more of the world than you ever wished to, 
fearsome fauna and threatening terrain. Before long, you are the talk of the tavern, and everyone seems to have 
crowded around your table. They tell you about the dragon that terrorizes their town, offering you riches for its defeat. 
'''
main_tablestealthp2 = "Under the pressure of the crowd, there’s no answer you can give but yes.  You leave the tavern with their indistinct, supportive shouts at your back. It’ll be a long journey to the castle, but when you return, it’ll be as a hero."

main_barp1= "You stride to the bar and take the last seat. After introducing yourself to the bartender, you explain that you have traveled to many lands, seen many things. At a sudden pang of hunger, you order some food which you promptly devour. The bartender watches you with amusement. Belatedly, you realize that you don’t have any money. You sheepishly say as much when he asks for payment, thinking he might be lenient. Seemingly without any regard for what you just said, he tells you that a dragon has been terrorizing this town for many years."
main_barp2 = "You look at him, baffled, until you realize his meaning. “Me? Kill a dragon? To pay for my food? You must be joking!” He stares at you solemnly, and you realize he’s dead serious. After an uncomfortable moment, you acquiesce. If the mission was that dangerous, he wouldn’t send you, right? Before you leave, he spots the golden amulet hanging around your neck. “That looks valuable,” he says. “Why don’t I hold on to it until you return?” Once more, you have no choice but to agree, and with that, he rudely shoves you out the door. Guess it’s time to kill a dragon. “Head to the castle!” he yells after you. Very helpful, isn’t he? "
main_magicwitch = '''After an interminably long time, your attackers deposit you roughly in front of the tavern. 
You are terrified to see a pyre set up outside. People flood out of the building, drinks in their hands and malice in their eyes. 
They start to herd you towards your fiery fate when a man barrels through the mob and tells you to run. You both dash away in the 
confusion, stopping only once there is no danger that they might find you. “Why did you save me?” you ask, wheezing. You’re more out 
of shape than you thought. “You are immensely powerful,” says the mysterious man. '''
main_magicwitchp2= ''' “There is a dragon that resides in a castle nearby,
 and it has brought nothing but destruction to this town. You must kill it.” // “Me?” you sputter. “Kill a dragon?” // “You have no 
 choice,” he impresses. “Unless you want the mob to conveniently find you again.” // “And here I thought you were a good person,” 
 you say, stung. “But yes, I will try to kill this dragon.” // He asks for your amulet as collateral, which annoys you even more, 
 but you hand it over. He did save your life, after all. Ready to leave him behind, you begin your long journey to slay the dragon.'''
main_charismawitch ='''After an interminably long time, your attackers deposit you roughly in front of the tavern. 
You are terrified to see a pyre set up outside. People flood out of the building, drinks in their hands and malice in their eyes. 
They start to herd you towards your fiery fate, but you stop in your tracks, hoping to buy yourself enough time to talk them out of 
burning you. “Move along,” a scowling man with blood stains on his clothing grumbles. // “No,” you say loudly, trying to suppress the
 trembling in your voice.  
'''
main_charismawitchp2 = '''“Listen, I may be a witch, and you may hate me for that, but I am powerful. Surely my magic could be of some
  use to you.” // The silence is painful, and you think they’ll go ahead and kill you all the same. Then the man speaks. “Actually, 
  there is something you can do for us, witch. Slay the dragon that lives in the castle, and we will let you go on your way.” // “All 
  right,” you say. “I accept your terms.” // Probable death is better than certain death, right? You turn to leave when you hear the 
  man’s voice again. “One more thing. The amulet.” '''
main_charismawitchp3= '''You hand it over readily, not willing to risk him rescinding the offer. 
  Terrified, you take the first steps of what will likely be a fatal journey.'''
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
print("here")

#tavern and witch hunt 
if stealth == True:
    tavern_choice(main_tavern,fir,sec,main_tablestealth,main_tablestealth_yes,main_tablestealth_no)

if strength == True:
    choice(main_tavern, fir, sec, main_tablestrength, main_tablestealthp2, main_barp1, main_barp2)

elif magic == True: 
    mainstory(main_magicwitch ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    time.sleep(0.5)
    mainstory(main_magicwitchp2 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    # time.sleep(0.5)
    # # mainstory(main_magicwitchp3 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
elif manipulation == True: 
    mainstory(main_charismawitch,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    time.sleep(0.5)
    mainstory(main_charismawitchp2 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    time.sleep(0.5)
    mainstory(main_charismawitchp3 ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
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