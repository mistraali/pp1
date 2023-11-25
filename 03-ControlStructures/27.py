facebook = bool(input("Facebook? "))
twitter = bool(input("Twitter? "))
instagram = bool(input("Instagram? "))


if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):
    print("A person can be a good influencer!")
else:
    print("A person cannot be a good influencer!")   
