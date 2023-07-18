import random, os

run = True



player = {
    'str':0,
    'dex':0,
    'wis':0,
    'hp':0,
    'food':10,
    'gold':10,
    'name':'',
    'pos':74,
    'inventory':{},
    'weapon':{'name':'fist','damage':'1'},
    'armor':{}
}


map = [
        0,0,0,1,0,0,0,0,0,0,
        0,0,1,9,1,0,0,0,2,0,
        0,0,1,1,0,0,0,0,0,0,
        0,0,1,1,0,1,0,0,0,0,
        0,0,0,0,1,0,1,0,0,0,
        0,0,0,1,1,1,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,2,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,

      ]


towns = {

    75:{
        'name': 'Crisop',
        'buildings': {
                'Green Dragon Inn':{
                'name':'Green Dragon Inn',
                'type':'Inn',
                'description': 'The inn is tight and crammed inbetween to taller houses. The common room is smokey and a fire roars in the corner.'+
                'The inn keeper looks at you, a brawly fellow with an eye patch, "aye what can I get for you?"',
                'cost': 3,
                'rumors':["Listen up, lads and lasses! I've heard whispers from a weary traveler that a long-lost tomb has been unearthed deep within the nearby cursed forest. They say it's filled with ancient treasures and guarded by restless spirits. Who among you dares to delve into the darkness and claim the riches that lie within?"]
                },
                "Ballads Goods":{
                'name':'Ballads Goods',
                'type':'Store',
                'description': 'Most of the shelfs were stocked with a mess of goods ranging from common kitchen implements to rusty daggers. The owner is a portly fellow inspecting a jewl with great interest.',
                'goods':{ 'dagger':{'name':'dagger','cost':4, 'damage': 2, 'type':'weapon'}, 'longsword': {'name': 'longsword', 'cost': 8, 'damage': 6, 'type': 'weapon'}}
                }
        }
    }

}


dungeons = {


    13:{
        'name':'Lost Tomb',
        'start': 12,
        'map':[
            0,0,0,0,0,0,0,0,0,0,
            0,0,2,0,0,0,0,0,0,0,
            0,0,1,0,0,0,0,0,0,0,
            0,0,1,1,1,1,1,1,2,0,
            0,0,0,1,0,0,0,0,0,0,
            0,0,0,1,0,0,0,0,0,0,
            0,0,0,2,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
        ],
        'randomEncounters':[['lich servator',30]],

        'rooms':{
            12: {
                'description':'You are in an empty room, the walls are made of stone. It appears to be very old and is crumbling around you.',
                'exits': 'south',
                'items':[],
                'enemies':[]
            },
            63: {
                'description':'The room appears to be some kind of a make shift barracks. There are several torn bed rolls and weapons strewn about the room along with a collection of supplies and maps.',
                'exits': 'north',
                'items':[{'name': 'satchel of rations', 'cost': 4, 'type': 'loot', 'effect':'20 food'},{'name': 'tattered battle standard', 'cost': 5, 'type':'armor','armor':3}],
                'enemies':[]
            },
            38:{
                'description':'You enter into some form of catacomb. Skeletons and graves line all the walls. In the middle there appears to be some kind of amulet sitting a top podium',
                'exits': 'west',
                'items':[],
                'enemies':[{'name':'Lich','hp':300,
                            'str':20,
                            'dex':18,
                            'wis':18,
                            'gold':500,
                            'weapon':{'name':'Aruers Bane','damage':20},
                            'loot':[{'name': 'Aruers Amulet', 'type':'item'}]
                            }

                        ]
            }
        }
    }




}

enemies = {
    'bandit':{
        'name':'Bandit',
        'hp':10,
        'str':8,
        'dex':8,
        'wis':5,
        'gold':4,
        'weapon':{'name':'sword','damage':'4'},
    },
    'nomad':{
        'name':'Nomad',
        'hp':8,
        'str':12,
        'dex':8,
        'wis':3,
        'gold':2,
        'weapon':{'name':'spear','damage':'5'},
    },
    'lich servator':{
        'name':'Lich Servator',
        'hp':80,
        'str':18,
        'dex':18,
        'wis':16,
        'gold':50,
        'weapon':{'name':'Demon Blade','damage':'12'},

    }
}


def checkWinCondition():
    if('Aruers Amulet' in player['inventory']):
        print("You have succeeded in your quest! A worthy hero indeed you appear to be!")
        run = False


def movement(direction):
    player['food'] -= random.randint(0,1)
    if(direction == 'north'):
        player['pos'] -= 10
    elif(direction == 'south'):
        player['pos'] += 10
    elif(direction == "west"):
        player['pos'] -= 1
    elif(direction == "east"):
        player['pos'] += 1


def genPlayer():
    player['str'] = random.randint(3,18)
    player['dex'] = random.randint(3,18)
    player['wis'] = random.randint(3,18)
    player['hp'] = player['str'] * 2
    player['name'] = input("Enter thy name: ")



