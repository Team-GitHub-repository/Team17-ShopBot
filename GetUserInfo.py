import json
with open("StoredInfo.json") as conffile:
    StoredInfo = json.load(conffile)

firstN = StoredInfo["firstName"]
lastN = StoredInfo["lastName"]
phone = StoredInfo["phoneNumber"]
email = StoredInfo["email"]
shipAd = StoredInfo["shippingAddress"]
shipApt = StoredInfo["shippingAptSuite"]
shipCity = StoredInfo["shippingCity"]
shipState = StoredInfo["shippingState"]
shipStateAb = StoredInfo["shippingStateAb"]
shipCountry = StoredInfo["shippingCountry"]
shipCountryAb = StoredInfo["shippingCountryAb"]
shipZip = StoredInfo["shippingZip"]
billAd = StoredInfo["billingAddress"]
billApt = StoredInfo["billingAptSuite"]
billCity = StoredInfo["billingCity"]
billState = StoredInfo["billingState"]
billStateAb = StoredInfo["billingStateAb"]
billCountry = StoredInfo["billingCountry"]
billCountryAb = StoredInfo["billingCountryAb"]
billZip = StoredInfo["billingZip"]
cardType = StoredInfo["cardType"]
cardNum = StoredInfo["cardNumber"]
cardCvv = StoredInfo["cardCvv"]
expYear = StoredInfo["expYear"]
expMonth = StoredInfo["expMonth"]
cardName = StoredInfo["cardName"]

# when first using the information in StoredInfo.json, it will use values currently on the github repository
# these values will need to be updated by running UserInfo.py again to store new values

# https://github.com/bencmbrook/SneakerBot/blob/master/scripts/getconf.py was used as reference for this code
