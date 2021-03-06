import pygame, time, sys, textwrap

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (107, 251, 216)
MAGENTA = (225, 41, 124)

pygame.init()

# Set the width and height of the screen [width, height]
length = 700
width = 600
size = (length, width)
screen = pygame.display.set_mode(size)

green_x = 20
white_x = 25
green_l = 660
white_l = 650

fir = False
sec = False
yess = False
noo = False
bar_choice = False
table_choice = False
stealth = False
strength = False
magic = False
manipulation = False
hp = 100

pygame.display.set_caption("Run of Infringement")

# Loop until the user clicks the close button.
done = False


# Functions
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


def text_printer(textnumber, wrapped_text):
	myfont = pygame.font.SysFont("monospace", 15)
	label = myfont.render(wrapped_text[textnumber], 1, WHITE)
	screen.blit(label, (30, 425 + 15 * textnumber))


def text_printer_long(textnumber, wrapped_text):
	myfont = pygame.font.SysFont("monospace", 12)
	label = myfont.render(wrapped_text[textnumber], 1, WHITE)
	screen.blit(label, (30, 425 + 15 * textnumber))

def mainstorydif(textput, image):
    pygame.event.get()
    textput_wrap = textwrap.wrap(textput, 65)
    while pygame.key.get_pressed()[pygame.K_SPACE] == 0:
        pygame.event.get()
        if pygame.key.get_pressed()[pygame.K_x] == 1:
            sys.exit()
        screen.fill(BLACK)
        draw(100)
        tavern_stealth = pygame.image.load(image)
        screen.blit(tavern_stealth, (25, 25))
        for i in range(len(textput_wrap)):
            text_printer(i, textput_wrap)
        pygame.display.flip()


def yesno(inputed, cit, yeschoice, nochoice, a, b):
	pygame.event.get()
	textput_wrap = textwrap.wrap(inputed, 65)
	yess = False
	noo = False
	while yess == False and noo == False:
		pygame.event.get()
		if pygame.key.get_pressed()[pygame.K_x] == 1:
			sys.exit()
		screen.fill(BLACK)
		draw(100)
		tavern_stealth = pygame.image.load(cit)
		screen.blit(tavern_stealth, (25, 25))
		for i in range(len(textput_wrap)):
			text_printer(i, textput_wrap)
		pygame.event.get()
		if pygame.key.get_pressed()[pygame.K_y]:
			yess = True
		elif pygame.key.get_pressed()[pygame.K_n]:
			noo = True
		pygame.display.flip()
	if yess:
		time.sleep(0.5)
		mainstorydif(yeschoice, a)

	elif noo:
		time.sleep(0.5)
		mainstorydif(nochoice, b)


def tavern_choice(inputed, fir, sec, choice1, choice1_1, choice1_2):
	pygame.event.get()
	textput_wrap = textwrap.wrap(inputed, 65)
	fir=False
	sec=False
	print(fir)
	print(sec)
	while fir == False and sec == False:
		pygame.event.get()
		if pygame.key.get_pressed()[pygame.K_x] == 1:
			sys.exit()
		screen.fill(BLACK)
		draw(100)
		tavern_img = pygame.image.load("tavern_walkup.jpg")
		screen.blit(tavern_img, (25, 25))
		pygame.event.get()
		for i in range(len(textput_wrap)):
			text_printer(i, textput_wrap)
		pygame.event.get()
		if pygame.key.get_pressed()[pygame.K_t]:
			fir = True
		elif pygame.key.get_pressed()[pygame.K_b]:
			sec = True
		pygame.display.flip()
	if fir:
		time.sleep(0.5)
		yesno(choice1,"tavern_table_stealth.jpg", choice1_1, choice1_2, "tavern_table_stealth.jpg", "tavern_table_stealth.jpg")
	elif sec:
		time.sleep(0.5)
		mainstorydif(main_barp1, "tavern_barrr.jpg")
		time.sleep(0.5)
		mainstorydif(main_barp2, "tavern_bar_stealth.jpg")


def choice(inputed, ab, fir, sec, choice1, choice1p2, choice1p3, choice2, choice2p2, choice2p3, a, b, c, d, e, f):
	pygame.event.get()
	textput_wrap = textwrap.wrap(inputed, 65)
	fir=False
	sec=False
	while fir == False and sec == False:
		pygame.event.get()
		if pygame.key.get_pressed()[pygame.K_x] == 1:
			sys.exit()
		screen.fill(BLACK)
		draw(100)
		tavern_img = pygame.image.load(ab)
		screen.blit(tavern_img, (25, 25))
		for i in range(len(textput_wrap)):
			text_printer(i, textput_wrap)
		pygame.event.get()
		if pygame.key.get_pressed()[pygame.K_t]:
			fir = True
		elif pygame.key.get_pressed()[pygame.K_b]:
			sec = True
		pygame.display.flip()
	if fir:
		time.sleep(0.5)
		mainstorydif(choice1, a)
		time.sleep(0.5)
		mainstorydif(choice1p2, b)
	elif sec:
		time.sleep(0.5)
		mainstorydif(choice2, c)
		time.sleep(0.5)
		mainstorydif(choice2p2, d)

