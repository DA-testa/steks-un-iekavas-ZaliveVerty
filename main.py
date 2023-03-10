# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    last_opening_bracket_index = 0
    
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            last_opening_bracket_index = i + 1

        if next in ")]}":
            if len(opening_brackets_stack) > 0:
                last_open_bracket = opening_brackets_stack.pop()
                if are_matching(last_open_bracket, next):
                    continue

            return i + 1

    if len(opening_brackets_stack) > 0:
        return last_opening_bracket_index

    return 0


def main():
    text = input()
    mismatch = find_mismatch(text)

    if mismatch == 0:
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
