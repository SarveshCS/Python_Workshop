from functools import reduce

x = [1, 2, 3, 4]
print(f'Original: {x}')
squares = list(map(lambda n: n**2, x))
print(f'Squares: {squares}')

evens = list(filter(lambda n: n % 2 == 0, squares))
print(f'Evens: {evens}')

sum_evens = reduce(lambda a, b: a + b, evens)
print(f'Sum of evens: {sum_evens}')

odds = list(filter(lambda n: n % 2 != 0, squares))
print(f'Odds: {odds}')

squares_of_odds = list(map(lambda n: n**2, odds))
print(f'Squares of odds: {squares_of_odds}')

sum_squares_of_odds = reduce(lambda a, b: a + b, squares_of_odds)
print(f'Sum of squares of odds: {sum_squares_of_odds}')