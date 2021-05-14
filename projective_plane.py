"""
We will build projective plane on top of affine enriching with points in infinity.
The same point is attached for each equivalence class induced by relation
of parallelity on affine lines and one line of all these points.

Since projective plane is also a symmetric design with parameters (n^2+n+1, n+1, 1),
the minimum distance between rows is equal to 2*(n+1 - 1) = 2*n.
"""
from affine_plane import AffinePlane


class ProjectivePlane(AffinePlane):

    def __init__(self, n):
        super().__init__(n, sort_parallel=True)
        self.add_points_in_infinity(n)
        # as a projective plane is also a symmetric design
        self.block_len = n**2 + n + 1
        self.block_pts = n + 1
        self.mindist = 2*n

    def add_points_in_infinity(self, n):
        # incidence matrix is sorted so we simply need to
        # for each point in infinity extend next n lines by the same point
        for i in range(n+1):
            for line in self.incidence_matrix[(i*n):((i+1)*n)]:
                extension = [0 for _ in range(n+1)]
                extension[i] = 1
                line += extension

        # and add line in infinity
        self.incidence_matrix.append([0 for _ in range(n**2)] + [1 for _ in range(n + 1)])