# def castle(inputed, ):

clock = pygame.time.Clock()

# The story code goes here
text_intro = "You wake up with little recollection of who you are. Your surroundings are unfamiliar. Before you are four costumes, each promising to endow you with a new identity. Which do you choose? (1/2/3/4)"
# class text
textstealth_chose = "You choose Frankina of the Stealth class. You check your pockets, finding a ninja star and an amulet that seems valuable. You hang the amulet around your neck."
textstrength_chose = "You choose Farra of the Strength class. You check your pockets, finding a mysterious potion and an amulet that seems valuable. You hang the amulet around your neck."
textmagic_chose = "You choose Asenath of the Magic class. You check your pockets, finding a philosopher’s stone and an amulet that seems valuable. You hang the amulet around your neck."
textcharisma_chose = "You choose Tempest of the Charisma class. You check your pockets, finding a dagger and an amulet that seems valuable. You hang the amulet around your neck."

stealth_mugging = "With your swiftness and ability to dodge oncoming punches from attackers, you evade the attackers and break into a sprint, leaving them far behind."
strength_mugging = "With your impeccable strength and intimidation, you overpower the mugger and move on your way, each step increasing the distance between you and their prone forms."
magic_mugging = "You panic, doubtful of your ability to defeat the attackers. To your surprise and relief, the philosopher’s stone begins to glow in your pocket, surely a sign of your nascent magical powers. Before you get a chance to do anything, however, the reprobates overpower you. As they drag you along with them, you hear something about a tavern and… a witch hunt? No, surely not."
charisma_mugging = "You know you’re not the strongest person around, but words can be powerful too. So you insinuate that you possess powerful magic, thinking that’ll scare the attackers off. But if anything, that only seems to spur them on, and the reprobates overpower you. As they drag you along with them, you hear something about a tavern and… a witch hunt? No, surely not. You’re innocent!"

# main text
main_mugging = "After walking for some time along a path that leads through a heavily forested area, you begin to feel uneasy. Suddenly, several menacing figures jump out from among the foliage, blocking your way forward."
main_tavern1 = "As you keep walking, you see a small light in the distance. You keep walking, and eventually you are close enough to see that the light is emanating from the window of a small establishment, which you decide to enter."
main_tavern2 = " It turns out to be a tavern, its brightly lit interior brimming with rowdy patrons who have claimed nearly every spot at the rough-hewn wooden tables and bar. You scan the room and identify only two open seats; do you choose to sit at the bar or the table in the corner? (b/t)"

main_tablestealth1 = "You head over to the table in the far corner of the room. After introducing yourself to the people in your vicinity, you order a hearty meal. They ask about your dangerous travels and you explain that you have seen more of the world than you ever wished to, fearsome fauna and threatening terrain."
main_tablestealth2 = " Impressed, they tell you that in a nearby castle lives a dragon, and that it has been terrorizing this town for years. “You seem up for an adventure!” the woman to your left declares. “And there’s a dragon that needs slaying, a bounty on its head that needs claiming. What do you say?” You pause to consider. (y/n)"

main_tablestealth_yes1 = "“Why not?” you hear yourself saying. You wouldn’t mind an influx of money. You linger for a while longer, then pay for your food and head out the door to begin the long journey to the castle."

main_tablestealth_no1 = " “I think not!” you tell them. The topic changes, and you while away the night with the other tavern-goers in a blur of drinks and merriment. "
main_tablestealth_no2 = "After some time, the woman across from you makes a comment of a polemic nature. You take offense and respond indignantly. She challenges you to a fight with the condition that the loser must fight the dragon."
main_tablestealth_no3 = "Of course, you lose. In your defense, you’re not at your stealthiest right now. Gathering your wounded pride and your meager belongings, you leave the tavern and begin the long journey to the castle."

main_tablestrength1 = "You head over to the table in the far corner of the room.After introducing yourself to the people in your vicinity, you order a hearty meal.They admire your armour and ask you about your travels. You explain that you have seen more of the world than you ever wished to,fearsome fauna and threatening terrain."
main_tablestrength2 = "Before long, you are the talk of the tavern, and everyone seems to have crowded around your table. They tell you about the dragon that terrorizes their town, offering you riches for its defeat. Under the pressure of the crowd, there’s no answer you can give but yes."
main_tablestrength3 = "You leave the tavern with their indistinct, supportive shouts at your back. It’ll be a long journey to the castle, but when you return, it’ll be as a hero."

main_bar1 = "You stride to the bar and take the last seat. After introducing yourself to the bartender, you explain that you have traveled to many lands, seen many things. At a sudden pang of hunger, you order some food which you promptly devour. The bartender watches you with amusement."
main_bar2 = "Belatedly, you realize that you don’t have any money. You sheepishly say as much when he asks for payment, thinking he might be lenient. Seemingly without any regard for what you just said, he tells you that a dragon has been terrorizing this town for many years."
main_bar3 = "You look at him, baffled, until you realize his meaning. “Me? Kill a dragon? To pay for my food? You must be joking!”"
main_bar4 = "He stares at you solemnly, and you realize he’s dead serious. After an uncomfortable moment, you acquiesce. If the mission was that dangerous, he wouldn’t send you, right?"
main_bar5 = "Before you leave, he spots the golden amulet hanging around your neck. “That looks valuable,” he says. “Why don’t I hold on to it until you return?”"
main_bar6 = "Once more, you have no choice but to agree, and with that, he rudely shoves you out the door. Guess it’s time to kill a dragon. “Head to the castle!” he yells after you. Very helpful, isn’t he?"

