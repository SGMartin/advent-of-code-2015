def get_new_position(position, direction):
    moves = {
        ">": (0, 1),
        "<": (0, -1),
        "v": (1, 0),
        "^": (-1, 0),
    }
    return (position[0] + moves[direction][0], position[1] + moves[direction][1])

with open("puzzle_input.txt", "r") as fil:
    directions = fil.read().strip()

# Part 1: Santa
current_pos = (0, 0)
visited_houses = {current_pos}

for direction in directions:
    if direction in ">v<^":
        current_pos = get_new_position(current_pos, direction)
        visited_houses.add(current_pos)

# Part 2: Santa and Robo-Santa
santa_pos, robo_pos = (0, 0), (0, 0)
both_visited_houses = {santa_pos}

for i, direction in enumerate(directions):
    if direction in ">v<^":
        if i % 2 == 0:  # Robo turn
            robo_pos = get_new_position(robo_pos, direction)
            both_visited_houses.add(robo_pos)
        else:  # Santa turn
            santa_pos = get_new_position(santa_pos, direction)
            both_visited_houses.add(santa_pos)

print(f"Part 1 answer is {len(visited_houses)}")
print(f"Part 2 answer is {len(both_visited_houses)}")
