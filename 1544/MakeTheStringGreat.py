class Solution:
    def makeGood(self, s: str) -> str:
        nuevaPalabra = []
        for letra in s:
            if nuevaPalabra and abs(ord(nuevaPalabra[-1]) - ord(letra)) == 32:
                nuevaPalabra.pop()
            else:
                nuevaPalabra.append(letra)
        return "".join(nuevaPalabra)