import rpy2.robjects as ro


def rserialize(robject):
    return ro.r("serialize({}, NULL)".format(robject.r_repr()))
