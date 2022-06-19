import math
import random
from functools import wraps

def decW(flag):
    def dec(func):
        wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            TP = TN = FP = FN = 0
            total = 0
            for e in result:
                if (e[0] is True) and (e[1] is True):
                    TP += 1
                elif (e[0] is True) and (e[1] is False):
                    FN += 1
                elif (e[0] is False) and (e[1] is True):
                    FP += 1
                elif (e[0] is False) and (e[1] is False):
                    TN += 1
                else:
                    pass
                total += 1
            if flag == "ACC":
                acc = (TP + TN) / total
                print("ACC : %f" % acc)
            elif flag == "MCC":
                mcc = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                print("MCC : %f" % mcc)
            else:
                pass

            return result
        return wrapper
    return dec



@decW("ACC")  #if you want to output"MCC",you can use MCC here
def Random_yield(**kargs):
    num = kargs["num"]
    struct = kargs["struct"]
    for i in range(num):
        element = list( )
        for key, val in struct.items( ):
            if key == "int":
                it = iter(val["range"])
                element.append(random.randint(next(it), next(it)))
            elif key == "float":
                it = iter(val["range"])
                element.append(random.uniform(next(it), next(it)))
            elif key == "str":
                strRange = val["range"]
                strLength = val["length"]
                string = ""
                for j in range(strLength):
                    string += random.choice(strRange)
                element.append(string)
            elif key == "bool":
                for ith in range(val["num"]):
                    element.append(random.choice((True, False)))
            else:
                element.append("Uknown Type")

        yield element



arg = {"num":10000, "struct":{"bool":{"num":5}}}
Random_yield(**arg)



