"""
A script that creates text files to create level text files
"""
# NOTE: STILL IN DEVELOPMENT

# Also Looks terrible
# TODO: clean up this code too

def main():
    print("** LEVEL CREATOR ***")
    print("Press ENTER to create level")
    input()

    lvl_num = int(input("Level number: "))
    layout_texts = []
    layout_texts.append(f"n|{lvl_num}")
    choice = -1

    while choice != 0:
        print("\nCREATE:")
        print("1. Player     (in development)")
        print("2. Walls")
        print("3. Obstacle   (in development)")
        print("4. Door & Key (in development)")
        print("5. Goal       (in development)")
        print("0. QUIT")
        
        choice = int(input("> "))

        match choice:
            case 1:
                pass
            case 2:
                layout_texts.append(create_walls())
        
    with open(f"tools/lvl_{lvl_num}.txt", "w") as lvl_file:
        for text in layout_texts:
            lvl_file.write(text + "\n")

def create_walls() -> str:
    num_walls = int(input("Number of walls: "))
    walls_str = f"w"

    for i in range(num_walls):
        while True:
            try:
                print(f"\nWall {i + 1}")
                x = int(input("x: "))
                y = int(input("y: "))
                walls_str += f"|{x},{y}"
                break
            except ValueError:
                continue

    return walls_str

if __name__ == "__main__":
    main()
