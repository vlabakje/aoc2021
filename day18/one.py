from dataclasses import dataclass

@dataclass
class Node():
    value: str
    n: "Node" = None

def str_to_nodes(s):
    head, tail = None, None
    cur_int = None
    def add(new):
        nonlocal head, tail
        if head is None:
            head, tail = new, new
        else:
            tail.n, tail = new, new
    for c in s:
        if cur_int:
            if c.isdigit():
                cur_int += c
                continue
            else:
                add(Node(value=int(cur_int)))
                cur_int = None
        if c in "[],":
            add(Node(value=c))
        elif c.isdigit():
            cur_int = c
    return head

def nodes_to_str(head):
    return "".join(str(n.value) for n in iterate_nodes(head))

def test_str_to_nodes():
    VALUES = ("[1,2]", "[[1,2],3]", "[[[[1,2],[3,4]],[[5,6],[7,8]]],9]")
    for v in VALUES:
        assert v == nodes_to_str(str_to_nodes(v))

def add(n1, n2):
    head, comma, tail = Node(value="["), Node(value=","), Node(value="]")
    head.n = n1
    list(iterate_nodes(n1))[-1].n = comma
    comma.n = n2
    list(iterate_nodes(n2))[-1].n = tail
    return reduce(head)

def test_add():
    n1 = str_to_nodes("[[[[4,3],4],4],[7,[[8,4],9]]]")
    n2 = str_to_nodes("[1,1]")
    assert nodes_to_str(add(n1, n2)) == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"

def split(head):
    orig = head
    while head.n:
        if type(head.n.value) == int and head.n.value > 9:
            after = head.n.n
            new = Node(value="[")
            new.n = Node(value=head.n.value//2)
            new.n.n = Node(value=",")
            new.n.n.n = Node(value=int((head.n.value+1)/2))
            new.n.n.n.n = Node(value="]", n=after)
            head.n = new
            #print(f"after split  : {nodes_to_str(orig)}")
            return True
        head = head.n
    return False

def test_split():
    n = str_to_nodes("[15,[0,13]]")
    assert split(n)
    assert nodes_to_str(n) == "[[7,8],[0,13]]"
    assert split(n)
    assert nodes_to_str(n) == "[[7,8],[0,[6,7]]]"

def explode(head):
    orig = head
    level = 0
    last_int = None
    add_to_next = None
    while head.n:
        if add_to_next != None:
            if type(head.value) == int:
                head.value += add_to_next
                break
        elif type(head.value) == int:
            last_int = head
        elif head.value == "[":
            level += 1
            if level == 5:
                if last_int:
                    last_int.value += head.n.value
                add_to_next = head.n.n.n.value
                head.value = 0
                head.n = head.n.n.n.n.n
                head = head.n
                continue
        elif head.value == "]":
            level -= 1
        head = head.n
    return add_to_next != None

def test_explode():
    def e(s, r, second=False):
        n = str_to_nodes(s)
        assert explode(n)
        assert nodes_to_str(n) == r
        assert explode(n) is second
        if not second:
            assert nodes_to_str(n) == r
    e("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]")
    e("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]")
    e("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]")
    e("[[6,[5,[4,[15,2]]]],1]", "[[6,[5,[19,0]]],3]")
    e("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", True)

def reduce(head):
    while explode(head) or split(head):
        pass
    return head

def test_reduce():
    assert nodes_to_str(reduce(str_to_nodes("[[[[[9,8],1],2],3],4]"))) == "[[[[0,9],2],3],4]"

def iterate_nodes(head):
    while head.n:
        yield head
        head = head.n
    yield head
        
def magnitude(head):
    # look for [i, j] and replace with result
    while head.value == "[":
        for node in iterate_nodes(head):
            if (node.value == "[" and
                type(node.n.value) == int and
                node.n.n.value == "," and
                type(node.n.n.n.value) == int):
                # replace with result
                node.value = 3 * node.n.value + 2 * node.n.n.n.value
                node.n = node.n.n.n.n.n
                break
    return head.value

def test_magnitude():
    VALUES = (
            ("[9,1]", 29),
            ("[[1,2],[[3,4],5]]", 143),
            ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
            ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
            ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
            ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
            ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488))
    for i, o in VALUES:
        assert magnitude(str_to_nodes(i)) == o

def add_all(filename):
    lines = open(filename).readlines()
    result = str_to_nodes(lines[0])
    for line in lines[1:]:
        result = add(result, str_to_nodes(line))
    #print(f"final: {nodes_to_str(result)}")
    return magnitude(result)


if __name__ == "__main__":
    print(add_all("input"))
