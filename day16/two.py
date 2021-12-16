class Packet():
    def __init__(self, bits):
        self.version, self.type, self.bits = int(bits[0:3], 2), int(bits[3:6], 2), bits[6:]
        self.children = list(self._children())
        self.literal = self._literal()
        #print(f"parsed {self.version=} {self.type=} {self.literal=}")

    def _literal(self):
        if self.type == 4:
            nibbles = ""
            while self.bits:
                nibble, self.bits = self.bits[:5], self.bits[5:]
                nibbles += nibble[1:]
                if nibble[0] == "0":
                    break
            return int(nibbles, 2)
        elif self.type == 0:
            return sum(p.literal for p in self.children)
        elif self.type == 1:
            total = self.children[0].literal
            for c in self.children[1:]:
                total *= c.literal
            return total
        elif self.type == 2:
            return min(p.literal for p in self.children)
        elif self.type == 3:
            return max(p.literal for p in self.children)
        elif self.type == 5:
            return 1 if self.children[0].literal > self.children[1].literal else 0
        elif self.type == 6:
            return 1 if self.children[0].literal < self.children[1].literal else 0
        elif self.type == 7:
            return 1 if self.children[0].literal == self.children[1].literal else 0
    
    def _children(self):
        if self.type != 4:
            I, self.bits = self.bits[0], self.bits[1:]
            if I == "0":
                n, self.bits = int(self.bits[:15], 2), self.bits[15:]
                #print(f"parsing {n=} bits of packets")
                yield from self._n_bits_of_packets(n)
            else:
                n, self.bits = int(self.bits[1:11], 2), self.bits[11:]
                #print(f"parsing {n=} subpackets")
                yield from self._n_subpackets(n)

    def _n_bits_of_packets(self, n):
        p_bits, self.bits = self.bits[:n], self.bits[n:]
        while len(p_bits):
            p = Packet(p_bits)
            yield p
            p_bits = p.bits

    def _n_subpackets(self, n):
        for i in range(n):
            p = Packet(self.bits)
            self.bits, p.bits = p.bits, []
            yield p


def literal(filename):
    return Packet(bin(int(open(filename).read().strip(), 16))[2:]).literal

def test(h, value):
    output = Packet(bin(int(h, 16))[2:]).literal
    if output != value:
        print(f"error: {Packet(bin(int(h, 16))[2:]).literal=} != {value}")
    return output == value

if __name__ == "__main__":
    assert test("C200B40A82", 3)
    #assert test("04005AC33890", 54)
    assert test("880086C3E88112", 7)
    assert test("CE00C43D881120", 9)
    assert test("D8005AC2A8F0", 1)
    assert test("F600BC2D8F", 0)
    assert test("9C005AC2F8F0", 0)
    assert test("9C0141080250320F1802104A08", 1)
    print(literal("input"))
