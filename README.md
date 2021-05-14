# Geometric Codes
### Mini-project for the course in Advanced Discrete Mathematics (UJ 2020/2011)


The code in this repository allows the user to generate three types of a combinatorial design:

- affine plane,
- projective plane,
- cyclic design (for prime n=4m-1),

Also enables to use error correction code obtained from the incidence matrix of a chosen one on a given file.

Usage:
```
python main.py -type T N [-mindist] [-correct filename.txt]
```
in cases of affine (T=A) and projective (T=P) planes N is its order while in case of cyclic (T=C) N is a number of elements.
Remaining arguments are optional.

File example.txt demonstrates purpose of the program using the projective plane of order 2:
```
python main.py -type P 2 -correct example.txt
```

