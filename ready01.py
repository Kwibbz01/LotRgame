from time import sleep
import random
import colorama
from colorama import Fore, Style
import sys
import time
# colorama.init(autoreset=True)

# frodo_gold = 30
# frodo_health = 100
# nazgul_health = 50
# watcher_in_the_water_health = 50
# moria_troll_health = 100
# moria_orc_health = 50
# saruman_health = 100
# sam_health = 100
# mordor_orc_health = 100
# sauron_health = 250


def tprint(words):
 for char in words:
     sys.stdout.write(char)
     sys.stdout.flush()
     time.sleep(0.04)


frodo_gold = 30
frodo_health = 100
nazgul_health = 50
watcher_in_the_water_health = 50
moria_troll_health = 100
moria_orc_health = 50
saruman_health = 100
sam_health = 100
mordor_orc_health = 100
sauron_health = 250

tprint("                            LORD OF THE RING                                \n")
tprint("----------------------------")
tprint("CRIDETS")
tprint("----------------------------\n\n\n\n")
tprint("*********Daniel Anderson*********\n\n\n")
tprint("*********Lewis Chesworth*********\n\n\n")
tprint("*********Malik Azumi*********\n\n\n")
tprint("*********Seeed Alam*********\n\n\n")

def display_intro():
    tprint(Fore.GREEN)
    tprint("Welcome to Middle-earth!\n")

    tprint(Fore.GREEN + "You are Frodo Baggins, a hobbit living in the Shire.\n")
     
    tprint(Fore.GREEN + "On the day of your Uncle Bilbo's eleventy-first birthday party,\n he mysteriously vanishes while giving his birthday speech.\n You rush to his home, your home, Bag End, where you find none other than the wizard, Gandalf.\n")
    
    meet_gandalf()

def meet_gandalf():
    tprint(Fore.YELLOW + 'You: "Gandalf?\n Where is Bilbo?\n He disappeared into thin air, and we haven\'t even had cake yet."\n')
  
    tprint(Fore.CYAN + 'Gandalf: "Frodo, I must speak with you. It is very important."\n')

    tprint(Fore.YELLOW + 'You: "Of course, Gandalf. What is it? What has happened?\n"')
 
    tprint(Fore.CYAN + 'Gandalf: "Bilbo has gone. He has left all of his belongings, including Bag End, to you."\n')

    tprint(Fore.YELLOW + 'You: "Gone? Gone where? Is he coming back?"\n')

    tprint(Fore.CYAN + 'Gandalf: "I should say not. He has gone to visit the elves, and I do not expect he will return."\n')
 
    tprint(Fore.CYAN + 'Gandalf: "He has left you something else, Frodo. There, on the mantlepiece."\n')
 
    tprint(Fore.GREEN + "You walk over to the fireplace and take down an envelope from the mantle. You open it, and inside is something you recognise immediately\n.")
   
    tprint(Fore.YELLOW + 'You: "Bilbo\'s ring! Why would he leave me this?"\n')
  
    tprint(Fore.CYAN + 'Gandalf: "I have long suspected that Bilbo did not come into possession of that ring by mere chance.\n I have spent many years studying, trying to glean it\'s history."\n')
   
    tprint(Fore.CYAN + 'Gandalf: "It is time to find out if my efforts were to any avail, Frodo. Throw it into the fire."\n')
   
    tprint(Fore.GREEN + 'You hesitate, and Gandalf motions toward the flames. Reluctantly, you throw the envelope into the hearth.\n')
    
    tprint(Fore.GREEN +'As the envelope burns away, you see a faint glow. Gandalf reaches for a poker, and with some effort,\n knocks the ring to the floor. The glow is brighter now, and you can see it is coming from something written on the inside.\n')
   
    tprint(Fore.CYAN + 'Gandalf: "You can pick it up. It\'s quite cool."\n')
    
    tprint(Fore.GREEN + 'You reach down and lift the ring to your eye.\n')
  
    tprint(Fore.YELLOW + 'You: "It\'s some form of elvish, but not a language I recognise."\n')
   
    tprint(Fore.CYAN + 'Gandalf: "I would not expect you to."' + Fore.GREEN + ' Gandalf slowly turns away.\n' + Fore.CYAN + '" It is the Black Speech of Mordor. It is as I suspected. It reads, "One Ring to rule them.\n One Ring to find them. One ring to bring them all, and in the darkness bind them."\n')
  
    tprint(Fore.YELLOW + 'You: "What does it mean, Gandalf?"\n')
   
    tprint(Fore.CYAN + 'Gandalf: "It is the One Ring.\n The weapon of the Dark Lord. We are all in great peril, Frodo. We must make haste.\n The ring cannot stay here. We must seek council."\n')
    
    tprint(Fore.CYAN + 'Gandalf: "I must speak with the wisest of my order.\n You, Frodo, must leave immediately. We have to get the ring to Rivendell."\n')
  
    tprint(Fore.GREEN + 'A noise from outside the window startles you.\n Gandalf throws it open, gripping his staff in both hands.\n He looks out, but there is no one to be seen. The bush rustles underneath the window sill,\n and Gandalf reaches out with the butt of his staff and strikes downward.\n')
    
    tprint(Fore.LIGHTMAGENTA_EX + '"OOOOOOOOOOOOOOOW!"\n')
    
    tprint(Fore.GREEN + 'Gandalf leans out and reaches down. With surprising strength,\n he yanks a startled (and sore) Sam in through the window.\n')

    tprint(Fore.CYAN + 'Gandalf: "SAMWISE GAMGEE! Do you make a habit of eavesdropping on private conversations?\n How much did you overhear?"\n')
     
    tprint(Fore.LIGHTMAGENTA_EX + 'Sam: "I\'m sorry, sir... sirs... I ain\'t been dropping no eaves, and I didn\'t hear much.\n That is to say,\n I did hear a bit about a ring and a Dark Lord, and the end of the world and whatnot..."\n')
     
    tprint(Fore.CYAN + 'Gandalf: "Indeed. Well, since you\'re here, Frodo will likely be in need of a companion for his journey.\n You must go with him, and you must take good care of him, Samwise Gamgee."\n')
     
    tprint(Fore.CYAN + 'Gandalf: "That is, if Frodo accepts the task. Well, Frodo? Will you undertake this quest?"\n')
    make_decision()

def make_decision():
    tprint(Fore.GREEN + 'What will you do?\n')
    tprint(Fore.GREEN + "1. Accept Gandalf's task\n")
    tprint(Fore.GREEN + "2. Refuse Gandalf's task\n")

    choice = input(Fore.GREEN + "Enter your choice (1 or 2): ")

    if choice == '1':
        accept_task()
    elif choice == '2':
        refuse_task()
    else:
        tprint(Fore.RED + "Invalid choice. Please enter 1 or 2.")
        make_decision()

def accept_task():
    tprint(Fore.YELLOW + 'Frodo: "I will help you, Gandalf. What must I do?"\n')
     
    tprint(Fore.CYAN + 'Gandalf: "You must leave the Shire immediately and make your way as fast as you can to Bree.\n Seek shelter in the Prancing Pony The innkeeper, Barliman Butterbur, is a friend.\n I will meet you there as soon as I am able.\n From there we must travel to Rivendell,\n where we shall seek Elrond\'s council. I the meantime, I have an urgent errand to attend with Saruman.\n Farewell, Frodo. Goodbye, and good luck."\n')
     
    merry_and_pippin()

def refuse_task():
    tprint(Fore.YELLOW + 'Frodo: "I am sorry, Gandalf. I cannot do this."\n')
    tprint(Fore.CYAN + 'Gandalf: "I understand, Frodo. But know that the fate of Middle-earth depends upon this task."\n')
    tprint(Fore.GREEN + "You have chosen to refuse Gandalf's task. The fate of Middle-earth grows darker.\n")
    quit()
    # Game over or possible redirection to another part of the story(Game ends right now)

