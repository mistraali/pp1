first = bool(input("First? (y/n): ").lower().strip() == 'y')
second = bool(input("Second? (y/n): ").lower().strip() == 'y')
third = bool(input("Third? (y/n): ").lower().strip() == 'y')

print(f"First: {"Yes" if first else "No"}")
print(f"Second: {"Yes" if second else "No"}")
print(f"Third: {"Yes" if third else "No"}")