main_magicwitch1 = "After an interminably long time, your attackers deposit you roughly in front of the tavern. You are terrified to see a pyre set up outside. People flood out of the building, drinks in their hands and malice in their eyes."
main_magicwitch2 = "They start to herd you towards your fiery fate when a man barrels through the mob and tells you to run. You both dash away in the confusion, stopping only once there is no danger that they might find you."
main_magicwitch3 = "“Why did you save me?” you ask, wheezing. You’re more out of shape than you thought."
main_magicwitch4 = "“You are immensely powerful,” says the mysterious man. “There is a dragon that resides in a castle nearby, and it has brought nothing but destruction to this town. You must kill it.”"
main_magicwitch5 = "“Me?” you sputter. “Kill a dragon?”"
main_magicwitch6 = "“You have no choice,” he impresses. “Unless you want the mob to conveniently find you again.”"
main_magicwitch7 = "“And here I thought you were a good person,” you say, stung. “But yes, I will try to kill this dragon.”"
main_magicwitch8 = "He asks for your amulet as collateral, which annoys you even more, but you hand it over. He did save your life, after all. Ready to leave him behind, you begin your long journey to slay the dragon."

main_charismawitch1 = "After an interminably long time, your attackers deposit you roughly in front of the tavern. You are terrified to see a pyre set up outside. People flood out of the building, drinks in their hands and malice in their eyes."
main_charismawitch2 = "They start to herd you towards your fiery fate, but you stop in your tracks, hoping to buy yourself enough time to talk them out of burning you. “Move along,” a scowling man with blood stains on his clothing grumbles."
main_charismawitch3 = "“No,” you say loudly, trying to suppress the trembling in your voice. “Listen, I may be a witch, and you may hate me for that, but I am powerful. Surely my magic could be of some use to you.”"
main_charismawitch4 = "The silence is painful, and you think they’ll go ahead and kill you all the same. Then the man speaks. “Actually, there is something you can do for us, witch. Slay the dragon that lives in the castle, and we will let you go on your way.”"
main_charismawitch5 = "“All right,” you say. “I accept your terms.” Probable death is better than certain death, right?"
main_charismawitch6 = "You turn to leave when you hear the man’s voice again. “One more thing. The amulet.”"
main_charismawitch7 = "You hand it over readily, not willing to risk him rescinding the offer. Terrified, you take the first steps of what will likely be a fatal journey."

main_castle1 = "You can see the castle in the distance where it sits smugly atop a tall hill. Beneath your feet is a dusty path, which you decide to follow for now, though you’re not sure if it actually leads to the castle. If it doesn’t, well, you’ll deal with that later."
main_castle2 = "As you walk further and further, the tavern shrinks in your vision until it it seems like an insignificant speck of light. But that insignificant speck is why you’re here."
main_castle3 = "A shiver of fear runs through you at the reminder of what awaits you at your destination. Why were you foolish enough to agree to this? Well, turning back is not an option. You will keep going, and you will slay that dragon. Probably. Maybe."
main_castle4 = "You walk for what seems like hours. The stars shine brightly against the dark canvas of the sky, and you let yourself bask in the beautiful sight for a moment."
main_castle5 = "Then you have to bring your attention back to your surroundings, because before you is a deep canyon into which the path gradually slopes. Something in its very nature seems sinister and menacing, as though this valley might end you before the dragon does."
main_castle6 = "But to circumvent the ravine would prolong your journey, when you just want this ordeal to be over as soon as possible. Plus, you have to conserve your strength for the real fight. So the canyon it is."

main_castle_stealth1 = "With your first step, you know this was a bad idea. You hear a slight splashing noise, and look down to see a small puddle. No reason to worry. But as you continue, you begin to notice a thin layer of water dampening the soles of your shoes."
main_castle_stealth2 = "And the water keeps rising. Soon you’re wading through it, slowing your forward progress to a crawl. You’re not sure where it’s coming from, but it’s an inconvenience nonetheless.  Also, you don’t really know how to swim. That might be a problem."
main_castle_stealth3 = "You slosh through the water for as long as you can until it threatens to envelop you entirely. Your breath comes in small, panicked spurts, and then not at all. Is this the moment you die?"
main_castle_stealth4 = "You kick your feet at the canyon floor to lift your head for one last glimpse at the world, and instead spot a miracle. A dead tree branch, floating languidly on the water’s surface. You reach for it and barely manage to hold on."
main_castle_stealth5 = "You propel yourself to the end of the ravine by kicking your legs out behind you, and it is a such a relief once you stand upon solid ground again. There is still the dragon to fight, of course, but you expunge the thought from your mind until you stand before the doors of the castle. "

