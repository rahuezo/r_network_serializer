import rpy2.robjects as ro


def to_listvector(tlist):
    return ro.ListVector(tlist)

def rserialize(robject):
    return ro.r("serialize({}, NULL)".format(robject.r_repr()))
