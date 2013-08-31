def getitem(v,d):
    "Returns the value of entry d in v"
    assert d in v.D
    return v.f[d] if d in v.f else 0

def setitem(v,d,val):
    "Set the element of v with label d to be val"
    assert d in v.D
    v.f[d] = val
    return

def equal(u,v):
    "Returns true iff u is equal to v"
    assert u.D == v.D

    _equal = True

    if len(u.f) == 0 & len(v.f) == 0:
        return _equal

    # if value = 0, not required to exist in other vector
    # If value != 0, MUST exist in the other vector

    _equal = __vector_equal(u.f, v.f)
    _equal = _equal & __vector_equal(v.f, u.f)

    return _equal

def __vector_equal(vector1, vector2):
    __equals = True
    for element in vector1:
        if vector1[element] == 0:
            continue
        if element not in vector2:
            __equals = False
            break
        if vector1[element] != vector2[element]:
            __equals = False
            break

    return __equals


def add(u,v):
    "Returns the sum of the two vectors"
    assert u.D == v.D

    _result_dict = u.f.copy()

    for key in v.f.keys() :
        if key in _result_dict:
            _result_dict[key] += v.f[key]
        else:
            _result_dict[key] = v.f[key]

    _result = Vec(u.D, _result_dict)

    return _result

def dot(u,v):
    "Returns the dot product of the two vectors"
    assert u.D == v.D

    # v also needs to have the same key for dot product. the if is required to avoid not found key error.
    # E.g.
    # v1 = Vec({'p','q','r','s'}, {'p':2,'s':3,'q':-1,'r':0})
    # v2 = Vec({'p','q','r','s'}, {'p':-2,'r':5})
    return sum(u.f[_u_key] * v.f[_u_key] for _u_key in u.f if _u_key in v.f)

def scalar_mul(v, alpha):
    "Returns the scalar-vector product alpha times v"
    _result = Vec(v.D, {})

    if alpha == 0: # results in a sparse vector
     return _result

    _result.f = {key:v.f[key]*alpha for key in v.f if v.f[key] != 0}

    return _result

def neg(v):
    "Returns the negation of a vector"
    return scalar_mul(v, -1)

##### NO NEED TO MODIFY BELOW HERE #####
class Vec:
    """
    A vector has two fields:
    D - the domain (a set)
    f - a dictionary mapping (some) domain elements to field elements
        elements of D not appearing in f are implicitly mapped to zero
    """
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    __neg__ = neg
    __rmul__ = scalar_mul #if left arg of * is primitive, assume it's a scalar

    def __mul__(self,other):
        #If other is a vector, returns the dot product of self and other
        if isinstance(other, Vec):
            return dot(self,other)
        else:
            return NotImplemented  #  Will cause other.__rmul__(self) to be invoked

    def __truediv__(self,other):  # Scalar division
        return (1/other)*self

    __add__ = add

    def __radd__(self, other):
        "Hack to allow sum(...) to work with vectors"
        if other == 0:
            return self
    
    def __sub__(a,b):
         "Returns a vector which is the difference of a and b."
         return a+(-b)

    __eq__ = equal

    def __str__(v):
        "pretty-printing"
        try:
            D_list = sorted(v.D)
        except TypeError:
            D_list = sorted(v.D, key=hash)
        numdec = 3
        wd = dict([(k,(1+max(len(str(k)), len('{0:.{1}G}'.format(v[k], numdec))))) if isinstance(v[k], int) or isinstance(v[k], float) else (k,(1+max(len(str(k)), len(str(v[k]))))) for k in D_list])
        # w = 1+max([len(str(k)) for k in D_list]+[len('{0:.{1}G}'.format(value,numdec)) for value in v.f.values()])
        s1 = ''.join(['{0:>{1}}'.format(k,wd[k]) for k in D_list])
        s2 = ''.join(['{0:>{1}.{2}G}'.format(v[k],wd[k],numdec) if isinstance(v[k], int) or isinstance(v[k], float) else '{0:>{1}}'.format(v[k], wd[k]) for k in D_list])
        return "\n" + s1 + "\n" + '-'*sum(wd.values()) +"\n" + s2

    def __repr__(self):
        return "Vec(" + str(self.D) + "," + str(self.f) + ")"

    def copy(self):
        "Don't make a new copy of the domain D"
        return Vec(self.D, self.f.copy())