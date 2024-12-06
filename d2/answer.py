with open("puzzle_input.txt") as fil:
    boxes = [line.strip() for line in fil]

total_wrapping_needed = 0
ribbon_needed = 0

for box in boxes:
    l, w, h = sorted(map(int, box.split("x")))
    total_wrapping_needed += 2 * (l * w + w * h + h * l) + l * w
    ribbon_needed += 2 * (l + w) + l * w * h

print(f"Part 1 answer is {total_wrapping_needed}")
print(f"Part 2 answer is {ribbon_needed}")