main_castle_strength1 = "With your first step, you know this was a bad idea. The night seems even darker from inside the ravine, everything cast in shadows that lurk and linger with a menacing import. But even worse is when the weather-worn stone walls tower their highest above you, blotting out every source of brightness."
main_castle_strength2 = "You don’t want to admit it, but you might be a little scared of the dark."
main_castle_strength3 = "Also, you keep bumping into boulders and tripping over small rocks that litter the canyon floor."
main_castle_strength4 = "When you finally make it out, you attend to your numerous scrapes and gashes. You turn back to look at the geographical feature that has caused you so much turmoil, and from here, you feel a little foolish for being so weak."
main_castle_strength5 = "You also feel a little lightheaded, having lost a lot of blood, but after a short rest, you stagger the rest of the way to the castle, stopping right before its grand doors."

main_castle_m1 = "With your first step, you know this was a bad idea. Nothing bad has occurred yet, but you’re pretty sure something will."
main_castle_m2 = "Things are too oddly sanguine for the first few minutes, but then a loud crashing noise shatters the fraught silence. You crane your head over your shoulder to investigate."
main_castle_m3 = "A massive boulder sits squarely where you were standing just a moment ago, and you say a thousand thanks that you left the tavern when you did, that you weren’t walking any slower."
main_castle_m4 = "But you must be on your guard now, for what happened once can happen again. You scan the tops of the canyon walls for any more plummeting rocks, and spot a shadowy figure. Someone must have followed you from the tavern."
main_castle_m5 = "You watch detachedly as he pushes another boulder to the edge of the ravine. Then you realize it’s meant for you. Meant to kill you. You break into a run, narrowly dodging rocks of all sizes that are hurled at you."
main_castle_m6 = "One grazes your shoulder painfully, and you want to collapse right there. You’re bleeding and out of breath, but you keep sprinting, out of the canyon and onwards to the castle. Whoever is trying to kill you will not succeed, not today or ever."
main_castle_m7 = "You reach the castle, and, looking around to ensure the man is nowhere near, sit down in front of its grand doors. You just need a moment to tend to your wound. And catch your breath."

main_incastle1 = "You linger outside the castle as long as you can, trying to steel yourself for the tremendous task that of slaying a dragon that may very well slay you. But eventually you convince yourself that it will do you no good to wait any longer, so you wrest open the doors and enter the dragon’s abode."
main_incastle2 = "You wander around for a bit, and when you see another set of doors as forbidding and ornate as those you passed through earlier, you know your foe can be nowhere else but inside."

stealth_dragon1 = "When you enter the cavernous chamber, you see the dragon asleep in the corner atop a pile of gold. You inch quietly towards it, hoping to catch it unaware, but your foot accidentally catches on a stray gold coin that sounds loudly as it careens across the cold floor."
stealth_dragon2 = "The dragon lifts its head slowly to stare at you. It uncurls itself from its sleeping position and bats its wings, circling the room from above."
stealth_dragon3 = "You nimbly dodge deadly spurts of fire, and when it pauses for a second, you take out your dagger and launch it at the dragon’s underbelly. A line of blood appears where the dagger grazes, but unfortunately, ‘tis but a flesh wound."
stealth_dragon4 = "The dragon continues its blazing attacks, not weakened in the slightest. In another opportune moment, you take out your ninja star, your last weapon, and eye the glimmering chandelier. If your timing and aim is perfect, you might be able to bring the dragon down with it. Or you could aim the star directly at the dragon. What do you do? (chandelier(t)/dragon(b))"

stealth_dragon_dragon1 = "You carefully send the ninja star spinning towards the dragon’s heart, but the beast twists to the left just as the weapon leaves your hand. The star glances harmlessly off its side and lands on the opposite side of the room."
stealth_dragon_dragon2 = "You stare at it helplessly, trembling with the knowledge that this is likely your final moment. It is. Though you try to dodge the next inferno sent your way, the last sensation you ever experience is that of being engulfed in flames. THE END."

stealth_dragon_chand1 = "You carefully aim the ninja star at the chain attaching the chandelier to the ceiling. One link breaks, but that is all it takes for the decorative collection of glass shards to descend upon the dragon and send him crashing to the floor. You are in disbelief at what you’ve accomplished."
stealth_dragon_chand2 = "There are so many coins littering the floor, and you shouldn’t let them go to waste, so you start gathering them up in your arms.Then the dragon awakens sluggishly. You startle, and coins spill everywhere."
stealth_dragon_chand3 = "You start running before it gets the chance to kill you again, but stop when you realize that you can’t return to the tavern without proof of its death. Searching around, you spot an iridescent scale near the dragon, which you sprint to pick up before leaving."
stealth_dragon_chand4 = "You can hear the dragon roaring even after you exit the castle, but thankfully it’s too weak to actually pursue you."

strength_dragon = "When you enter the cavernous chamber, you see the dragon asleep in the corner atop a pile of gold. You could try killing it as it sleeps, but that seems dishonorable. You could also wake it up so that you can fight on equal terms, but that’s not an enticing option either. What do you do? (sleep(t)/wake(b)?"

