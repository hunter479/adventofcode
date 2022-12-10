#!/usr/bin/env python

def main():
    fd = open("input.txt")
    carry = []
    nb = 0

    while True:
        line = fd.readline()
        if len(line) == 0:
            break
        if line == "\n":
            carry.append(nb)
            nb = 0
            continue
        nb += int(line.rstrip("\n"))
    carry.sort(reverse=True)
    print(f"max_calorie = {max(carry)}")
    print(f"sum top 3 = {sum(carry[:3])}")
    return

if __name__ == "__main__":
    main()