def merry_and_pippin():
    tprint(Fore.GREEN + "Not two minutes later, you are shutting the front door to Bag End.\n Sam, still looking frightened, is stood at the gate, waiting.\n")
     
    tprint(Fore.YELLOW + 'You: "Well, Sam, it looks like it\'s just you and me now.\n Let\'s get this over with."\n')
     
    tprint(Fore.GREEN + "Sam just nods, and the two of you head down the hill and into Hobbiton.\n The noise of Bilbo's party is dying out as you leave the town, following the road south across the The Water, then east,\n headed for Bywater, and then leaving the road and cutting southeast at the Three Farthing Stone,\n heading for Green-Hill Country and the less-travelled road from Tuckborough.\n")
     
    tprint(Fore.GREEN + "You travel for several days and nights, eventually arriving at the gates of Bree with your two friends,\n Merry and Pippin, in tow.\n They were scrumping Farmer Maggot's crops and need to lay low for a while\n, so they decided to join you and Sam on your journey to Bree.\n You were chased by Riders dressed in black onto the ferry at Buckleberry, so your guard is up, and you want to keep a low profile.\n")
     
    bree()

def bree():
    tprint(Fore.GREEN + "After some sharp words from the watchman at the gate,\n he lets you in and shows you the direction of the Prancing Pony.\n")
     
    tprint(Fore.GREEN + "At the inn, you ask for a room for the night - using the name 'Underhill' - find a table in a corner,\n and order ale. You don't feel much like drinking, but Merry and Pippin are in high spirits.\n Pippin especially, as he orders a full pint at the tavern bar.\n")
     
    pay_the_tab()

def pay_the_tab():
    global frodo_gold
    
    tprint(Fore.GREEN + "After a while, the time comes to settle the tab.\n")
     
    tprint(Fore.LIGHTYELLOW_EX + '"Pippin: Let\'s make it interesting. We\'ll roll dice.\n If it\'s above 10, you pay, Frodo. If not, Sam pays."\n')
     
    
    input(Fore.GREEN + "Press Enter to roll the dice...")
    tprint(Fore.GREEN + "Rolling the dice...")
     
    
    roll = random.randint(1, 20)
    tprint(Fore.GREEN + f"It lands on {roll}.")
     

    if roll > 10:
        tprint(Fore.YELLOW + '"You: Looks like I have to pay.\n"')
        frodo_gold -= 5
         
        tprint(Fore.GREEN + f"You pay 5 gold. You now have {frodo_gold} gold left.\n")
    else:
        tprint(Fore.LIGHTMAGENTA_EX + '"\nSam: Lucky you, Mr Frodo. I\'ll cover it."\n')
        tprint(Fore.GREEN + "Sam pays for the tab. You keep your gold.\n")
     
    strider()

def strider():
    tprint(Fore.GREEN + "Pippin collects the coins and heads to the bar. You can just about hear him talking to the innkeep,\n Butterbur, who seems to be asking a question.\n")
     
    tprint(Fore.LIGHTYELLOW_EX + 'Pippin: "Sure I know a Baggins. He\'s sat right over there."\n')
     
    tprint(Fore.GREEN + "You yell in surprise, causing the faces nearest you to turn in your direction.\n You stumble to your feet and lurch towards Pippin. Something traps your foot and sends you flying.\n The ring that had been in your hand (what was it doing there?) flies into the air,\n and as you snatch at it, somehow you slip it onto your finger.\n")
     
    tprint(Fore.GREEN + "The room shifts focus. Everyone is still there, but now they are somehow blurry,\n and their faces look harsher, and more shocked. You realise they are looking around for you.\n This was Bilbo's trick. The ring.\n")
     
    tprint(Fore.GREEN + "You crawl into a corner, away from the crowd, and pull the ring from your finger.\n A rough hand grasps the back of your travelling cloak and not too tenderly brings you to your feet.\n You recognise the face of a man that was staring at you from the opposite corner as Pippin was ordering his beer, but before you can say anything, he pushes you up the stairs.\n")
     
    tprint(Fore.GREEN + "He pushes you into a room and extinguishes the candles,\n drawing the tattered sheet into place across the window, then he turns to face you.\n")
     
    tprint(Fore.CYAN + '"You need to be more careful, Mr Underhill. That is no mere trinket you carry."\n')
     
    tprint(Fore.YELLOW + 'You: "I don\'t know what you mean. Who are you?"\n')
     
    tprint(Fore.GREEN + "Before he can answer, the door bursts open and in rush your three friends,\n each branding a makeshift weapon.\n")
     
    tprint(Fore.LIGHTMAGENTA_EX + 'Sam: "GET BACK, "STRIDER"! We know who you are. What do you want with Frodo?"\n')
     
    tprint(Fore.CYAN + 'Strider: "Calm yourself, Master Hobbit. I am no danger to you. Gandalf asked me to keep watch for you.\n He has not returned from his travels, and I fear some ill has befallen him."\n')
     
    tprint(Fore.YELLOW + 'You: "You know Gandalf?"\n')
     
    tprint(Fore.CYAN + 'Strider: "We are old friends. We have helped one another many times over the years.\n For now, I must help you. Come, you will not be sleeping in these beds this night."\n')
     
    tprint(Fore.GREEN + "After relighting the candles, and with much protesting from Merry and Pippin,\n Strider leads the way out the back door of the inn and across the courtyard to another, smaller room.\n")
     
    tprint(Fore.CYAN + 'Strider: "We will stay here tonight, but at first light, we must leave for Rivendell."\n')
     
    tprint(Fore.GREEN + "The hubbub of the tavern dies away and you settle down to sleep but are awakened again\n a short time later by the sound of metal on wood. Strider is at the window, staring in the direction\n of the room you left earlier. Sam, Merry, and Pippin are all sat bolt upright,\n staring at Strider. You move to the window and peer out.\n There are figures silhouetted against the sheet covering the window of the room opposite.\n You would recognise them anywhere.\n")
     
    tprint(Fore.GREEN + "The silhouettes draw swords and plunge them into the beds.\n As they realise they have been duped,\n you hear their bloodcurdling shrieks. The noise drives all thought from your mind.\n When you regain your senses, Strider is sat in a chair next to the window with his pipe in his mouth, looking deep in thought.\n You lay back down, still trembling, and knowing sleep will evade you for the rest of the night.\n")
    sleep(9)
    tprint(Fore.GREEN + "As the first light of dawn breaks, Strider rouses you and your friends,\n and you make your way quietly out of the courtyard, through the town,\n and into the fields. Strider informs you that travelling by road is too dangerous,\n and so you make your way east across meadows and fields, and through copses of woods, until,\n at dusk, you see a tall hill in the far distance,\n with the ancient remains of some stone\n structure at its summit, and flashes of fire and lightning arcing across the crumbled stones.\n")
     
    tprint(Fore.CYAN + 'Strider: "Alas, we are too far to be of assistance.\n Weathertop is two days journey still. We can only hope for his victory."\n')
     
    tprint(Fore.YELLOW + 'You: "Whose victory?"\n')
     
    tprint(Fore.GREEN + "Strider does not answer. instead settling his small bag down,\n and tightening his sword belt.\n")
     
    tprint(Fore.CYAN + 'Strider: "We camp here.\n"')
     
    tprint(Fore.GREEN + "Strider walks off into the woods to hunt for supper as Merry and Pippin prepare a fire.\n You stare at the hill and the flashing lights as the night grows darker,\n and wonder what could cause such a fascinating light show.\n")
     
    tprint(Fore.GREEN + "Two days later, the company arrives at the base of the hill.\n Strider leads the way to the peak.\n After searching among the fallen rocks and singed grass, he locates a small cairn.\n He shifts a small boulder from the gap and reaches inside,\n withdrawing his hand after fumbling around for a moment,\n and in his hand you see a small fragment of parchment.\n")
     
    tprint(Fore.CYAN + 'Strider: "Our friend survived the battle. Gandalf will meet us in Rivendell."\n')
     
    tprint(Fore.YELLOW + 'You: "Gandalf? He was here?"\n')
     
    tprint(Fore.CYAN + 'Strider: "None other could have stood against the Black Riders,\n and the note he left confirmed it.\n I must scout around for a while to find which direction the Riders took. Be wary.\n They may yet be abroad in these hills."\n')
     
    tprint(Fore.GREEN + "Strider disappears behind the remains of a wall, and you follow a few steps behind,\n wanting to know more about Gandalf\'s note, but as you round the wall,\n Strider is nowhere to be seen.\n")
     
    tprint(Fore.GREEN + "As the evening draws on, Pippin pulls out Sam's cooking equipment.\n They have brought enough wood for a small fire,\n and everyone is hungry. Pippin reaches into his own bag and pulls out a wrapped bundle.\n")
     
    tprint(Fore.LIGHTYELLOW_EX + 'Pippin: "Well, Frodo? Fancy some bacon?"\n')
     
    bacondecision()

