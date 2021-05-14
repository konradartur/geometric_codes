"""
First we need to find generator g of multiplicative group Zn.
Then we have first block of design {g^2, ..., (g^2)^((n-1)/2)}
and remaining blocks are translation of it by 1 through n-1.

The only case supported is when the order of design is a prime
n of the form 4m-1 so design parameters are (4m-1, 2m-1, m-1),
because length of a block is equal to (n-1)/2.

A cyclic design is also a symmetric thus minimum distance between rows
of incidence matrix is equal to 2*( (2m-1) - (m-1) ) = 2*m (or (n+1)/2).
"""
from utils import is_prime, find_generator, block_to_row, translate_block, block_generated_by


class CyclicDesign:

    def __init__(self, n):
        assert is_prime(n) and n % 4 == 3, "cyclic design supported only for prime n of the form 4m-1"
        self.incidence_matrix = []
        self.fill_matrix(n)
        self.block_len = n  # 4m-1
        self.block_pts = (n-1)//2  # 2m-1
        self.mindist = (n+1)//2  # 2m

    def fill_matrix(self, n):
        g = find_generator(n)
        g_sq = (g*g) % n

        block_0 = block_generated_by(g_sq, n)
        self.incidence_matrix.append(block_to_row(block_0, n))

        for i in range(1, n):
            block_i = translate_block(block_0.copy(), i, n)
            self.incidence_matrix.append(block_to_row(block_i, n))

    def print_matrix(self):
        for row in self.incidence_matrix:
            print(row)
