import netCDF4
from boolparser.core import BoolParser, EvaluateVariable

class ncar(object):
    def __init__(self,var):
        self.var = var
        return
    def __ge__(self, num):
        return self.var>=num
    def __le__(self, num):
        return self.var<=num
    def __gt__(self, num):
        return self.var>num
    def __lt__(self, num):
        return self.var<num
    
def define_class(nc):
    class ev_nc(EvaluateVariable):
        def eval(self):
            if self.value in nc.variables:
                return ncar(nc.variables[self.value][:])
            elif self.value in nc.dimensions:
                return ncar(nc.dimensions[self.value][:])
            else:
                raise NameError("Not a variable: {0}".format(self.value))
                return self.value
    return ev_nc
    
nc = netCDF4.Dataset("mrom2001.nc")

nceval = define_class(nc)

bp   = BoolParser(nceval)


test = """(Profile_lat>=-5.)&(Profile_lat<=5.)&(Profile_lon>0)&(Profile_lon<5)"""

for line in test.split("\n"):
    print line
    res = bp.parse(line)
    print res
    if any(res):
        print nc.variables["Profile_lat"][res]
