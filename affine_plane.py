"""
We build affine plane in two phase process:
first, we assume nonzero coefficient by y variable,
second, conversely we retrieve "vertical" lines.
Additionally method sort_parallel used when projective plane is built,
rearranges incidence matrix in such a way that n successive
blocks (lines) are parallel to each other thus lines indexed by
k*n, ..., (k+1)*n establish equivalence class (for k=0, ..., n).

Minimal distance is equal to 2*n-2: given two lines of n points consider two cases:
i) If they are parallel, then they differ at 2*n positions and remaining n^2 - 2*n
positions represent elements of space belonging to any of them.
ii) If they intersect it is clear that they differ in 2 less positions than above.
"""
from utils import block_to_row, is_parallel


class AffinePlane:

    def __init__(self, n, sort_parallel=False):
        self.incidence_matrix = []
        self.fill_matrix(n, sort_parallel)
        self.block_len = n**2
        self.block_pts = n
        self.mindist = 2*n - 2

    def fill_matrix(self, n, sort_parallel):
        # we use mapping (x, y) -> x*n + y to encode pair (x, y) as element of {0, ..., n^2-1}
        for b in range(n):
            for a in range(n):
                block = [x*n + (a*x + b) % n for x in range(n)]
                self.incidence_matrix.append(block_to_row(block, n**2))
            block = [b*n + y for y in range(n)]
            self.incidence_matrix.append(block_to_row(block, n**2))

        if sort_parallel:
            self.sort_parallel(n)

    def sort_parallel(self, n):
        for cls in range(n):  # there is n+1 classes but the last one would be "found" if we have found others

            # pick a representative of cls
            idx_repr = cls*n

            idx_to_swap = cls*n + 1
            idx_to_check = cls*n + 1

            # and search for its remaining n-1 parallel friends
            while idx_to_swap - idx_repr < n:
                if is_parallel(self.incidence_matrix[idx_repr], self.incidence_matrix[idx_to_check]):
                    tmp = self.incidence_matrix[idx_to_swap]
                    self.incidence_matrix[idx_to_swap] = self.incidence_matrix[idx_to_check]
                    self.incidence_matrix[idx_to_check] = tmp
                    idx_to_swap += 1
                idx_to_check += 1

    def print_matrix(self):
        for idx, row in enumerate(self.incidence_matrix):
            print(row)
