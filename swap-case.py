def swap_case(s):
    swapped = ""
    for x in s:
        if x.isupper():
            swapped += x.lower()
        else:
            swapped += x.upper()
    return swapped


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
