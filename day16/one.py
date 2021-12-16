class Packet():
    def __init__(self, bits):
        self.version, self.type, self.bits = int(bits[0:3], 2), int(bits[3:6], 2), bits[6:]
        self.literal = self._literal()
        #print(f"parsed {self.version=} {self.type=} {self.literal=}")
        self.children = list(self._children())

    def _literal(self):
        if self.type == 4:
            nibbles = ""
            while self.bits:
                nibble, self.bits = self.bits[:5], self.bits[5:]
                nibbles += nibble[1:]
                if nibble[0] == "0":
                    break
            return int(nibbles, 2)
    
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

    def version_sum(self):
        return self.version + sum(c.version_sum() for c in self.children)


def versions(filename):
    return Packet(bin(int(open(filename).read().strip(), 16))[2:]).version_sum()

if __name__ == "__main__":
    assert versions("example") == 6
    assert versions("example2") == 14
    print(versions("input"))
