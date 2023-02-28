# Cryptosystem
# Encrypted tuple
## Definition 
The tuple of encrypted elements(char) in order. <br />
Enc_tup[i] = E(plainText[i]) <br /> 
eg: "Javidh" is encrypted and if the cipher is (-12, 3, 23, 34, -24, -2) for a Random key then 'J' is mapped to -12, 'a' is mapped to 3, 'v' is mapped to 23, .. . 


# Class Funtions
## PublicKeyCrypto()
### class PublicKeyCrypto( <br />
###    random_seed: int = 1, <br />
###    Range: list[int] = [2, 100] <br />
### )