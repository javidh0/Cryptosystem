import random
import math
class PublicKeyCrypto:
    __power = None
    __div = None
    def __init__(self, random_seed = 1, Range:list[int] = [0, 100]) -> None:
        random.seed(random_seed)
        self.__power = random.randint(Range[0], Range[1])
        random.seed(random_seed+Range[1])
        self.__div = random.randint(Range[0], Range[1])
        print("Public Key Generation Succesfull")
    def __Compute(self, a):
        return chr(math.pow(ord(a), self.__power) % self.__div)
    def Encypt(self, value:str):
        return str(map(self.__Compute, tuple(value)))