strength_dragon_sleep1 = "You creep towards the dragon, guilt rising within you. This really doesn’t seem like the right thing to do. As you get closer, you hold your sword in front of you, steadying yourself for the kill. Then the dragon cracks an eye open. You freeze, but don’t lower the sword."
strength_dragon_sleep2 = "It lifts its head and startles you by speaking. “Don’t kill me,” it says calmly, its voice low and gravelly."
strength_dragon_sleep3 = "“Why not?” you ask, trembling. “Many innocent people have perished because of you.”"
strength_dragon_sleep4 = "“True, but I could easily stop,” it replies. “And if you choose not to kill me, I might be convinced to.”"
strength_dragon_sleep5 = "Something seems off—the dragon doesn’t seem as helpless as it’s acting—but you agree. The dragon shakes its head, causing an iridescent scale to fall loose."
strength_dragon_sleep6 = "“Proof,” it says, and you could swear it’s smirking at you, “of your heroic deed.”"
strength_dragon_sleep7 = "You pick it up warily, nod at the dragon, and turn around to leave. You walk triumphantly out the castle, when suddenly the dragon swoops you up in its claws. It flies along the path you took to get here, and you figure the dragon wants to spare you of the long walk back."
strength_dragon_sleep8 = "When you see the tavern below you, you realize that your mission will have been for nothing if the townspeople look up and see the dragon alive and well."
strength_dragon_sleep9 = "“What are you doing?” you yell, trying to be heard over the howling wind."
strength_dragon_sleep10 = "“You didn’t think I would be that easily stopped, did you?” the dragon growls."
strength_dragon_sleep11 = "Then it releases an intense wave of fire that razes the town to nothing more than flaming wood and detritus. You close your eyes and silently apologize to everyone who died because of your naivete. THE END."

strength_dragon_wake1 = "You yell unintelligibly until the dragon wakes up, and when it does, you can’t deny that you’re a little terrified. You brandish your sword in the air, and it circles you in the air. When it swoops low to snap you up in its jaws, you swing your sword across its neck with every bit of your might, and to your surprise, it slices clean through."
strength_dragon_wake2 = "You stand back, stunned at your own strength, and feel a little ashamed for having slain such a mighty creature, for having slain any creature at all. Then you remember the damage it inflicted upon that town, and the guilt is mostly gone." 
strength_dragon_wake3 = "One of the dragon’s iridescent scales has fallen loose. You pick it up as proof of what you accomplished today, walking away with a slightly heavier heart. No one said being a hero was easy."

magic_dragon1 = "When you enter the cavernous chamber, the dragon sits upright and fixes you to your spot with its unnerving stare, as though it has been waiting for you all this time." 
magic_dragon2 = "The situation is doing nothing to soothe your frayed nerves. You spent the entire journey stewing in terrified anticipation—you’re not ready to die, but your magic powers are so erratic and uncontrollable that you wish you had something else to rely on."
magic_dragon3 = "But here you are, standing before the dragon, hoping for a miracle. Or you could flee. It’s probably not too late for that, and even if it makes you a coward, at least you will avoid death. What do you do? (fight(t)/flee(b))"

magic_dragon_fight1 = "You decide to stand your ground and keep your promise to your savior. If you die, it will be with honor."
magic_dragon_fight2 = "The dragon takes flight, circling the room from above. It sends ferocious spurts of fire at you that you manage to dodge. One blast comes especially close, singeing your clothes and skin. But now you can feel the magic surging in your veins now, powerful and impatient; the intense danger of that moment must have triggered its return from dormancy."
magic_dragon_fight3 = "Instinctively, you hold up your philosopher’s stone, and out of it shoots a bright bolt of light that seeks out the dragon and slams it forcefully into the far wall. Its limp form slides to the ground, and it remains there, slumped. Several iridescent scales scatter across the floor."
magic_dragon_fight4 = "You approach the dragon tentatively, not sure whether it’s dead or merely unconscious. As you get closer, you can see clearly that it remains still, its belly not swelling with the intake of breath."
magic_dragon_fight5 = "An almost tangible wave of guilt hits you at having ended the life of a magnificent beast with one swift blow. You push that sentiment aside and pick up a single scale as proof of what you did."
magic_dragon_fight6 = "You look at the dragon one last time, then turn away with a heavy heart and begin the journey back."

magic_dragon_flee1 = "You turn around and run away. You really can’t do this. That man back at the tavern may have saved you, but he had no right to ask this of you. Once outside of the castle, you see the very person you were silently berating."
magic_dragon_flee2 = "“Hello,” he says, sounding very much like cat toying with its prey."
magic_dragon_flee3 = "“What are you doing here?” you ask, indignant. If he followed you all the way here, why couldn’t he have helped you kill the dragon?"
magic_dragon_flee4 = "His next words cut you deep. “Forgive me if I didn’t trust you to complete this mission. And as you can see, I was right.”"
magic_dragon_flee5 = "“Then why ask me at all?”"
magic_dragon_flee6 = "“You see, this was a test. I am a wizard, and I was hoping to find a honorable apprentice in you,” he says."
magic_dragon_flee7 = "“Really?” you ask, taken aback."
magic_dragon_flee8 = "He smirks. “No.” He takes out a gleaming dagger and strikes a fatal blow to your person. THE END. (Press x to exit game)"

