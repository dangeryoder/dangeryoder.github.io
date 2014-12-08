import random
print "Welcome to Blackjack!"
money = 1000
print "You have $",money, "dollars"
cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
random.shuffle(cards)

def print_card(x):
    if x <10:
        print "-----------"
        print "|",x,"       |"
        print "|          |"
        print "|          |"
        print "|      ",x," |"
        print "-----------"
    else:
        print "-----------"
        print "|",x,"      |"
        print "|          |"
        print "|          |"
        print "|      ",x,"|"
        print "-----------"
    return
    
def card_add(sum, x):
    if x < 10:
        sum+=x
    else:
        sum+=10
    return sum
    
for i in range(10):
    print "How much do you want to bet?"
    chip_in = int(raw_input())
    player_sum = 0
    house_sum = 0
    if chip_in > 0 and money-chip_in >= 0:
        player_sum = card_add(player_sum, cards[-1])
        print_card(cards.pop())
        player_sum = card_add(player_sum, cards[-1])
        print_card(cards.pop())
        print "Your point:",player_sum
    while (int(raw_input('Do you need an extra card? (1:yes, 0:no)'))):
        player_sum = card_add(player_sum, cards[-1])
        print_card(cards.pop())
        print "Your point:",player_sum
        if player_sum > 21:
            print "You lose!!!"
            money-=chip_in
            print "Now you have $", money, "dollars"
            break
        elif player_sum == 21:
            print "You Win!!!"
            money+=chip_in*2
            print "Now you have $", money, "dollars"
            break
        else:
            print "Now, it's my turn..."
            house_sum = card_add(house_sum, cards[-1])
            print_card(cards.pop())
            house_sum = card_add(house_sum, cards[-1])
            print_card(cards.pop())
            print "House point:",house_sum
        while (house_sum < 17):
                house_sum = card_add(house_sum, cards[-1])
                print_card(cards.pop())
                print "House point:",house_sum
                if house_sum <= 21 and house_sum > player_sum:
                    print "You lose!!!"
                    money-=chip_in
                    print "Now you have $", money, "dollars"
                    break
                elif house_sum > 21:
                    print "You Win!!!"
                    money+=chip_in
                    print "Now you have $", money, "dollars"  
                    break             
                else:
                    print "You Win!!!"
                    money+=chip_in
                    print "Now you have $", money, "dollars"
                    break
