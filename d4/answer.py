import hashlib

puzzle_input = "bgvyzdsv"

part1_answer = 0
part2_answer = 0
answer = 0

while True:
    attempt_string = f"{puzzle_input}{answer}"
    hashed = hashlib.md5(attempt_string.encode("utf-8")).hexdigest()

    # Find part 1 number
    if part1_answer == 0 and hashed.startswith("00000"):
        part1_answer = answer

    # Find part 2 number
    if hashed.startswith("000000"):
        part2_answer = answer
        break

    answer += 1

    if answer % 100000 == 0:
        print(f"Tried up to {answer}...")


print(f"Part 1 answer is {part1_answer}")
print(f"Part 2 answer is {part2_answer}")
