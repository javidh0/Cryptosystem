import random
import math

class PublicKeyCrypto:
    __power = None
    __div = None
    def __init__(self, random_seed = 1, Range:list[int] = [2, 100]) -> None:
        random.seed(random_seed)
        self.__power = random.randint(Range[0], Range[1])
        random.seed(random_seed+Range[1])
        self.__div = random.randint(Range[0], Range[1])
        print("Public Key Generation Succesfull")
    def __Compute(self, a):
        a1 = math.pow(self.__power, ord(a))
        a2 = int(math.remainder(a1, self.__div))
        return a2
    def Encypt(self, value:str):
        return tuple(map(self.__Compute, value))