import math as m

print(f'Pierwiastek kwadratowy z 81 wynosi {m.sqrt(81)}')
print(f'8 do potęgi 10 wynosi {m.pow(8, 10)}')
print(f'Suma pierwiastków z 2, 3 i 6 wynosi {(m.sqrt(2) + m.sqrt(3) + m.sqrt(6)):.2}')
print(f'Pierwiastek kwadratowy z -5 wynosi ???') #Program zwraca ValueError, nie wiem czy trzeba było tutaj wykonywać Exception Handling?
print(f'Pierwiastek sześcienny ze 125 wynosi {m.pow(125, (1/3))}')