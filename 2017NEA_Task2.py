import sys

print("Welcome")
email = input("Enter your email address: \n")

while True:
    country = input("Please enter your country: 'UK', 'US', 'AU' \n")
    skill_level = input("Choose your Skill Level (C)Casual/(E)Expert: \n")

    entry_fee = 10

    if country.upper() == "UK":
        currency = " GBP"
    elif country.upper() == "US":
        currency = " USD"
    elif country.upper() == "AU":
        currency = " AUD"
    else:
        sys.exit("Skill level does not exist")

    if skill_level.upper() == "C":
        entry_fee += 20
    elif skill_level.upper() == "E":
        entry_fee += 35
    else:
        sys.exit("Skill level does not exist")

    if currency == " USD":
        entry_fee *= 1.50
    elif currency == " AUD":
        entry_fee *= 2.00

    print("fee = " + str(entry_fee) + currency)

    another_fee = input("Do you want to calculate another fee? Yes/No: \n")

    if another_fee.upper() == "No":
        break

