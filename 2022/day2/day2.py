#!/usr/bin/env python3

# OP ME : Value
# A X : Rock 1
# B Y : Paper 2
# C Z : Scissors 3

part_2_strat = {
    "X": { # Lose
        "A": "Z",
        "B": "X",
        "C": "Y"
    },
    "Y": { # Draw
        "A": "X",
        "B": "Y",
        "C": "Z"
    },
    "Z": { # Win
        "A": "Y",
        "B": "Z",
        "C": "X"
    }
}

def score(s):
    match s:
        case "A X":
            return 1 + 3 # Drasw
        case "B X":
            return 1 + 0 # Lose
        case "C X":
            return 1 + 6 # Win
        case "A Y": ###############
            return 2 + 6 # Win
        case "B Y":
            return 2 + 3 # Draw
        case "C Y":
            return 2 + 0 # Lose
        case "A Z": ###############
            return 3 + 0 # Lose
        case "B Z":
            return 3 + 6 # Win
        case "C Z":
            return 3 + 3 # Draw

def part_2_score(s):
    return score(f"{s[0]} {part_2_strat[s[2]][s[0]]}")

def main():
    fd = open("input.txt")
    a_score = 0
    b_score = 0

    while True:
        s = fd.readline().rstrip("\n")
        if len(s) == 0:
            break
        a_score += score(s)
        b_score += part_2_score(s)
    print(f"A Strat = {a_score}")
    print(f"B Strat = {b_score}")
    fd.close()
    return

if __name__ == "__main__":
    main()