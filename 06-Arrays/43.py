import m43

text = "An apple a day keeps the doctor away"

print(text)
print(f"a: \t{m43.words_number(text)}")
print(f"aa: \t{m43.words_number_by_split(text)}")
print(f"b: \t{m43.order_by_length(text)}")
print(f"c: \t{m43.sort_alpha(text)}")