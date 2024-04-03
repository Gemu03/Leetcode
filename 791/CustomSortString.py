""" 
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.
 """

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = {}
        for i in range(len(order)):
            order_dict[order[i]] = i
        s = sorted(s, key=lambda x: order_dict.get(x, 100))
        return ''.join(s)
    
# Explicación:
# 1. Creamos un diccionario con las letras de order y su posición en order.
# 2. Ordenamos s basado en el valor de order_dict, si no existe en order_dict, le asignamos 100.
# 3. Devolvemos la cadena s ordenada.
    