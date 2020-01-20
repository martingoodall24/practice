#!/usr/bin/env python3


def last_8(some_int):
    """Return the last 8 digits of an int
    :param int some_int: the number
    :rtype: int
    """
    last_8_digits = some_int % 100000000
    return last_8_digits
    #raise NotImplementedError()
    
def remove_me():
    print("remove_me3")

def optimized_fibonacci(f):
    out = []
    out.append(0) 
    out.append(1)
    for i in range(2,f+1):
        out.append(out[i-1] + out[i-2])
    return out[f]
    #raise NotImplementedError()

def optimized_fibonacci(f):
    out = []
    out.append(0) 
    out.append(1)
    for i in range(2,f+1):
        out.append(out[i-1] + out[i-2])
    return out[f]
    #raise NotImplementedError()    

class SummableSequence(object):
    def __init__(self, *initial):
        self.initial = initial
        #print(self.initial)
        #raise NotImplementedError()

    def __call__(self, i):
        out = []
        for each in self.initial:
            #print(each)
            out.append(each)
        for j in range(2,i+1):
            out.append(out[j-1] + out[j-2] + out[j-3])
        return out[i]
        #raise NotImplementedError()

if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))