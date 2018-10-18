player_name:()
player_type:("adventurer")("knight")("mage")
player_inventory:()
yes:(mission_task_1)
no:(adventure_1)
what_do:("")
direction:"north""east""south""west"
print("hello there human, what type of badass would you like to be")
print("a ADVENTURER who stares death in the eye of all his travels")
print("a KNIGHT of the kings forces trainedby a master swordsman")
print("or a fine MAGE with spells of fire, snow, and lightning")
def player_type(p):print("")
def mission_option_1(q):yes or no # NOTE:yes or no answer needed
if yes:
    print:("Oh Thank You Young Sir")(player_name)("! I think there are crops in a cart near a troll cave not too far from here")
if no:
    print:("Oh. Well. Then just leave this place")(player_name)("you are no longer welcome")

def player(n):
    if player_type:adventurer
    player=adventurer
    print:intro_one
    if player_type:knight
    player=knight
    print:intro_two
    if player_type:mage
    player=mage
    print:intro_three



intro_one=print("Hello young")(player)("you are in the small town of Nuran. can i ask you your name")
player_name=print("")
print("there isn't much here and we need more crops, can you help")
print:mission_option_1
if yes:
    print:("Oh Thank You Young Sir")(player_name)("! I think there are crops in a cart near a troll cave not too far from here")
if no:
    print:("Oh. Well. Then just leave this place")(player_name)("you are no longer welcome")
def mission_task_1(z):print("the cave is to the north")(player_name)("what direction do you want to go?")
    direction=print("")
    if north:print ("you walk up the path until you see a warning sign,what do you do?")
        print
