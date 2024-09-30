####Fonction secondaire
""" écrire un programme permettant de voir si un mot est -il un palindromes"""
def ispalindrome(p):
    """vérifier si p est un palindromes
    arg:p"""
    p1 = p.lower()
    mytable = str.maketrans("éèêëàâôç-'.;:!?,","eeeeaaoc        ")
    p2= p1.translate(mytable)
    p3 = p2.replace(" ","")
    if p3[::-1] == p3[::1]:
        return True
    return False


#### Fonction principale
def main():
    """ Dire si P est un palindrome"""
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
