# Cryptosystem
# Encrypted tuple
## Definition 
The tuple of encrypted elements(char) in order. <br />
$Chiper_t[i] = E\left(plainText[i]\right)$ <br /> 
eg: "Javidh" is encrypted and if the cipher is (-12, 3, 23, 34, -24, -2) for a Random key then 'J' is mapped to -12, 'a' is mapped to 3, 'v' is mapped to 23, .. . 


# Class Funtions
## PublicKeyCrypto()
### class PublicKeyCrypto( <br />
### random_seed: int = 1, <br />
### Range: list[int] = [2, 100] )
* Encryption method:
    * $y = f(x)$ ; y is chipher and x is plain text
    * $f --> Remainder\left(power^x /div\right)$ ; power, div &#x2208; &#8477;
* init(random_seed: int = 1, Range: list[int] = [2, 100]) 
    * Generates a random public key 