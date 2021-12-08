DIGITS="abcdefg"
MAPPING={
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9
    }

def main():
    with open("input") as fileh:
        total = 0
        for line in fileh:
            samples, _, output = line.strip().partition(" | ")
            key = find_key(samples.split(" ") + output.split(" "))
            total += decode(key, output)
            print(f"{output}: {decode(key, output)}")
        return total


def find_key(scrambled):
    possible = dict((digit, set(DIGITS)) for digit in DIGITS)
    last = sum(len(v) for v in possible.values())
    for f in (eliminate_two_three_four, eliminate_fives, eliminate_sixes, figure_out_cf):
        f(scrambled, possible)
        eliminate_subsets(possible)
    assert sum(len(v) for v in possible.values()) == len(DIGITS)
    return dict((min(v), k) for k, v in possible.items())


def decode(key, scrambled):
    output = ""
    for digit in scrambled.split(" "):
        output += str(MAPPING["".join(sorted(key[d] for d in digit))])
    return int(output)


def eliminate_subsets(possible):
    # if there are any pairs in possible, this removes them as possibilities from other digits
    pairs = [x for x in possible.values() if len(x) == 2]
    for pair in pairs:
        if pairs.count(pair) == 2:
            eliminate_from(set(pair), "abcdefg", possible, not_for=pair)
    for single in [min(y) for y in possible.values() if len(y) == 1]:
        eliminate_from(set(single), "abcdefg", possible, not_for=set(single))


def eliminate_fives(scrambled, possible):
    # all len(5)s have 3 digits in common, these map to a,d,g
    fives = [x for x in scrambled if len(x) == 5]
    if len(fives) > 1:
        common = set(fives[0])
        for f in fives[1:]:
            common &= set(f)
        if len(common) == 3:
            eliminate_from(common, "bcef", possible)


def eliminate_sixes(scrambled, possible):
    # all len(6)s have 5 digits in common, these map to a,b,d,f,g
    sixes = [x for x in scrambled if len(x) == 6]
    if len(sixes) > 1:
        common = set(sixes[0])
        for s in sixes[1:]:
            common &= set(s)
        if len(common) == 5:
            eliminate_from(common, "ce", possible)
        

def eliminate_two_three_four(scrambled, possible):
    for s in sorted(scrambled, key=lambda s: len(s)):
        if len(s) == 2:
            # this is a 1 so it removes these digits from being possible
            # on a, b, d, e, g
            eliminate_from(s, "abdeg", possible)
        elif len(s) == 3:
            eliminate_from(s, "bdeg", possible)
        elif len(s) == 4:
            eliminate_from(s, "aeg", possible)


def figure_out_cf(scrambled, possible):
    # if e is known I can figure out what c should be based on fives
    if len(possible['e']) == 1:
        fives = [x for x in scrambled if len(x) == 5]
        for five in fives:
            if list(possible['e'])[0] in five:
                # this is a 2, so c is present in here too!
                possible['c'] &= set(five)


def eliminate_from(digits, possibilities, possible, not_for=None):
    for d in digits:
        for p in possibilities:
            if possible[p] != not_for and d in possible[p]:
                possible[p].remove(d)

if __name__ == "__main__":
    print(main())
