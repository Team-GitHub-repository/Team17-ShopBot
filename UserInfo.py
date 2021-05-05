import json

configuration = {}

print("")
print("You can leave segments blank by just pressing enter. "
      "However, This can cause errors.")
print("")

configuration["firstName"] = input("Enter your first name: ")
configuration["lastName"] = input("Enter your last name: ")
configuration["phoneNumber"] = input("Enter your phone number: ")
configuration["email"] = input("Enter your email address: ")
configuration["shippingAddress"] = input("Enter the shipping address: ")
configuration["shippingAptSuite"] = input("Enter the apartment/suite number, if applicable: ")
configuration["shippingCity"] = input("Enter the shipping city: ")
configuration["shippingState"] = input("Enter the shipping state (not abbreviated): ")
configuration["shippingStateAb"] = input("Enter the shipping state (abbreviated): ")
configuration["shippingCountry"] = input("Enter the shipping country (not abbreviated): ")
configuration["shippingCountryAb"] = input("Enter the shipping country (abbreviated): ")
configuration["shippingZip"] = input("Enter the shipping zip code: ")

billing = input("Is the billing information the same as the shipping information? [Y/N]: ").title()
if billing in ["N", "No"]:
    configuration["billingAddress"] = input("Enter the billing address: ")
    configuration["billingAptSuite"] = input("Enter the apartment/suite number, if applicable: ")
    configuration["billingCity"] = input("Enter the billing city: ")
    configuration["billingState"] = input("Enter the billing state (not abbreviated): ")
    configuration["billingStateAb"] = input("Enter the billing state (abbreviated): ")
    configuration["billingCountry"] = input("Enter the billing country (not abbreviated): ")
    configuration["billingCountryAb"] = input("Enter the billing country (abbreviated): ")
    configuration["billingZip"] = input("Enter the billing zip code: ")
else:
    configuration["billingAddress"] = configuration["shippingAddress"]
    configuration["billingAptSuite"] = configuration["shippingAptSuite"]
    configuration["billingCity"] = configuration["shippingCity"]
    configuration["billingState"] = configuration["shippingState"]
    configuration["billingStateAb"] = configuration["shippingStateAb"]
    configuration["billingCountry"] = configuration["shippingCountry"]
    configuration["billingCountryAb"] = configuration["shippingCountryAb"]
    configuration["billingZip"] = configuration["shippingZip"]

configuration["cardType"] = input("Enter the type of credit card being used(Visa, MasterCard, Amex...)? ")
configuration["cardNumber"] = input("Enter the credit card number: ")
configuration["cardCvv"] = input("Enter the CVV for the credit card: ")
configuration["expYear"] = input("Enter the card's expiration year: ")
configuration["expMonth"] = input("Enter the card's expiration month: ")
configuration["cardName"] = input("Enter the name that appears on the card: ")

with open("StoredInfo.json", "w") as conffile:
    json.dump(configuration, conffile, sort_keys=False, indent=4)

print("")
print("Thank you. The information has been stored.")

# https://github.com/bencmbrook/SneakerBot/blob/master/scripts/makeinfo.py was used as reference for this code
