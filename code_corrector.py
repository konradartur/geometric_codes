"""
We can detect less than mindist errors and correct less than half of it.

Correction is made in a naive way by assessing all valid words distance
to given "non-word" and correcting to that of the least distance.
"""
from utils import hamming_dist


class CodeCorrector:

    def __init__(self, words, word_len, word_ones, mindist):
        self.words = words
        self.word_len = word_len
        self.word_ones = word_ones
        self.mindist = mindist

    def correct(self, non_word):
        assert len(non_word) == self.word_len, "wrong coding scheme selected"

        dists = [hamming_dist(non_word, w) for w in self.words]
        errors = min(dists)

        if errors < self.mindist/2:  # correctable
            corrected = self.words[dists.index(errors)]
            print(f"{non_word} corrected to {corrected})")
        elif errors < self.mindist:  # ambiguous case
            candidates = []

            while True:
                try:
                    idx = dists.index(errors)
                except ValueError:
                    break
                candidates.append(self.words[idx])
                dists.pop(idx)

            print(f"{non_word} is ambiguous, candidates are",
                  *[f"{cand}, " for cand in candidates[:-1]],
                  candidates[-1])
        else:
            print("no correction possible")
