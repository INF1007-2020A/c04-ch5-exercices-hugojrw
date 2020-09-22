#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number <= 0:
        number *= -1
    else:
        number *= 1 
    return number


def use_prefixes() -> List[str]:
    names = []
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    for pre in prefixes:
        name = pre + suffixe
        names.append(name)

    return names


def prime_integer_summation() -> int:
    count = 2
    prime = []
    while len(prime) != 100:
        for value in range(2, count):
            if count%value == 0:
                break
        else:
            prime.append(count)
        count += 1

    return sum(prime)


def factorial(number: int) -> int:
    count = 1
    total = 1
    while count <= number:
        total *= count
        count += 1
    return total


def use_continue() -> None:
    for i in range(1, 11, 1):
        if i == 5:
            continue
        else:
            print(i)
            
def verify_ages(groups: List[List[int]]) -> List[bool]:
    valid = []
    for group in groups:
        if len(group) > 10:
            valid.append(False)
        elif len(group) <= 3:
            valid.append(False)
        else:
            try:
                group.index(25)
                valid.append(True)
            except:
                if min(group) < 18:
                    valid.append(False)
                elif max(group) > 70:
                    try:
                        group.index(50)
                        valid.append(False)
                    except:
                        valid.append(True)
                else:
                    valid.append(True)
                

    return valid

# Autre Méthode avec 2 loops for

#def verify_ages(groups: List[List[int]]) -> List[bool]:
#    valid = []
#    for group in groups:
#        if len(group) > 10:
#            valid.append(False)
#        elif len(group) <= 3:
#            valid.append(False)
#        else:
#            validity = True
#            for mem in group:
#                if mem == 25:
#                    validity = True
#                    break
#                elif mem < 18:
#                    validity = False
#                elif mem > 70:
#                    for mem2 in group:
#                        if mem2 == 50:
#                            validity = False
#
#            if validity:
#                valid.append(True)
#            else:
#                valid.append(False)
#    return valid

def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