def printStats():
    print("Strength: " + str(player['str']))
    print("Dexterity: " + str(player['dex']))
    print("Wisdom: " + str(player['wis']))
    print("HP: " + str(player['hp']))
    print("------------------------")
    print("Food: "+ str(player['food']))
    print("Gold: "+ str(player['gold']))
    print("Inventory: " + str(player['inventory']))
    print("Weapon: " + str(player['weapon']))
    print("Armor: " + str(player['armor']))
    print("Overworld Pos: " + str(player['pos']))
    print("------------------------")



def town(index):
    town = towns[index]
    inTown = True
    print("You enter the town of " + town['name'])
    print("The town contains")
    for i in town['buildings']:
        print(town['buildings'][i]['name'])


    while(inTown):
        building = input("Where would you like to visit?. Type 'exit' to leave.")
        if(building in town['buildings']):
            os.system('cls')
            print("------------------------------------------------------")
            printStats()
            if(town['buildings'][building]['type'] == "Inn"):
                Inn = town['buildings'][building]
                print(Inn['description'])
                print("A room is " + str(Inn['cost']) + " per night")
                print("1. Room")
                print('2. Rumors')
                print("3. Exit")
                choice = ''
                while(choice != '3'):
                    choice = input('')
                    if(choice == '1'):
                        if(player['gold'] >= Inn['cost']):
                            player['hp'] = player['str'] * 2
                            print("You feel rested.")
                        else:
                            print("You don't have enough money!")
                    elif(choice == '2'):
                        print(Inn['rumors'][0])
            elif(town['buildings'][building]['type'] == "Store"):
                Store = town['buildings'][building]
                print(Store['description'])
                print("The store contains the following goods")
                for i in Store['goods']:
                    item = Store['goods'][i]
                    print(item['name'] + ": " + str(item['cost']) +"gp")
                purchase = ''
                while purchase != "exit":
                    purchase = input("Enter the item name you wish to purchase. Type 'exit' to leave.")
                    if purchase in Store['goods']:
                        if player['gold'] >= Store['goods'][purchase]['cost']:
                            print("You purchased a " + purchase)
                            player['gold'] -= Store['goods'][purchase]['cost']
                            player['inventory'][purchase] = Store['goods'][purchase]
        elif(building == 'exit'):
            inTown = False






def dungeon(index):
    dungeon = dungeons[index]
    dungeonMap = dungeon['map']
    inDungeon = True
    playerPosDungeon = dungeon['start']

    print("You enter " + dungeon['name'])
    while inDungeon:
        index = playerPosDungeon
        if(dungeon['map'][index] == 2):
            room = dungeon['rooms'][index]
            print(room['description'])
            if(dungeon['map'][index - 10] == 1):
                print("There is a door to the north")
            if(dungeon['map'][index + 10] == 1):
                print("There is a door to the south")
            if(dungeon['map'][index + 1] == 1):
                print("There is a door to the east")
            if(dungeon['map'][index - 1] == 1):
                print("There is a door to the west")
            for i in room['enemies']:
                combat(i)

        elif(dungeon['map'][index] == 1):
            print("You are in a damp stone corridor")
            if(dungeon['map'][index - 10] == 1):
                print("There is a cooridor to the north")
            if(dungeon['map'][index + 10] == 1):
                print("There is a cooridor to the south")
            if(dungeon['map'][index + 1] == 1):
                print("There is a cooridor to the east")
            if(dungeon['map'][index - 1] == 1):
                print("There is a cooridor to the west")

            if(dungeon['map'][index - 10] == 2):
                print("There is a door to the north")
            if(dungeon['map'][index + 10] == 2):
                print("There is a door to the south")
            if(dungeon['map'][index + 1] == 2):
                print("There is a door to the east")
            if(dungeon['map'][index - 1] == 2):
                print("There is a door to the west")


        action = input("What do you want to do?: ")
        os.system('cls')
        print("------------------------------------------------------")
        printStats()
        if(action.upper() == "NORTH"):
            move = playerPosDungeon - 10
            player['food'] -= 1
            if(dungeon['map'][move] != 0):
                playerPosDungeon = move
            else:
                print("You cannot move that way.")
        elif(action.upper() == "EAST"):
            move = playerPosDungeon + 1
            player['food'] -= 1
            if(dungeon['map'][move] != 0):
                playerPosDungeon = move
            else:
                print("You cannot move that way.")
        elif(action.upper() == "SOUTH"):
            move = playerPosDungeon + 10
            player['food'] -= 1
            if(dungeon['map'][move] != 0):
                playerPosDungeon = move
            else:
                print("You cannot move that way.")
        elif(action.upper() == "WEST"):
            move = playerPosDungeon - 1
            player['food'] -= 1
            if(dungeon['map'][move] != 0):
                playerPosDungeon = move
            else:
                print("You cannot move that way.")

        elif(action.upper() == "SEARCH"):
            if(dungeon['map'][index] == 2):
                search = random.randint(1,20) + player['dex'] / 3
                if(search > 13):
                    index = random.randint(0,len(room['items']) - 1)
                    item =  room['items'][index]
                    if(item['name'] not in player['inventory']):
                        print("You find a " + item['name'])
                        player['inventory'][item['name']] = item
        elif(action.upper() == "EXIT"):
            if(index == dungeon['start']):
                inDungeon = False

        for i in dungeon['randomEncounters']:
            enemy = enemies[i[0]]
            chance = i[1]
            randomEncounter(enemy,chance)
        if(player['hp'] <= 0):
            inDungeon = False






