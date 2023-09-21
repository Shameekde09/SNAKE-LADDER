import  random
snakes={29:9,38:15,47:5,53:33,62:37,86:54,92:70,97:25}
ladders={2:23,8:34,20:77,32:68,41:79,82:100,85:95}
player_position=1
def rolldice():
    return random.randint(1,6)



while player_position<100:
    input("Press Enter to roll the dice for player 1 ---->>>> \n")
    dice=rolldice()
    print("your dice number is -->> ",dice)
    player_position +=dice
    print("\n")




    if player_position in snakes:
        print("snake!! move to -->> ",snakes[player_position])
        player_position=snakes[player_position]
        print("\n")
    elif player_position in ladders:
        print("yess  ladder!! move to---->> \n",ladders[player_position])
        player_position=ladders[player_position]
        print("\n")
    if player_position>100:
        player_position=100
    print("current position is --->> ",player_position)
    print("\n")
    if player_position==100:
        print("congratulations! You have reached the final position ")
        break
