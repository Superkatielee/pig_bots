 if player == 0:
        # answer = input("Do you want to roll again? (yes/no): ").lower()
        # return answer == "yes"
        if scores[1] + score <= 100:
            return True
        else:
            return False
    else:
        return scores[0] > scores[1] + score or score < 20

def roll_die() :
    return random.randint(1, 6)

def take_turn(player):