manip_dungeon1 = "When you enter the cavernous chamber, the dragon sits upright and fixes you to your spot with its unnerving stare, as though it has been waiting for you all this time."
manip_dungeon2 = "The situation is doing nothing to soothe your frayed nerves. You’ve spent the entire journey stewing in terrified anticipation, and to have this moment upon you now is nothing short of overwhelming. Your only weapons are your words and your dagger, and though neither seem suited to this situation, they’re all you have."
manip_dungeon3 = "“Who are you?” the dragon tries to snarl in an oddly high-pitched voice."
manip_dungeon4 = "You suppress nervous laughter and quickly formulate a response. You see two viable options: intimidation or ingratiation. Which do you choose? (intimidation(t)/ingratiation(b))"

manip_dungeon_int1 = "“I am a renowned dragon slayer,” you say sonorously. “And if you refuse to cease inflicting injury after injury upon the poor town nearby, I would advise you to prepare for your end.”"
manip_dungeon_int2 = "You expect the dragon to say something, anything, but it just stands there, impassive. Then it sniffles, and a single tear falls to the ground. It scorches a hole straight through the floor. Um, what is going on, exactly?"
manip_dungeon_int3 = "“My father… he was the one who killed all those people, and now… he’s gone.” It glares at you, if such a thing is possible for a dragon. “At the hands of a dragon slayer like you.”"
manip_dungeon_int4 = "Oh. Intimidation was a really bad idea."
manip_dungeon_int5 = "“It appears that I was mistaken,” you say, inching backwards. “Now, if you don’t mind, I’ll just leave you in peace.”"
manip_dungeon_int6 = "“I don’t think so,” it hisses. The last thing you see is the scorched floor where the acidic tear fell, and then you are engulfed in flames. THE END."

manip_dungeon_ingrate1 = "“I’m a huge fan of yours!” you exclaim, with as much enthusiasm as you can muster for a murderer. “I admire the way you can raze a village with a single fiery exhale, how you upend lives with such ease. So I wanted to meet you in person.” Hopefully your words paint you as a slightly crazed devotee and not a sycophant."
manip_dungeon_ingrate2 = "“Is that right?” says the dragon, sounding flattered. “Well, thank you!” Is your crazy scheme actually working?"
manip_dungeon_ingrate3 = "“Of course! But you know what? There’s a tavern nearby where they don’t appreciate your work quite as much, and as someone who wants the best for you, I would humbly suggest that you take your art elsewhere.” You hold your breath, wishing for the best."
manip_dungeon_ingrate4 = "“I suppose you might be right,” the dragon says after a moment."
manip_dungeon_ingrate5 = "“Wonderful! I promise you won’t regret it,” you say. “Oh, and before I leave, I wonder if I might have one of your lovely iridescent scales as a souvenir?” As proof of its “death.”"
manip_dungeon_ingrate6 = "It agrees easily, scattering a few loose with a shake of its head. You pick one up and thank the dragon vigorously, then exit the castle after exchanging a few pleasantries. You feel a bit sleazy for deceiving the dragon, especially because it seems so lonely, but that doesn’t diminish how happy you are that you achieved your mission without any killing."

main_tavern_again = "After a long, arduous trip back from the castle, during which you decide that nothing can make you pass through that valley again, you arrive back at the tavern that has caused you so much misery, hopefully for the last time."

main_bar_again1 = "You make your way to the bar, pushing your way through swarms of people. You are here for one reason, and one reason alone: to reclaim your collateral from the bartender. But when you ask him to return the amulet, he smirks maliciously, holding it out of your reach."
main_bar_again2 = "“You actually thought you were going to get this back? No way. A weakling like you could never have killed the dragon.”"
main_bar_again3 = "You pull out the dragon's scale and show it to him. His face pales. “How did you get that?” he sputters."
main_bar_again4 = "“This weakling,” you snarl, light glinting off your armor, “killed a dragon. Do you really want to make her angry?”"
main_bar_again5 = "“No!” he practically yelps, and shoves the amulet into your hands."
main_bar_again6 = "“Thank you,” you say, smiling sweetly. When you turn around to leave this godforsaken tavern behind for good, an enormous wave of people stands in your way. You hope that they're not angry at you for intimidating the bartender, because he got what he deserved."
main_bar_again7 = "Then their faces light up with smiles. “All hail the dragon-slayer!” they shout in unison. They herd you back to the bar, where they tell the sulking bartender to serve you a drink. He doesn't even try to refuse."
main_bar_again8 = "You regale the admiring crowd with stories of your brave exploits, fudging the truth just a little bit. They don't need to know everything."
main_bar_again9 = "When you run out of things to say, people begin telling you about other monsters in the vicinity they'd like you to slay. “Why not?” you declare. THE END."

main_table_chose1 = "You find the same group at that same table in the corner. Have they been sitting there this whole time? “I'm back, you indolent lot,” you say."
main_table_chose2 = "“The dragon slayer returns!” announces the woman who first told you about the dragon. The whole tavern seems to hear, and they crowd around your table."
main_table_chose3 = "You regale the admiring crowd with stories of your brave exploits, fudging the truth just a little bit. They don't need to know everything."
main_table_chose4 = "When you run out of things to say, people begin telling you about other monsters in the vicinity they'd like you to slay. “Why not?” you declare. THE END."

