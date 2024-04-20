import random
def main():
    level = get_level()

    print("Score" , generate_integer(level))



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in {1,2,3}:
                break
        except ValueError:
            pass
    return level
def generate_integer(level):
    score = 0
    for ten in range(1,11):
        if level == 1:
            x = random.randint(0,9)
            y = random.randint(0,9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        else:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        count = 0
        while count < 3:
            try:
                guess  = int(input(f"{x} + {y} = "))
                if guess == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    count += 1
                    if count == 3:
                        print(f"{x} + {y} = {x + y}")
                        break
            except ValueError:
                print("EEE")
                count += 1
                pass
    return  score
if __name__ == "__main__":
    main()
