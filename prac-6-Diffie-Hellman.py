#implementing Diffie-Hellman Algorithm

from random import randint

if __name__ == '__main__':
    P = 23
    G = 9
    print('The Value of P is: %d' % P)
    print('The Value of G is: %d' % G)

    a = 4  
    print('Secret Number for Alice is: %d' % a)
    x = int(pow(G, a, P))  

    b = 6  
    print('Secret Number for Bob is: %d' % b)
    y = int(pow(G, b, P))  

    ka = int(pow(y, a, P))  
    kb = int(pow(x, b, P))  

    print('Secret key for Alice is: %d' % ka)
    print('Secret key for Bob is: %d' % kb)