main_table_forced1 = "You find the woman who challenged you to a fight, still brimming with resentment towards her. “I killed the dragon,” you tell her sullenly."
main_table_forced2 = "Her head stays slumped in a drink-induced stupor for a moment, then she turns slowly to look at you. “Wait, what?” she slurs. “What dragon?”"
main_table_forced3 = "“The dragon I had to kill after you beat me in that fight?”"
main_table_forced4 = "“Fight? What are you talking about?”"
main_table_forced5 = "You sigh again, even louder this time, and find some more friendly faces to talk to. Soon, the whole population of the tavern is gathered around you."
main_table_forced6 = "You regale the admiring crowd with stories of your brave exploits, fudging the truth just a little bit. They don't need to know everything."
main_table_forced7 = "When you run out of things to say, people begin telling you about other monsters in the vicinity they'd like you to slay. “Why not?” you declare. THE END."

main_magic_table1 = "You seek out your savior from earlier. You don't think he would run off with your amulet. You scan the tavern for him, and at first he is nowhere to be seen."
main_magic_table2 = "But finally, you spot him, sulking in a corner. He looks noticeably more handsome than you remembered. You try not to blush as you approach his table."
main_magic_table3 = "After taking the seat across from him, you sit there awkwardly for a moment until you realize why you're here. “So... I killed the dragon,” you announce, holding up the scale as proof."
main_magic_table4 = "“Indeed? I'm impressed,” he says, smiling slightly. He takes out the amulet from his satchel and hands it to you."
main_magic_table5 = "“Oh. Um, thanks,” you reply, hoping he realizes you're grateful for both the amulet and the compliment. “Well, I guess I'll get going, them?”"
main_magic_table6 = "“Wait,” he says, seeming almost reluctant to see you go. “Why not stay and share a drink?”"
main_magic_table7 = "“Why not?” you say. Who knows where this might lead? THE END."

main_charisma_return1 = "You find the burly man with whom you negotiated your release from the pyre. “The dragon is dead,” you say, holding the scale up as proof. Hopefully he won't doubt you."
main_charisma_return2 = "“Well done,” he admits grudgingly, gruffly. He gives you the amulet."
main_charisma_return3 = "You leave the tavern with no intention of ever returning. You don't need anyone finding out that the dragon is still alive and well."
main_charisma_return4 = "Who knows what great and terrible things you could achieve with a dragon who hands on your every word? THE END."

# -------- Main Program Loop -----------

pygame.event.get()
while pygame.key.get_pressed()[pygame.K_SPACE] == 0:
	pygame.event.get()
	# --- Main event loop
	screen.fill(BLACK)
	draw(100)
	img1 = pygame.image.load("intro_screen.jpg")
	screen.blit(img1, (25, 25))
	pygame.event.get()
	textput_wrap = textwrap.wrap(text_intro, 65)
	for i in range(len(textput_wrap)):
		text_printer(i, textput_wrap)
	if pygame.key.get_pressed()[pygame.K_x] == 1:
		sys.exit()

	if pygame.key.get_pressed()[pygame.K_1] != 0:
		stealth = True
		strength = False
		magic = False
		manipulation = False
	elif pygame.key.get_pressed()[pygame.K_2] != 0:
		strength = True
		stealth = False
		magic = False
		manipualtion = False
	elif pygame.key.get_pressed()[pygame.K_4] != 0:
		magic = True
		stealth = False
		strength = False
		manipulation = False
	elif pygame.key.get_pressed()[pygame.K_3] != 0:
		manipulation = True
		stealth = False
		strength = False
		magic = False

	if stealth == True:
		screen.fill(BLACK)
		draw(100)
		imgstea = pygame.image.load("Stealth_Bio.jpg")
		screen.blit(imgstea, (25, 25))
		text("CHOOSE STEALTH")
		textput_wrap = textwrap.wrap(textstealth_chose, 65)
		for i in range(len(textput_wrap)):
			text_printer(i, textput_wrap)
	elif strength == True:
		screen.fill(BLACK)
		draw(100)
		imgstre = pygame.image.load("Strength_Bio.jpg")
		screen.blit(imgstre, (25, 25))
		text("CHOOSE STRENGTH")
		textput_wrap = textwrap.wrap(textstrength_chose, 65)
		for i in range(len(textput_wrap)):
			text_printer(i, textput_wrap)
	elif manipulation == True:
		screen.fill(BLACK)
		draw(100)
		imgmanip = pygame.image.load("Charisma_Bio.jpg")
		screen.blit(imgmanip, (25, 25))
		text("CHOOSE MANIPULATION")
		textput_wrap = textwrap.wrap(textcharisma_chose, 65)
		for i in range(len(textput_wrap)):
			text_printer(i, textput_wrap)
	elif magic == True:
		screen.fill(BLACK)
		draw(100)
		imgmag = pygame.image.load("Magic_Bio.jpg")
		screen.blit(imgmag, (25, 25))
		text("CHOOSE MAGIC")
		textput_wrap = textwrap.wrap(textmagic_chose, 65)
		for i in range(len(textput_wrap)):
			text_printer(i, textput_wrap)
	else:
		text("")
	pygame.display.flip()
	pygame.event.get()
	if pygame.key.get_pressed()[pygame.K_SPACE] == 1:
		done = True

