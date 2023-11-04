password = input("Enter password: ")

comp = False

if len(password) == 8:
    comp = True

print(f"Password has correct length: {comp}")