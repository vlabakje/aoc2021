from collections import Counter

def min_max(filename):
    seq, mappings = seq_mappings(filename)
    print(f"{seq=} {mappings=}")
    for step in range(10):
        seq = apply_mappings(seq, mappings)
        print(f"{step=} {seq[:90]=}")
    c = Counter(seq)
    print(f"{max(c.values())=} {min(c.values())=} {c=}")
    return max(c.values()) - min(c.values())


def seq_mappings(filename):
    seq, maplines = open(filename).read().split("\n\n")
    return seq, dict(tuple(m.strip().split(" -> ")) for m in maplines.split("\n") if m != "")


def apply_mappings(seq, mappings):
    output = seq[0]
    for i in range(len(seq) - 1):
        output += mappings.get(seq[i:i+2], "") + seq[i+1]
        #print(f"{output=} {mappings.get(seq[i:i+2], '')=} {seq[i:i+2]=}")
    return output


if __name__ == "__main__":
    assert min_max("example") == 1588
    print(min_max("input"))
