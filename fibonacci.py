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

class SummableSequence(object):
    def __init__(self, *initial):
        self.initial = initial
        self.n = len(initial)

    def __call__(self, i):
        out = [] 
        n = self.n
        for each in self.initial:
            out.append(each)
        j = 0
        for j in range(0,i-n):
            a = sum(out[j:n+j+1])
            out.append(a)
        return(out[i-1])

if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))