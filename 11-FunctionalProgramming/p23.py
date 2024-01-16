"""
Calculate and display the total points obtained by competitors. 
The highest and lowest scores are discarded. 
The remaining three scores are added up to form the final score obtained by the competitor.
Tip: use the Python built-in functions: map(), sum(), min(), max()
"""

scores = [(17,15,16,17,15),(16,18,19,17,19),(19,15,15,19,18),(18,17,19,15,16)]

final_scores = list(map(lambda x: sum(sorted(x)[1:4]),scores))

print(final_scores)

final_scores_2 = list(map(lambda x: sum(x)-min(x)-max(x), scores))

print(final_scores_2)