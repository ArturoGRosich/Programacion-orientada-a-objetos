 class Yatzy:

    global ONE, TWO, THREE, FOUR, FIVE, SIX, PAIR
    ONE, TWO, THREE, FOUR, FIVE, SIX = 1, 2, 3, 4, 5, 6
    PAIR = 2


    @staticmethod
    def chance(*dice):
        points = 0

        for die in dice:
            points += die

        return points


    @staticmethod
    def yatzy(*dice):
        
        for die in dice:
            if die != dice[0]:
                return 0

        return 50
    

    @staticmethod
    def ones(*dice):
        points = dice.count(ONE)
        return points


    @staticmethod
    def twos(*dice):
        points = dice.count(TWO) * TWO
        return points
    

    @staticmethod
    def threes(*dice):
        points = dice.count(THREE) * THREE
        return points
    

    @staticmethod
    def fours(*dice):
        points = dice.count(FOUR) * FOUR
        return points


    @staticmethod
    def fives(*dice):
        points = dice.count(FIVE) * FIVE
        return points


    @staticmethod
    def sixes(*dice):
        points = dice.count(SIX) * SIX
        return points
    

    @staticmethod
    def pair(*dice):
    
        for number in range(6, 1, -1):
            if dice.count(number) >= PAIR:
                return number * PAIR
        return 0


    @staticmethod
    def two_pairs(*dice):
        points = 0
        pairs = 0
        for number in range(1, 6):
            if dice.count(number) >= 2:
                points += number * PAIR
                pairs +=1
        if pairs >= 2:
            return points
        return 0


    @staticmethod
    def three_of_a_kind(*dice):
        for die in dice:
            if dice.count(die) >= THREE:
                return die * THREE
        return 0
    

    @staticmethod
    def four_of_a_kind(*dice):
        for die in dice:
            if dice.count(die) >= FOUR:
                return die * FOUR
        return 0
    

    @staticmethod
    def smallStraight(*dice):
        for number in range(1,6):
            if dice.count(number) != 1:
                return 0
        return sum(dice)
    

    @staticmethod
    def largeStraight(*dice):
        for number in range(2,7):
            if dice.count(number) != 1:
                return 0
        return sum(dice)


    @staticmethod
    def fullHouse(*dice):
        
        trio = Yatzy.three_of_a_kind(*dice)
        duo = 0
        
        for number in range(1, 7):
            if dice.count(number) == 2:
                duo = number

        if trio != 0 and duo != 0:
            return (trio + duo*2)
        
        return 0
        
