from collections import defaultdict, Counter

def min_max(filename):
    seq, mappings, start_end = seq_mappings_startend(filename)
    #print(f"{seq=} {mappings=}\n{charcounts(seq, start_end)=}\n{sum(charcounts(seq, start_end).values())=}\n")
    for step in range(40):
        seq = apply_mappings(seq, mappings)
        #print(f"{step=} {seq=} {sum(charcounts(seq, start_end).values())=}")
    cc = charcounts(seq, start_end)
    return max(cc.values()) - min(cc.values())


def charcounts(seq, start_end):
    c = defaultdict(int)
    for key, value in seq.items():
        c[key[0]] += value
        c[key[1]] += value
    c[start_end[0]] += 1
    c[start_end[1]] += 1
    for key in c.keys():
        c[key] = int(c[key]/2)
    return c

def seq_mappings_startend(filename):
    seq, maplines = open(filename).read().split("\n\n")
    start_end = seq[0] + seq[-1]
    maplines = dict(tuple(m.strip().split(" -> ")) for m in maplines.split("\n") if m != "")
    seq = Counter(seq[i:i+2] for i in range(len(seq)-1))
    return seq, maplines, start_end


def apply_mappings(seq, mappings):
    output = Counter()
    for pair, value in seq.items():
        output[pair[0] + mappings[pair]] += value
        output[mappings[pair] + pair[1]] += value
    return output

if __name__ == "__main__":
    assert min_max("example") == 2188189693529
    print(min_max("input"))
