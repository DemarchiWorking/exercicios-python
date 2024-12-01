def e_palindromo(palavra):
    if len(palavra) <= 1:
        return True
    if palavra[0] != palavra[-1]:
        return False
    return e_palindromo(palavra[1:-1])

palavra = "ovo"
print(e_palindromo(palavra))

palavra = "mundo"
print(e_palindromo(palavra))
