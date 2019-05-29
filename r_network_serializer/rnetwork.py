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
        self.name = self.matrix_file.name
        self.network = self.load_matrix()
        self.serialize_ready = (self.name, self.network)

    def load_matrix(self):
        if self.matrix_file:
            reader = csv.reader(self.matrix_file, delimiter=",")
            header = filter(lambda x: len(x) > 0, reader.next())

            rows = [[0 if len(col) == 0 else col for col in row[1:]] for row in reader]

            if RNetwork.is_square(rows):
                matrix = np.array(rows)

                self.network = rnetwork.network(ro.r.matrix(matrix, nrow=matrix.shape[0], ncol=matrix.shape[1]),
                                                matrix_type="adjacency", ignore_eval=False, names_eval="like")

                self.network = ro.r("`network.vertex.names<-`")(self.network, ro.StrVector(header))

                return self.network