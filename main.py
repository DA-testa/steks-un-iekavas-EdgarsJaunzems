# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))
            # pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i + 1
            pop = opening_brackets_stack.pop()
            if not are_matching(pop.char, next):
                return i + 1
            # pass
    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1
    return "Success"

def main():
    text2 = input()
    # Printing answer, write your code here
    if text2 == "I":
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)
    elif text2 == "F":
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)
    else:
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)

    


if __name__ == "__main__":
    main()
