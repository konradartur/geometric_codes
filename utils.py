from math import sqrt


def find_generator(n):
    for elem in range(2, n):
        if order_of(elem, n) == n-1:
            return elem
    return None


def order_of(element, mod_n):
    order = 1
    nxt = element
    while nxt != 1 and order <= mod_n:
        order += 1
        nxt = (nxt*element) % mod_n
    return order


def block_generated_by(element, mod_n):
    s = [element]
    nxt = (s[-1] * element) % mod_n
    s.append(nxt)
    while nxt != 1 and nxt != 0:
        nxt = (s[-1] * element) % mod_n
        s.append(nxt)
    return s


def translate_block(block, t, mod_n):
    for i in range(len(block)):
        block[i] = (block[i] + t) % mod_n
    return block


def block_to_row(block, length):
    return [int(i in block) for i in range(length)]


def is_parallel(row1, row2):
    # the same lines are parallel
    if row1 == row2:
        return True
    # otherwise their intersection need to be empty
    intersection = [e1*e2 for e1, e2 in zip(row1, row2)]
    empty = not bool(sum(intersection))
    return empty


def hamming_dist(row1, row2):
    tmp = [1 if e1 != e2 else 0 for e1, e2 in zip(row1, row2)]
    return sum(tmp)


def is_prime(n):
    assert n > 1
    for i in range(2, int(sqrt(n) + 1)):
        if not n % i:
            return False
    return True
