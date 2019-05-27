import csv, os
import numpy as np

import rpy2.robjects as ro
from rpy2.robjects.packages import importr
import rpy2.robjects.numpy2ri

rpy2.robjects.numpy2ri.activate()

rnetwork = importr("network", on_conflict="warn")


class RNetwork:
    @staticmethod
    def is_square(rows):
        return all([len(row) == len(rows) for row in rows])

    def __init__(self, matrix_file):
        self.matrix_file = matrix_file
        self.name = os.path.split(self.matrix_file)[-1]
        self.network = self.load_matrix()
        self.serialize_ready = (self.name, self.network)

    def load_matrix(self):
        if self.matrix_file:
            with open(self.matrix_file, "rb") as inf:
                reader = csv.reader(inf, delimiter=",")
                header = reader.next()

                rows = [row[1:] for row in reader]

                if RNetwork.is_square(rows):
                    matrix = np.array(rows)

                    self.network = rnetwork.network(ro.r.matrix(matrix, nrow=matrix.shape[0], ncol=matrix.shape[1]),
                                                    matrix_type="adjacency", ignore_eval=False, names_eval="like")

                    self.network = ro.r("`network.vertex.names<-`")(self.network, ro.StrVector(header))

                    return self.network