# Story
time.sleep(0.5)
mainstorydif(main_mugging, "muggingdrop.jpg"  )

# mugging
time.sleep(0.5)
if stealth == True:
	mainstorydif(stealth_mugging,"muggingstealth.jpg" )
elif strength == True:
	mainstorydif(strength_mugging, "muggingstrength.jpg" )
elif magic == True:
	mainstorydif(magic_mugging, "muggingmagic.jpg")
elif manipulation == True:
	mainstorydif(charisma_mugging, "muggingcarisma.jpg")


# tavern and witch hunt
time.sleep(0.5)
if stealth == True:
	tavern_choice(main_tavern, fir, sec, main_tablestealth, main_tablestealth_yes, main_tablestealth_no)

elif strength == True:
	choice(main_tavern, "tavern_walkup.jpg", fir, sec, main_tablestrength, main_tablestealthp2, main_barp1, main_barp2, "tavern_tables_strength.jpg", "tavern_tables_strength.jpg", "tavern_bar_strength.jpg", "tavern_bar_strength.jpg"  )

elif magic == True:
	mainstorydif(main_magicwitch, "PyreMagic-2.jpg")	
	time.sleep(0.5)
	mainstorydif(main_magicwitchp2,"PyreMagic-2.jpg" )

elif manipulation == True:
	mainstorydif(main_charismawitch,"PyreCharisma.jpg" )
	time.sleep(0.5)
	mainstorydif(main_charismawitchp2,"PyreCharisma.jpg" )
	time.sleep(0.5)
	mainstorydif(main_charismawitchp3,"PyreCharisma.jpg" )
# time.sleep(0.5)

#castle walk up
time.sleep(0.5)
mainstorydif(main_castle_1, "tocastle.jpg")
time.sleep(0.5)
mainstorydif(main_castle_2, "tocastle.jpg" )
time.sleep(0.5)
mainstorydif(main_castle_3, "tocastle.jpg")

#conflict in front of the castle 
time.sleep(0.5)
if stealth == True:
	mainstorydif(main_castle_stealth_1, " " )
	time.sleep(0.5)
	mainstorydif(main_castle_stealth_2," "  )
	time.sleep(0.5)
	mainstorydif(main_castle_stealth_3," " )
elif strength == True:
	mainstorydif(main_castle_strength_1, "Strengthcastle.jpg")
	time.sleep(0.5)
	mainstorydif(main_castle_strength_2, "Strengthcastle.jpg")
elif magic == True:
	mainstorydif(main_castle_m_1, "magiccastle.jpg") #magic and manip needs to have boulder behind sprites
	time.sleep(0.5)
	mainstorydif(main_castle_m_2, "magiccastle.jpg")
	time.sleep(0.5)
	mainstorydif(main_castle_m_3, "magiccastle.jpg")
elif manipulation == True:
	mainstorydif(main_castle_m_1, "charismacastle.jpg")
	time.sleep(0.5)
	mainstorydif(main_castle_m_2, "charismacastle.jpg")
	time.sleep(0.5)
	mainstorydif(main_castle_m_3, "charismacastle.jpg")


#dragon
time.sleep(0.5)
mainstorydif(main_incastle_ , "tocastle.jpg")
time.sleep(0.5)
if stealth == True:
	mainstorydif(stealth_dragon1, "Stealth1.jpg" )
	time.sleep(0.5)
	choice(stealth_dragon1p1, "Stealth2.jpg", fir, sec, stealth_dragon_chand, stealth_dragon_chand2, stealth_dragon_dragon, "PRESS X TO END" , "stealth4.jpg", "stealth4.jpg", "Stealth3.jpg", "Stealth3.jpg" )
if strength == True: 
	choice(strength_dragon, "DungeonStrength.jpg", fir, sec, strength_dragon_sleep, strength_dragon_sleep2, strength_dragon_wake, strength_dragon_wake2, "DungeonStrength-4.jpg", "DungeonStrength.jpg", "DungeonStrength-3.jpg", "DungeonStrength-7.jpg")
if magic == True:
	choice(magic_dragon, "dungeonmagic.jpg ", fir, sec, magic_dragon_fight, magic_dragon_fight2, magic_dragon_flee, magic_dragon_flee2, "dungeonmagic.jpg", "dungeonmagic.jpg", "dungeonmagic.jpg", "dungeonmagic.jpg")
if manipulation == True:
	choice( manip_dungeon , "dungeoncharis.jpg", fir , sec , manip_dungeon_intim , manip_dungeon_intim2, manip_dungeon_integ, manip_dungeon_integ2, "dungeoncharis.jpg", "dungeoncharis.jpg" , "dungeoncharis.jpg", "dungeroncharis.jpg" )
# --- Game logic should go here ---

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
exit()  # Needed when using IDLE
