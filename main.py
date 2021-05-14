from affine_plane import AffinePlane
from projective_plane import ProjectivePlane
from cyclic_design import CyclicDesign
from code_corrector import CodeCorrector
import time
import argparse

if __name__ == "__main__":
    t_start = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument('-type', type=str, required=True, dest="design")
    parser.add_argument('n', nargs=1, type=int)
    parser.add_argument('-mindist', action='store_true')
    parser.add_argument('-correct', nargs='?', dest='file', default=None, type=str)
    args = vars(parser.parse_args())

    if args['design'] == "A":
        design = AffinePlane(args["n"][0])
    elif args['design'] == "P":
        design = ProjectivePlane(args["n"][0])
    elif args['design'] == "C":
        design = CyclicDesign(args["n"][0])
    else:
        raise NameError(f"Design of type {args['design']} not supported.")

    design.print_matrix()

    if args["mindist"]:
        print(f"Minimal distance: {design.mindist}")

    if args["file"]:
        print()
        cc = CodeCorrector(design.incidence_matrix, design.block_len, design.block_pts, design.mindist)
        with open(args["file"], newline='\n') as file:
            for line in file:
                line = line[:-1]  # remove newline character
                line = list(map(int, line.split()))
                cc.correct(line)

    t_end = time.time()
    print(f"Running time: {round(t_end-t_start, 4)} seconds")
