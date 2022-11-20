from samples import food, monkey_king, zoo, game
import random

if __name__ == "__main__":
    m = random.choice([food, monkey_king, zoo, game])
    m.madlib()