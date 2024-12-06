with open("puzzle_input.txt", "r") as fil:
    parentheses = fil.readlines()

up_floors = parentheses[0].count("(")
down_floors = parentheses[0].count(")")

print(f"Part 1 answer is {up_floors - down_floors}")

floor = 0
for charid, char in enumerate(parentheses[0]):
    if char == "(":
        floor += 1
    else:
        floor -= 1

    if floor == -1:
        # Puzzle say start counting from 1
        print(f"Part 2 answer is {charid + 1}")
        break
