import re

from collections import Counter

with open("puzzle_input.txt", "r") as fil:
    words = [strs.rstrip().lower() for strs in fil.readlines()]

nice_counter = 0

for word in words:
    forbidden_exprs = re.findall(pattern="ab|cd|pq|xy", string=word)

    if forbidden_exprs:
        continue

    vowel_count = len(re.findall(pattern="[aeiou]", string=word))
    repeated_chars = re.search(r"(.)\1", word)

    if repeated_chars and vowel_count >= 3:
        nice_counter += 1

print(f"Part 1 answer is {nice_counter}")

# new rules!
next_nice_counter = 0

for word in words:
    non_overlap_twice_appear = re.search(r"(.{2}).*(?=\1)", word)
    repeated_with_one_char = re.search(r"(.).\1", word)

    if non_overlap_twice_appear and repeated_with_one_char:
        next_nice_counter += 1

print(f"Part 1 answer is {next_nice_counter}")