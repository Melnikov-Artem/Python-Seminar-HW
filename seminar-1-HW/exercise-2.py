#2.Напишите программу для. проверки истинности утверждения 
#¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


equtn = 'not(X or Y or Z) == not X and (not Y) and (not Z)'
print(f'Проверим верно ли утверждение:\n{equtn}\n')

for X in range(2):
    for Y in range(2):
        for Z in range(2):
            left = not(X or Y or Z)
            right = not X and not Y and not Z            
            if left == right:
                print(f'{X}\t{Y}\t{Z}\t Утверждение истинно')
            else:
                print(f'{X}\t{Y}\t{Z}\t Не истина')
print('\n')