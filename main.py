# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    lastOpeningBracketIndex = 0
    
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            lastOpeningBracketIndex = i

        if next in ")]}":
            lastOpenBracket = opening_brackets_stack.pop()
            if lastOpenBracket is next: continue

            return i + 1

    if len(opening_brackets_stack) > 0:
        return lastOpeningBracketIndex

    return 0


def main():
    text = input()
    mismatch = find_mismatch(text)

    if mismatch is 0:
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
