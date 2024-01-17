def main():
    
    print(NWD(3952, 864))
    print(NWD(45, 60))
    print(NWD(72, 180))
    print(NWD(126, 210))
    print(NWD(135, 225))
    
def NWD(a, b):
    """Obliczanie NWD za pomocą algorytmu Euklidesa"""
    
    while True: #nieskończona pętla żeby się powtarzała cały czas dopóki nie będziemy chcieli z nią skończyć
        reszta = a % b #przypisanie wyniku modulo a i b do zmiennej reszta
        if reszta != 0: #jeśli reszta wynosi 0 to znaczy że to już koniec algorytmu i nie chcemy nadpisać naszych wartości a i b, przechodzimy do else
            a = b #według algorytmu przenosimy; w następnej iteracji a to b, a b to reszta
            b = reszta
        else:
            return b #return b terminuje nieskończoną pętlę while
main()