def randomEncounter(enemy,chance):
    encounter = random.randint(0,100)
    if(encounter < chance):
        combat(enemy)



def loadEnvironment():
    index = player['pos']
    tile = map[index]

    if(tile == 0):
        enemy = enemies['bandit']
        print("You stand in an empty prairie landscape. The wind is blowing lightly.")
        randomEncounter(enemy,20)
    elif(tile == 1):
        enemy = enemies['nomad']
        print("You're in a forest glade. Animal sounds eminate from the trees around you.")
        randomEncounter(enemy,10)
    elif(tile == 2):
        town(index)
    elif(tile == 9):
        dungeon(index)

    northIndex = index - 10
    eastIndex = index + 1
    southIndex = index + 10
    westIndex = index - 1

    if(map[northIndex] == 0):
        print("To your North is prairie.")
    if(map[eastIndex] == 0):
        print("To your East is prairie.")
    if(map[southIndex] == 0):
        print("To your South is prairie.")
    if(map[westIndex] == 0):
        print("To your West is prairie.")

    if(map[northIndex] == 1):
        print("To your North is a Forest.")
    if(map[eastIndex] == 1):
        print("To your East is a Forest.")
    if(map[southIndex] == 1):
        print("To your South is a Forest.")
    if(map[westIndex] == 1):
        print("To your West is a Forest.")

    if(map[northIndex] == 2):
        print("To your North is a Settlement.")
    if(map[eastIndex] == 2):
        print("To your East is a Settlement.")
    if(map[southIndex] == 2):
        print("To your South is a Settlement.")
    if(map[westIndex] == 2):
        print("To your West is a Settlement.")





def combat(enemy):
    enemyTemp = {'name':enemy['name'],
    'hp':enemy['hp'],
    'str':enemy['str'],
    'dex':enemy['dex'],
    'wis':enemy['wis'],
    'gold':enemy['gold'],
    'weapon':enemy['weapon']
    }
    input("You are in combat with a " + enemyTemp['name'])
    while(enemyTemp['hp'] > 0 and player['hp'] > 0):
        os.system('cls')
        print("------------------------------------------------------")
        printStats()
        damage = random.randint(0,enemyTemp['str']) + enemyTemp['str'] / 5 + int(enemyTemp['weapon']['damage'])
        playerDamage = random.randint(0,player['str']) + player['str'] / 5 + int(player['weapon']['damage'])
        print(enemyTemp['name'] + " attacks you doing " + str(damage) + " damage.")
        print("You attack the " + enemyTemp['name'] + " doing " + str(playerDamage) + " damage.")
        choice = input("What do you want to do?")
        enemyTemp['hp'] -= playerDamage
        player['hp'] -= damage

    if(enemyTemp['hp'] <= 0):
        print(enemyTemp['name'] + " is dead. ")
        print(enemyTemp['name'] + " drops " + str(enemyTemp['gold']) + " gold!")
        if('loot' in enemy):
            for i in enemy['loot']:
                name = i['name']
                player['inventory'][name] = i
        player['gold'] += enemyTemp['gold']





def getPlayerInput():
    command = ''

    command = input("What do you want to do?: ")


    if(command.upper() == 'NORTH'):
        movement('north')
    elif(command.upper() == "SOUTH"):
        movement('south')
    elif(command.upper() == "WEST"):
        movement('west')
    elif(command.upper() == "EAST"):
        movement('east')
    elif(command.upper().split(" ")[0] == "EQUIP"):
        item = command.split(" ")[1]
        if(item in player['inventory']):
            if(player['inventory'][item]['type']=="weapon"):
                player['weapon'] = player['inventory'][item]
            elif(player['inventory'][item]['type']=="armor"):
                player['armor'] = player['inventory'][item]
            else:
                print("You cannot equip that.")
    elif(command.upper() == "HELP"):
        print("--------------------")
def playerState():
    global run
    if player['food'] <= 0:
        print("You starved to death!")
        run = False
    elif player['hp'] <= 0:
        print("You died!")
        run = False


def game():
    os.system('cls')
    print("------------------------------------------------------")
    printStats()
    loadEnvironment()
    playerState()
    getPlayerInput()
    checkWinCondition()






genPlayer()
while run:
    game()