def bacondecision():
    tprint(Fore.GREEN + "1. Cook the bacon.\n")
    tprint(Fore.GREEN + "2. Do not cook the bacon.\n")
     

    bacondecision_question = input(Fore.GREEN + "Will you cook the bacon? (1 or 2): ")

    if bacondecision_question == '1':
         
        cook_bacon()
    elif bacondecision_question == '2':
         
        do_not_cook_bacon()
    else:
        tprint(Fore.RED + "Invalid choice. Please enter 1 or 2.")
        bacondecision()

def cook_bacon():
    tprint(Fore.GREEN + "Your hunger overrides your caution, and you help start the fire.\n A few minutes later, you hear the ear-piercing shrieks you heard that night in Bree,\n and as you start to your feet,\n drawing the blade, Sting, that Bilbo left you, the Dark Riders converge on the hilltop.\n")
    encounter_nazgul()
    
    #insert fight here
def encounter_nazgul():
    tprint(Fore.RED + "Prepare for battle!!!")
     
    combat_sequence()

def combat_sequence():
    global frodo_health, nazgul_health
    
    while frodo_health > 0 and nazgul_health > 0:
        tprint(Fore.GREEN + f"Frodo's Health: {frodo_health}")
        tprint(Fore.RED + f"Nazgul's Health: {nazgul_health}")
         
        
        tprint(Fore.GREEN + "Choose your action:\n")
        tprint(Fore.RED + "1. Strike\n")
        tprint(Fore.GREEN + "2. Block\n")
        tprint(Fore.YELLOW + "3. Heal\n")
        
        choice = input(Fore.GREEN + "Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            damage = random.randint(10, 20)
            nazgul_health -= damage
            tprint(Fore.RED + f"You strike the Nazgul and deal {damage} damage!\n")
             
            if nazgul_health > 0:
                tprint(Fore.RED + "Nazgul: SHRIEK!!!!!!")
                 
        elif choice == '2':
            block = random.randint(5, 15)
            tprint(Fore.GREEN + f"You block and will reduce the next attack by {block} damage.")
             
        elif choice == '3':
            heal = random.randint(10, 20)
            frodo_health += heal
            tprint(Fore.YELLOW + f"You heal yourself for {heal} health.\n")
             
        else:
            tprint(Fore.RED + "Invalid choice. Please enter 1, 2, or 3.\n")
            continue
        
        if nazgul_health <= 0:
            break
        
        # Nazgul's turn
        nazgul_damage = random.randint(5, 15)
        if choice == '2':
            nazgul_damage -= block
            if nazgul_damage < 0:
                nazgul_damage = 0
        frodo_health -= nazgul_damage
        tprint(Fore.RED + f"The Nazgul strikes and deals {nazgul_damage} damage!\n")
         
    
    if frodo_health > 0:
        to_rivendell1()        
    else:
        tprint(Fore.RED + "You have been defeated by the Nazgul\n. Middle-earth's fate grows darker.\n")
         

def do_not_cook_bacon():
    tprint(Fore.YELLOW + 'You: "Absolutely not, you fools. We are exposed up here.\n We saw fires on this hill two nights ago,\n from forty miles away or more. Go to sleep. We will need to conserve all the energy we can for the journey."\n')
     
    tprint(Fore.GREEN + "Grumbling, they repack the cooking pans and bacon, and settle down to sleep.\n Strider awakens you all in the morning, and you make your way without further incident to Rivendell,\n where you are greeted warmly, introduced to Elrond, Lord of Rivendell,\n and given a bed... which you immediately make use of.\n")
     
    rivendell()

def to_rivendell1():
    tprint(Fore.GREEN + "As the Riders surround you, you feel the ring calling you. You pull it from your pocket and grip it tightly,\n but the urge is too strong. As you fall to the floor, you slip it onto your finger, and the world blurs again.\n")
     
    tprint(Fore.GREEN + "The Riders' appearances are transformed. Instead of hooded cloaks,\n they now wear the tattered remnants of fine clothes and have crowns on their heads,\n but they are as ghosts. As the tallest approaches,\n he pulls a long dagger, and before you can roll away, he stabs you in the shoulder.\n")
     
    tprint(Fore.GREEN + "A searing flash of pain blinds you. As you tear the ring from your finger,\n you see Strider arrive, sword drawn and carrying a burning brand.\n You are awake just long enough to see him set fire to their cloaks,\n and watch them all leap from the hilltop,\n and then the world around you goes dark, and you slip into unconciousness.\n")
     
    tprint(Fore.GREEN + "You awaken in a clearing. You can hear voices discussing your injury.\n Strider is telling Sam he needs to find a herb, Kingfoil, to stop the spread of infection.\n")
    kingsfoil()

def kingsfoil():
    tprint(Fore.GREEN + '"Strider and Sam are searching for the Kingsfoil plant.\n If you roll above 10, Strider finds the Kingsfoil, if not,\n Aragorn does not locate the plant."\n')
     

    input(Fore.GREEN + "Press Enter to roll the dice...")
    tprint(Fore.GREEN + "Rolling the dice...")
     

    roll = random.randint(1, 20)
    tprint(Fore.GREEN + f"It lands on {roll}.")
     

    if roll > 10:
        tprint(Fore.CYAN + 'Strider: "I found the it! I must make a poultice from the flowers.\n Sam, brew the leaves and give Frodo the tincture."\n')
         
        to_rivendell2()
    else:
        tprint(Fore.GREEN + "Strider and Sam search for the plant, but there is none to be found.\n")
         
        tprint(Fore.CYAN + 'Strider: "I  am sorry, Frodo. I will do what I can."\n')
         
        to_rivendell2()

def to_rivendell2():
    tprint(Fore.GREEN + "As Strider attends to your wound, you hear a new voice.\n A man enters the clearing speaking in elvish.\n Strider welcomes the stranger with an embrace and by name, Glorfindel, and tells him of your injury.\n")
     
    tprint(Fore.BLUE + 'Glorfindel: "We must get him to Elrond, Aragorn. Only the magic of the Eldar will save him now."\n')
     
    tprint(Fore.CYAN + 'Strider: "Ride, my friend. Like the wind. The Riders will not be far behind you.\n You must make the Ford of Bruinen before nightfall.\n We will meet you there in a few days."\n')
     
    tprint(Fore.GREEN + "You drift in and out of conciousness as the day wears on,\n but suddenly you are brought around by the familiar sound of other horses.\n You strain to turn your head to look behind,\n and there, on your tail, are nine black horses, with nine Riders.\n")
     
    tprint(Fore.GREEN + "Glorfindel speaks in elvish, and the horse beneath you surges forward.\n You can hear the sound of a waterfall,\n and you imagine for a moment that your ears are playing tricks on you.\n A few minutes later, the sound of splashing from your mount's hooves,\n spray in your face, then dry land again, and Glorfindel turns his steed to face the pursuers.\n")
     
    tprint(Fore.GREEN + "The Riders reach the edge of the river on the far side,\n their horses faltering at the water,\n but the Riders urge their mounts into the river. They have responded to Glorfindel's challenge, but he does not flee.\n")
     
    tprint(Fore.GREEN + "Instead, more words in elvish, this time it is as if he is talking to the river itself,\n and the river responds. With the Riders nearly halfway across the ford, the river roars.\n A torrent of water rises from upriver and comes barrelling down on the Dark Riders.\n They attempt to flee, but the flood arrives too swiftly.\n They are swept up in the deluge and carried downstream. The pain in your shoulder flares again,\n and you sink back into darkness.\n")
     
    tprint(Fore.GREEN + "The next time you awaken, Sam is at your side as an elf dressed in delicate finery tends your wound.\n Gandalf enters the room and speaks with your nurse,\n then introduces him to you as Elrond, Lord of Rivendell.\n You are too tired still to speak, so you nod your greeting and thanks, lay your head back,\n and drift into the most comfortable sleep you can remember.\n")
     
    rivendell()

def rivendell():
    tprint(Fore.GREEN + "Gandalf rouses you the next day. He quickly explains that he was held up in Isengard.\n Saruman has fallen under the sway of the Dark Lord, and Elrond has called a Council of elves and men,\n and now, hobbits and a dwarf. You hurry your breakfast down and walk with Gandalf to the meeting.\n")
     
    tprint(Fore.GREEN + "The meeting proceeds apace, with Gandalf explaining the provenance of the ring and Saruman's fall from grace.\n Strider is introduced as Aragorn, son of Arathorn, Isildur's heir,\n and heir to the throne of Gondor. Legolas, son of Thranduil of Mirkwood is present,\n as is the dwarf, Gimli, son of Gloin, and Boromir, son of the Steward of Gondor, Denethor.\n")
     
    tprint(Fore.GREEN + "Elrond tells the Council that the ring cannot be hidden in Rivendell. The Dark Lord will eventually muster his forces against the elves, and they will not withstand a siege. The ring, it seems, must be taken into Mordor, to the place of its creation, and destroyed in the fires of Mount Doom.")
     
    tprint(Fore.GREEN + "As the meeting decends into chaos and arguing, you realise someone must take it upon themselves to volunteer. Will it be you?\n")
     
    ring_decision()

def ring_decision():
    tprint(Fore.GREEN + "1. Take the ring to Mordor.\n")
    tprint(Fore.GREEN + "2. Do not take the ring to Mordor.\n")

    ringdecision = input(Fore.GREEN + "Enter your choice (1 or 2): ")

    if ringdecision == '1':
        tprint(Fore.GREEN + "You agreed to take the ring to Mordor. With the help of Gandalf, Aragorn, Legolas, Gimli, Merry, Pippin and Sam become known as 'THE FELLOWSHIP OF THE RING!\n")
         
        to_moria()
    elif ringdecision == '2':
        tprint(Fore.GREEN + "You refuse the ring and with the help of Gandalf, you make your way home to the Shire.\n")
         
        tprint(Fore.GREEN + "(A FEW MONTHS LATER)\n")
         
        tprint(Fore.GREEN + "You are awoken by the sound of screeams and a sunset orange blaze shining against the window glass.\n As you rush to peer through the window pane, it's clear that Sauron's forces have come slaughtering through the Shire.\n Hobbits are being slain and houses burnt.\n As you look away from the window and around your house, you see the whole place is engulfed in flames.\n You rush to the nearest exit, but you are blocked by flames.\n Slowly but surely each area is engulfed by flames blocking your exit. This is the end. Middle-earth has fallen to Sauron.\n")
    else:
        tprint(Fore.RED + "Invalid choice. Please enter 1 or 2.")
        ringdecision()

def to_moria():
    tprint(Fore.GREEN + "The fellowship sets out on the road and travels towards the Misty Mountains.\n As you approach the entrance to Moria, Gandalf asks you to make a decision.\n")
     
    moria_or_isengard()

def moria_or_isengard():
    tprint(Fore.GREEN + '"Isengard bars way to Mordor. The Mines of Moria are an unknown, but Gimli is full of bluster about them.\n Gandalf asks you whether you should go into Moria or face Saruman. What will you pick?"\n')
     
    tprint(Fore.GREEN + "1. Enter Moria\n")
    tprint(Fore.GREEN + "2. Face the might of Isengard\n")
     

    ringdecision = input(Fore.GREEN + "Enter your choice (1 or 2): ")

    if ringdecision == '1':
        tprint(Fore.GREEN + "You choose Moria, where Gimli will take you to experience the hospitality of the dwarves and meet his cousin, Balin.\n" )
         
        tprint(Fore.GREEN + "When you reach the gates of Moria, you discover they are magically locked.\n Gandalf tries to open the gates with spells.\n This does not work. After much poindering you realise that the speaking the elvish word for friend will allow you to open the gates.\n You ask Gandalf the word, and when it is spoken, the gates rumble open.\n Suddenly you are attacked from the rear by a giant monster from the pool behind you.\n You could fight the creature or escape into the Mines. Should you fight or flee?\n")
         
        gates_of_moria()
    elif ringdecision == '2':
        tprint(Fore.GREEN + "You choose to face Saruman at Isengard.\n")
         
        isengard()
    else:
        tprint(Fore.RED + "Invalid choice. Please enter 1 or 2.\n")
        ringdecision()

def gates_of_moria():
    tprint(Fore.GREEN + "1. Fight the monster.\n")
    tprint(Fore.GREEN + "2. Flee into the Mines.\n")
     

    moria_decision = input(Fore.GREEN + "Enter your choice (1 or 2):\n ")

    if moria_decision == '1':
        tprint(Fore.GREEN + "You will fight the Watcher in the Water.\n")
         
        watcher_in_the_water()
    elif moria_decision == '2':
        tprint(Fore.GREEN + "You flee and escape with your lives.\n")
         
        into_the_mines()
    else:
        tprint(Fore.RED + "Invalid choice. Please enter 1 or 2.")
        gates_of_moria()

def watcher_in_the_water():
    global frodo_health, watcher_in_the_water_health
    
    while frodo_health > 0 and watcher_in_the_water_health > 0:
        tprint(Fore.YELLOW + f"Frodo's Health: {frodo_health}\n")
        tprint(Fore.RED + f"Watcher in the Water's Health: {watcher_in_the_water_health}\n")
         
        
        tprint(Fore.GREEN + "Choose your action:")
        tprint(Fore.RED + "1. Strike")
        tprint(Fore.GREEN + "2. Block")
        tprint(Fore.YELLOW + "3. Heal")
        
        choice = input(Fore.GREEN + "Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            damage = random.randint(10, 20)
            watcher_in_the_water_health -= damage
            tprint(Fore.RED + f"You strike the creature and deal {damage} damage!\n")
             
            if watcher_in_the_water_health > 0:
                tprint(Fore.RED + "The Watcher in the Water thrashes in pain!!!!!!\n")
                 
        elif choice == '2':
            block = random.randint(5, 15)
            tprint(Fore.GREEN + f"You block and will reduce the next attack by {block} damage.\n")
             
        elif choice == '3':
            heal = random.randint(10, 20)
            frodo_health += heal
            tprint(Fore.YELLOW + f"You heal yourself for {heal} health.\n")
             
        else:
            tprint(Fore.RED + "Invalid choice. Please enter 1, 2, or 3.")
            continue
        
        if watcher_in_the_water_health <= 0:
            break
        
        watcher_in_the_water_damage = random.randint(5, 15)
        if choice == '2':
            watcher_in_the_water_damage -= block
            if watcher_in_the_water_damage < 0:
                watcher_in_the_water_damage = 0
        frodo_health -= watcher_in_the_water_damage
        tprint(Fore.RED + f"The creature strikes and deals {watcher_in_the_water_damage} damage!\n")
         
    
    if frodo_health > 0:
        tprint(Fore.GREEN + "You battle as hard as you can, but this creature seems to possess otherworldly strength.\n At the last, Gandalf orders everyone to fall back into the Mines. As you retreat,\n the beast lurches out of the pool and wraps its tentacles around the open gates,\n heaving them down with an enormous crash. Rocks fall from the mountainside above, sealing the entrance.\n")
         
        into_the_mines()        
    else:
        tprint(Fore.RED + "You have been defeated by the Watcher in the Water.\n The fellowship must continue without you. Middle-earth's fate grows darker.\n")
         
        quit()

def into_the_mines():
    tprint(Fore.GREEN + "You are now forced into the darkness. You find bones littered underfoot, along with orcish arrows.\n Gandalf takes the lead, guiding you with the light of his staff. After some days,\n you arrive at a room, bare except for a tomb in the centre.\n")
     
    tprint(Fore.GREEN + "Gimli runs into the room, wailing. Gandalf follows and finds a dust-covered book.\n As he reads aloud, it becomes apparent that this tomb is Balin's, and the Mines have fallen to the orcs.\n")
     
    tprint(Fore.GREEN + "Pippin sits on the edge of a well-like construction in one corner.\n There is a bucket with a chain attached. Pippin reaches for an arrow impaling the bucket.\n")
     
    the_arrow()

def the_arrow():
    tprint(Fore.GREEN + "1. Distract Pippin.\n")
    tprint(Fore.GREEN + "2. Don't distract Pippin.\n")
     

    moria_decision = input(Fore.GREEN + "Enter your choice (1 or 2): ")

    if moria_decision == '1':
        tprint(Fore.GREEN + "You successfully distract Pippin. Who knows what would have happened if you hadn't. Gandalf suggests you all leave this place as swiftly as possible.\n")
         
        to_the_hall()
    elif moria_decision == '2':
        tprint(Fore.GREEN + "Pippin twists the arrow. The bucket and chain fall into the hole.\n After a few moments, drums sound in the depths. Oh, no. They have a cave troll.\n")
         
        tomb_fight()
    else:
        tprint(Fore.RED + "Invalid choice. Please enter 1 or 2.")
        the_arrow()

def tomb_fight():
    global frodo_health, moria_troll_health
    
    while frodo_health > 0 and moria_troll_health > 0:
        tprint(Fore.GREEN + f"Frodo's Health: {frodo_health}\n")
        tprint(Fore.RED + f"Troll's Health: {moria_troll_health}\n")
         
        
        tprint(Fore.GREEN + "Choose your action:\n")
        tprint(Fore.RED + "1. Strike\n")
        tprint(Fore.GREEN + "2. Block\n")
        tprint(Fore.YELLOW + "3. Heal\n")
        
        choice = input(Fore.GREEN + "Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            damage = random.randint(10, 20)
            moria_troll_health -= damage
            tprint(Fore.RED + f"You strike the troll and deal {damage} damage!\n")
             
            if moria_troll_health > 0:
                tprint(Fore.RED + "Troll: ROAR!!!!!!\n")
                 
        elif choice == '2':
            block = random.randint(5, 15)
            tprint(Fore.GREEN + f"You block and will reduce the next attack by {block} damage.\n")
             
        elif choice == '3':
            heal = random.randint(10, 20)
            frodo_health += heal
            tprint(Fore.YELLOW + f"You heal yourself for {heal} health.\n")
             
        else:
            tprint(Fore.RED + "Invalid choice. Please enter 1, 2, or 3.")
            continue
        
        if moria_troll_health <= 0:
            tprint(Fore.GREEN + "The troll is defeated but the orcs keep coming. You must run.\n")
             
            break

        moria_troll_damage = random.randint(5, 15)
        if choice == '2':
            moria_troll_damage -= block
            if moria_troll_damage < 0:
                moria_troll_damage = 0
        frodo_health -= moria_troll_damage
        tprint(Fore.RED + f"The troll strikes and deals {moria_troll_damage} damage!\n")
         
    
    if frodo_health > 0:
        to_the_hall()        
    else:
        tprint(Fore.RED + "You have been defeated by the troll. Middle-earth's fate grows darker.\n")
        quit()

def to_the_hall():
    tprint(Fore.GREEN + "You all run as fast as your legs will carry you until you reach a wide hall.\n The orcs close around you, but suddenly, from the far end of the hall comes a deep bellow and the orcs scatter.\n Gandalf's face turns pale, and he urges you to flee once more.\n")
     
    tprint(Fore.GREEN + "You reach a narrow stone bridge. One by one you cross until only Gandalf remains.\n He turns halfway across. Behind him looms an enormous creature, wreathed in fire.\n Gandalf stands his ground on the bridge and yells:\n")
     
    tprint(Fore.CYAN + 'Gandalf: "YOU SHALL NOT PASS!"\n')
     
    tprint(Fore.GREEN + "The creature steps onto the bridge as Gandalf cracks his staff onto the stone.\n The bridge gives way and the creature falls into the abyss. At the last second, it flicks a fiery whip that wraps around Gandalf's ankle and drags him over the edge.\n Before he falls, with the last of his strength he cries:\n")
     
    tprint(Fore.CYAN + 'Gandalf: "FLY, YOU FOOLS!"\n')
     
    tprint(Fore.GREEN + "And he is gone. As grief and anger wash over you, you have a choice:\n stay and fight the orcs, or follow Gandalf's advice and flee.\n")
     
    balrog_fight()

def balrog_fight():
    tprint(Fore.GREEN + '"Do you want to fight or flee?"\n')
     
    tprint(Fore.GREEN + "1. Fight\n")
    tprint(Fore.GREEN + "2. Flee\n")
     

    balrogfight = input(Fore.GREEN + "Enter your choice (1 or 2): \n")

    if balrogfight == '1':
        moria_orc_fight()
    elif balrogfight == '2':
        tprint(Fore.GREEN + "You flee the Mines with your remaining companions.\n Aragorn tells you there is no time to sit and grieve, you must get out of these hills.\n With tears in your eyes, you all make your way down the slopes to the woods of Lothlorian.\n")
        lothlorien()
    else:
        tprint(Fore.RED + "Invalid choice. Please enter 1 or 2.")
        balrog_fight()

def moria_orc_fight():
    global frodo_health, moria_orc_health
    
    while frodo_health > 0 and moria_orc_health > 0:
        tprint(Fore.YELLOW + f"Frodo's Health: {frodo_health}\n")
        tprint(Fore.RED + f"Orcs' Health: {moria_orc_health}\n")
         
        
        tprint(Fore.GREEN + "Choose your action:\n")
        tprint(Fore.RED + "1. Strike\n")
        tprint(Fore.GREEN + "2. Block\n")
        tprint(Fore.YELLOW + "3. Heal\n")
        
        choice = input(Fore.GREEN + "Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            damage = random.randint(10, 20)
            moria_orc_health -= damage
            tprint(Fore.RED + f"You strike the orcs and deal {damage} damage!\n")
             
            if moria_orc_health > 0:
                tprint(Fore.RED + "Orc: AAARRGH!!!!!!\n")
                 
        elif choice == '2':
            block = random.randint(5, 15)
            tprint(Fore.GREEN + f"You block and will reduce the next attack by {block} damage.\n")
             
        elif choice == '3':
            heal = random.randint(10, 20)
            frodo_health += heal
            tprint(Fore.YELLOW + f"You heal yourself for {heal} health.\n")
             
        else:
            tprint(Fore.RED + "Invalid choice. Please enter 1, 2, or 3.\n")
            continue
        
        if moria_orc_health <= 0:
            tprint(Fore.GREEN + "These orcs are defeated but more are coming.\n You must run.\n As you exit the mines, Aragorn urges you down the slopes and into the trees.\n")
             
            break

        moria_orc_damage = random.randint(5, 15)
        if choice == '2':
            moria_orc_damage -= block
            if moria_orc_damage < 0:
                moria_orc_damage = 0
        frodo_health -= moria_orc_damage
        tprint(Fore.RED + f"The orcs strike and deal {moria_orc_damage} damage!\n")
         
    
    if frodo_health > 0:
        lothlorien()        
    else:
        tprint(Fore.RED + "You have been defeated by the orcs. Middle-earth's fate grows darker.\n")
        quit()

def lothlorien():
    tprint(Fore.GREEN + "As you enter the treeline, you are surrounded by elves.\n They take you into the forest where you are confronted by Galadriel and her husband, Celeborn.\n They offer you rest and restock your supplies. The next day,\n you head out of the forest, south and west, to the land of Rohan.\n To avoid being seen, Aragorn suggests you enter the edge of the forest of Fangorn.\n")
     
    fangorn()

def isengard():
    tprint(Fore.GREEN + "You choose to brave the dangers of the Tower of Orthanc,\n but Gandalf suggests stealth.\n You agree, and as you near the tower, you all furtively slip into the grounds.")
     
    encounter_saruman()

def encounter_saruman():
    tprint(Fore.RED + "On your past Isengard you sneak into the long reaching archways of the garden beneath the dark charcoal tower.\n  As you begin to think you have snuck by the wizard,\n you realise a presence lingering in the shadows. Saruman!\n")
     
    tprint(Fore.RED + "Prepare for battle!!!\n")
     
    saruman_fight()

def saruman_fight():
    global frodo_health, saruman_health
    
    while frodo_health > 0 and saruman_health > 0:
        tprint(Fore.YELLOW + f"Frodo's Health: {frodo_health}\n")
        tprint(Fore.RED + f"Saruman's Health: {saruman_health}\n")
         
        
        tprint(Fore.GREEN + "Choose your action:\n")
        tprint(Fore.RED + "1. Strike\n")
        tprint(Fore.GREEN + "2. Block\n")
        tprint(Fore.YELLOW + "3. Heal\n")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            damage = random.randint(10, 20)
            saruman_health -= damage
            tprint(Fore.GREEN + f"You strike Saruman and deal {damage} damage!\n")
             
            if saruman_health > 0:
                tprint(Fore.RED + "Saruman: You are no match for the power of Saruman\n")
                 
        elif choice == '2':
            block = random.randint(5, 15)
            tprint(Fore.GREEN + f"You block and will reduce the next attack by {block} damage.\n")
             
        elif choice == '3':
            heal = random.randint(10, 20)
            frodo_health += heal
            tprint(Fore.YELLOW + f"You heal yourself for {heal} health.\n")
             
        else:
            tprint(Fore.RED + "Invalid choice. Please enter 1, 2, or 3.\n")
            continue
        
        if saruman_health <= 0:
            break
        
        # Saruman's turn
        saruman_damage = random.randint(5, 15)
        if choice == '2':
            saruman_damage -= block
            if saruman_damage < 0:
                saruman_damage = 0
        frodo_health -= saruman_damage
        tprint(Fore.RED + f"Saruman strikes and deals {saruman_damage} damage!\n")
         
    
    if frodo_health > 0:
        tprint(Fore.GREEN + "You have defeated Saruman! Your way into Rohan and on to Edoras is now clear.\n")
         
        edoras()
    else:
        tprint(Fore.RED + "You have been defeated by Saruman. Gandalf uses the last of his strength to give you an escape.\n You make a run for it, north into Fangorn Forest.\n")
         
        fangorn()

def fangorn():
    tprint(Fore.GREEN + "Still aching from the loss of your friend,\n you make you way through the trees until you reach a clearing. Stood on a rocky ledge is a familiar figure,\n wreathed in white light.\n For a moment, you think Saruman has found you, but as your eyes become accustomed to the brightness, the face of Gandalf is revealed.\n")
     
    tprint(Fore.CYAN + 'Gandalf: "I have returned to you through fire and death at the turning of the tide.\n Come, we must reach Edoras and marshal Theoden\'s forces to aid Gondor.\n"')
     
    tprint(Fore.GREEN + "You reach the edge of Fangorn Forest. Gandalf would greatly appreciate a horse.\n")
     
    gandalf_horse()

def gandalf_horse():
    tprint(Fore.GREEN + "Gandalf whistles in the soft, gentle breeze to help summon his noble steed.\n You hope luck is on your side.\n")

    input(Fore.GREEN + "Press Enter to roll the dice...\n")
    tprint(Fore.GREEN + "Rolling the dice...\n")
     
    
    roll = random.randint(1, 20)
    tprint(Fore.GREEN + f"It lands on {roll}.\n")
     

    if roll > 10:
        tprint(Fore.GREEN + "You have summoned Gandalf's white stallion, Shadowfax. You arrive at Edoras in the evening.\n")
         
        edoras()

    else: 
        tprint(Fore.GREEN + "Gandalf's horse is no where to be seen. It looks like this long, arduous journey will take longer than expected\n")
         
        tprint(Fore.GREEN + "You arrive at Edoras 3 days later.\n")
        edoras()

def edoras():
    tprint(Fore.GREEN + "Once at Edoras, you are ushered into the King's hall. Gandalf persuades him to ride to Gondor's aid,\n you are resupplied with food and water, and the fellowship leaves for Gondor.\n")
     
    gondor()

def gondor():
    tprint(Fore.GREEN + "When you reach Gondor, you are met with a company of city guards and taken to the throne room.\n Denethor II, Steward of Gondor, sits on a small throne next to the King's, and questions you about your travels.\n")
     
    tprint(Fore.GREEN + "Gandalf cannot convince Denethor to allow you to take the ring into Mordor, but a fire starts in an adjacent room and Gandalf tells you and Sam to run.\n You manage to escape the throne room and down through the ringed walls of Gondor,\n slipping out of a hidden exit in the outer wall.\n You cross the Pellanor Fields, find a small boat on the edge of the River Anduin, and paddle to the eastern shore.\n")
     
    tprint(Fore.GREEN + "After a few days hard travel, you reach the road leading to a grim-looking tower, Minas Ithil.\n It has the stench of orcs and fell things,\n but to the north, set slightly back from the road, you come across a steep path cut into the cliff leading up,\n out of sight. A way into Mordor, perhaps. You have no choice. You must make the ascent.\n")
     
    shelob()

def shelob():
    tprint(Fore.GREEN + "You and Sam slowly climb your way up the steep, narrow steps.\n As you manage to pull yourselves up to the top of the mountain cliffside, you gaze upon a large opening,\n which looks like an entrance to a cave. Begrudgingly, you make your way into the dark caves where you are met by a void of sheer darkness.\n")
     
    tprint(Fore.GREEN + "The deeper you go, the darker it gets. The soft squelching underfoot is disturbing,\n and you can smell rotting flesh. You hear a scuttling sound resonating against the walls of the cave,\n and you can feel something soft brushing against you. You turn in alarm.\n Sam is no longer with you. You call him, and hear a distant reply off to your right.\n")
     
    tprint(Fore.GREEN + "As you turn to head towards it, a giant spider slams its body into you.\n You look down to see a stinger protuding from your stomach, and the world goes black.\n")
     
    sam()

def sam():
    tprint(Fore.GREEN + "As Sam stumbles out of the caves, he sees a group of orcs carrying a limp,\n mummified Frodo between them up a path that looks to lead to a makeshift tower.\n Frodo's sword,\n Sting, is lying under a small outcropping. He picks it up and tucks it into his belt.\n")
     
    tprint(Fore.GREEN + "He tails the orcs up the path, listening to their discussion.\n They apparently found Frodo lying at the cave exit with someone,\n or something, called 'Shelob' towering over him.\n They had chased the thing away with fire and are now arguing about what to do with its victim.\n")
     
    tprint(Fore.GREEN + "They disappear inside the tower, and Sam takes a moment to steel himself.\n He cannot leave Frodo to whatever fate these fiends have devised.\n He has to fight for his friend. He draws sting and enters the tower.\n")
     
    mordor_orc_fight()

def mordor_orc_fight():
    global sam_health, mordor_orc_health
    
    while sam_health > 0 and mordor_orc_health > 0:
        tprint(Fore.YELLOW + f"Sam's Health: {sam_health}\n")
        tprint(Fore.RED + f"Orcs' Health: {mordor_orc_health}\n")
         
        
        tprint(Fore.GREEN + "Choose your action:\n")
        tprint(Fore.RED + "1. Strike\n")
        tprint(Fore.GREEN + "2. Block\n")
        tprint(Fore.YELLOW + "3. Heal\n")
        
        choice = input(Fore.GREEN + "Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            damage = random.randint(10, 20)
            mordor_orc_health -= damage
            tprint(Fore.RED + f"Sam strikes the orcs and deals {damage} damage!\n")
             
            if mordor_orc_health > 0:
                tprint(Fore.RED + "Orcs: AAARRGH!!!!!!\n")
                 
        elif choice == '2':
            block = random.randint(5, 15)
            tprint(Fore.GREEN + f"Sam blocks and will reduce the next attack by {block} damage.\n")
             
        elif choice == '3':
            heal = random.randint(10, 20)
            sam_health += heal
            tprint(Fore.YELLOW + f"Sam heals himself for {heal} health.\n")
             
        else:
            tprint(Fore.RED + "Invalid choice. Please enter 1, 2, or 3.\n")
            continue
        
        if mordor_orc_health <= 0:
            tprint(Fore.GREEN + "The orcs are defeated. Sam rushes to your side.\n")
             
            break

        mordor_orc_damage = random.randint(5, 15)
        if choice == '2':
            mordor_orc_damage -= block
            if mordor_orc_damage < 0:
                mordor_orc_damage = 0
        sam_health -= mordor_orc_damage
        tprint(Fore.RED + f"The orcs strike and deal {mordor_orc_damage} damage!\n")
         
    
    if sam_health > 0:
        to_mount_doom()        
    else:
        tprint(Fore.RED + "Sam has been defeated by the orcs. Middle-earth's fate grows darker.\n")
        quit()

def to_mount_doom():
    tprint(Fore.LIGHTMAGENTA_EX + 'Sam: "Mr Frodo! Thank goodness I\'ve found you. Those orcs, they was gonna hand you over to the Dark Lord."\n')
     
    tprint(Fore.YELLOW + 'You: "Yes, Thank goodness, Sam. Help me up, would you? They took all my things, even my chain necklace with the..."\n')
     
    tprint(Fore.LIGHTMAGENTA_EX + 'Sam: "...It\'s okay, Mr Frodo. I found all your clothes.\n They had everything wrapped up in some kind of webbing.\n The chain was entangled in that sticky mess. Here, let me help you."\n')
     
    tprint(Fore.GREEN + "You redress quickly, then decide it would be better to be disguised as orcs,\n and so you and Sam pick through the bodies of the orcs Sam killed to find some more fitting attire then exit the tower,\n seeing the burning peak of a volcano in the distance.\n")
     
    tprint(Fore.YELLOW + 'You: "That is where we have to go, Sam. Mount Doom. We still have a long way to go,\n and I fear this step of our journey will be the most perilous."\n')
     
    tprint(Fore.GREEN + "Sam, as ever, is all business.\n")
     
    tprint(Fore.LIGHTMAGENTA_EX + 'Sam: "Let\'s get to it then, Mr Frodo. The sooner we get this done, the sooner we can get home."\n')
     
    tprint(Fore.GREEN + "Dear Sam. You would not have made it this far without him, but you fear there may be no return. Even if you succeed.\n")
     
    tprint(Fore.GREEN + "It takes you five days to cross the black, orc-infested lands of Mordor,\n but eventually, you arrive at the base of Orodruin, the Mountain of Fire, your goal.\n")
     
    tprint(Fore.GREEN + "It's strange, you think, how so near to the end of your journey you are, but yet so far,\n as you wander towards the snake-like path sloping slowly upwards toward a cave entrance halfway up the volcano.\n With each step since you left the orc tower, you have been feeling your footsteps get heavier and heavier,\n as if you are carrying a ships' anchor chain around your neck.\n")
     
    tprint(Fore.GREEN + "You are almost to your destination when, from the Black Tower of Barad Dur,\n you feel the gaze of Sauron shift towards you. You duck down, yelling for Sam to do the same. The Dark Lord is searching for you.\n Will he find you? The answer feels like it could be decided on a dice roll...\n")
    saurons_gaze()

def saurons_gaze():

    input(Fore.GREEN + "Press Enter to roll the dice...\n")
    tprint(Fore.GREEN + "Rolling the dice...\n")
     

    roll = random.randint(1, 20)

    if roll > 10:
        tprint(Fore.GREEN + "You have escaped Sauron's gaze.\n")
         
        tprint(Fore.YELLOW + 'Sam: "That was close!"\n')
         
        the_final_decision()
    else:
        tprint(Fore.RED + "Sauron's gaze glares right at you. You are frozen in the sight of the great Eye.\n You watch in horror as a huge shape manifests in front of you. Sauron himself has come.")
         
        final_combat_sequence()

def final_combat_sequence():
    global frodo_health, sam_health, sauron_health
    sam_health = 100
    frodo_health = 100
    
    while frodo_health > 0 and sam_health > 0 and sauron_health > 0:
        tprint(Fore.GREEN + f"Frodo's Health: {frodo_health}\n")
        tprint(Fore.YELLOW + f"Sam's Health: {sam_health}\n")
        tprint(Fore.RED + f"Sauron's Health: {sauron_health}\n")
         
        
        tprint(Fore.YELLOW + "Frodo's turn. Choose your action:\n")
        tprint(Fore.RED + "1. Strike\n")
        tprint(Fore.GREEN + "2. Block\n")
        tprint(Fore.YELLOW + "3. Heal\n")
        
        frodo_choice = input("Enter your choice (1, 2, or 3): ")
        
        if frodo_choice == '1':
            damage = random.randint(15, 25)  
            sauron_health -= damage
            tprint(Fore.GREEN + f"Frodo strikes Sauron and deals {damage} damage!\n")
             
        elif frodo_choice == '2':
            block = random.randint(5, 15)
            tprint(Fore.GREEN + f"Frodo blocks and will reduce the next attack by {block} damage.\n")
             
        elif frodo_choice == '3':
            heal = random.randint(10, 20)
            frodo_health += heal
            tprint(Fore.GREEN + f"Frodo heals himself for {heal} health.\n")
             
        else:
            tprint(Fore.RED + "Invalid choice. Please enter 1, 2, or 3.\n")
            continue
        
        if sauron_health <= 0:
            break
        
        tprint("Sam's turn. He strikes Sauron!\n")
        sam_damage = random.randint(10, 20)
        sauron_health -= sam_damage
        tprint(Fore.YELLOW + f"Sam strikes Sauron and deals {sam_damage} damage!\n")
         
        
        if sauron_health <= 0:
            break
        
        sauron_damage = random.randint(10, 25)  
        if sam_health > 0:
            sam_health -= sauron_damage
            tprint(Fore.RED + f"Sauron strikes Sam and deals {sauron_damage} damage!\n")
        else:
            if frodo_choice == '2':
                sauron_damage -= block
                if sauron_damage < 0:
                    sauron_damage = 0
            frodo_health -= sauron_damage
            tprint(Fore.RED + f"Sauron strikes Frodo and deals {sauron_damage} damage!\n")
         

     
        if sauron_health <= 100 and sauron_health > 50:
            tprint(Fore.RED + '"Sauron: You are strong, for vermin. But you will still fail!"\n')
        elif sauron_health <= 50 and sauron_health > 20:
            tprint(Fore.RED + '"Sauron: No! This cannot be! You will not defeat me! I am the true lord of this world, THE ONE TO RULE THEM ALL!"\n')
        elif sauron_health <= 20:
            tprint(Fore.RED + '"Sauron: This is impossible! I am the Dark Lord! I REFUSE TO LOSE TO A PAIR OF NOBODIES!!"\n')
         
    
    if sauron_health <= 0:
        tprint(Fore.GREEN + "You have defeated Sauron!\n")
         
        tprint(Fore.RED + '"Sauron: No... This cannot be... I cannot be defeated by mere hobbits..."\n')
         
        tprint(Fore.RED + '"Sauron: This is not the end... I REFUSE TO BE DEFEATED BY FILTHY HOBBITS!!! I will return...I WILL RETURN... AAAAAARRRRRGGGHHH!!!"\n')
         
        tprint(Fore.LIGHTMAGENTA_EX + '"Sam: We did it, Mr. Frodo! We really did it!"\n')
         
        tprint(Fore.YELLOW + '"You: It is not over yet Sam, that was just his body.\n We need to throw this cursed...Precious...thing into the fire, and save Middle-earth..."\n')
         
        tprint(Fore.GREEN + "You climb the rest of the way to the cavern, renewed by your victory.\n You spy Gollum lurking off to the side and offer him a wry smile. The call of the ring is much quieter now.\n You march into the mountain and pull the ring from its chain.\n")
         
        tprint(Fore.YELLOW + 'You: "This is it, Sam. we are finally free of it.\n"')
         
        tprint(Fore.GREEN + "You hurl the ring into the torrent of molten rock.\n You think there may have been an explosion,\n but you are too tired to care as the world dims.\n")
         
        epilogue()
    else:
        tprint(Fore.RED + "You have been defeated by Sauron.\n Middle-earth's fate grows darker.\n")
         

def the_final_decision():
    tprint(Fore.GREEN + "You have the ring. You have walked it hundreds of miles with Sam to Mordor.\n In the cavern halfway up the volcano lies your destination, and perhaps, a final choice.\n")
     
    your_choice()

def your_choice():
    tprint(Fore.GREEN + "What will be your choice?\n Throw the ring into the fire, or keep it?\n")
    tprint(Fore.RED + "1. Throw the ring into the fire.\n")
    tprint(Fore.GREEN + "2. Keep the ring for yourself.\n")

    the_ring = input(Fore.GREEN + "Do you want to throw or keep the ring?: \n")
    if the_ring == '1':
        tprint(Fore.GREEN + "Before you can throw the ring, the creature, Gollum,\n sneaks up behind you and hits you with a rock. He snatches the ring from you and,\n whirling in celebration, flees the cavern with his prize.")
         
        tprint(Fore.GREEN + "Both you and Sam are too exhausted to give chase. Gollum has doomed Middle-earth.\n Your quest is over. You have failed.\n")
        quit()
    elif the_ring == '2':
        tprint(Fore.GREEN + "You place it on your finger. The world shifts into that now-familiar blur,\n and you start walking to the cavern entrance.\n The creature, Gollum, rises behind Sam with a rock in hand and bashes Sam unconscious.\n He looks about on the floor, and, too late, you realise he is looking for your footprints.\n")
         
        tprint(Fore.GREEN + "Gollum pounces on top of you. Struggling, you fight to maintain your balance as he grips you around the chest with powerful legs,\n and pulls your hand up and back. You stumble towards the edge of the volcano's river of molten rock.\n")
         
        tprint(Fore.GREEN + "A cry escapes you as a bolt of agony shoots from your hand.\n Your finger. Your view returns to normal as Gollum releases you.\n He is holding... YOUR FINGER...\n")
         
        tprint(Fore.GREEN + "You launch yourself at the miserable creature. How dare he take what is rightfully yours.\n Your thoughts are not for your finger. As you close on him,\n Gollum trips backward over a small rock, and without warning, you are falling straight forward.\n")
         
        tprint(Fore.GREEN + "Suddenly, Sam's face is above you, his outstretched hand gripping your arm,\n and you are pulled up and over onto the ledge as Gollum falls, clutching his precious.\n And with a look of unadulterated joy, he plunges into the fiery chasm and the lava below.\n")
         
        tprint(Fore.GREEN + "The war... is over!\n")
        sleep(15)
        epilogue()
    else:
        tprint(Fore.RED + "Invalid choice. Please enter 1 or 2.\n")
        the_ring()

def epilogue():
    tprint(Fore.GREEN + "You awaken from a dream of bright skies and sunlit fields to a strange silence.\n You are in a tent of white, on a bed of soft furs. You glance down at your now-bandaged hand. Oddly, you feel no pain.\n None at all. No aching bones, no soreness in your hand. A head pokes through the tent flap, but before you can make out who it is, they are gone.\n")
     
    tprint(Fore.GREEN + "You hear curt commands, muffled by the tent, and sit up. Slowly,\n checking each movement, you rise from the bed. You have been dressed in a white robe, and,\n still marvelling at its embroidery, you pull back the tent flap and step outside.\n")
     
    tprint(Fore.GREEN + "The noise that greets you is deafening.\n Your companions stand in front of an army of men, every man's eyes on you,\n and the cheer they are sending up washes over you like a summer storm.\n")
     
    tprint(Fore.GREEN + "Gandalf is the first to step forward.\n")
     
    tprint(Fore.CYAN + 'Gandalf: "Well done, Frodo Baggins. The whole of Middle-earth is in your debt.\n The great evil of this age is now past, and a brighter future now awaits us all."\n')
     
    tprint(Fore.GREEN + "Aragorn, a crown now upon his brow, approaches you and kneels. The crowd falls silent.\n")
     
    tprint(Fore.CYAN + 'Aragorn: "There are no words of thanks strong enough to display my appreciation,\n nor my joy at seeing you again, Frodo. Your efforts have beggared us all.\n If there is any wish within my power to grant, ask it, and shall be yours."\n')
     
    tprint(Fore.YELLOW + 'You: I... just want to go home. To the Shire"\n')
     
    tprint(Fore.GREEN + "Aragorn rises and half-turns.\n")
     
    tprint(Fore.CYAN + 'Aragorn: "And return you shall. IN GLORY! WHAT SAY YOU?"\n')
     
    tprint(Fore.GREEN + "The crowd roars again, clashing swords on shields and banging cups of wine.\n")
     
    tprint(Fore.GREEN + "Sam sidles up to you.\n")
     
    tprint(Fore.LIGHTMAGENTA_EX + 'Sam: "Well, I hope it ain\'t gonna take too long.\n My old gaffer will be beside himself by now. He must think I\'ve fallen off the face of the world."\n')
     
    tprint(Fore.GREEN + "Two months, a coronation and a marriage later, you arrive on the outskirts of Hobbiton,\n looking down the hill towards Bag End.\n")
     
    tprint(Fore.LIGHTMAGENTA_EX + 'Sam: "Well. We\'re back."\n')
     
    tprint(Fore.GREEN + "THE END\n")
     
    tprint(Fore.BLUE + "Thank you for playing our little game. We hope you enjoyed it.\n")


display_intro()