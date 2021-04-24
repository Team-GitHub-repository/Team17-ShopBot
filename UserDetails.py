class UserDetails:

    def __init__(self):
        self.deliveryItems = {}
        self.userItems = {}
        self.paymentItems = {}
        self.productItems = {}

    def deliveryInfo(self, firstName, lastName, phone, address, city, state, zip):
        self.deliveryItems['firstName'] = firstName
        self.deliveryItems['lastName'] = lastName
        self.deliveryItems['phone'] = phone
        self.deliveryItems['address'] = address
        self.deliveryItems['city'] = city
        self.deliveryItems['state'] = state
        self.deliveryItems['zip'] = zip
        return self.deliverItems

    def userInfo(self, email, userName, password):
        self.userItems['email'] = email
        self.userItems['userName'] = userName
        self.userItems['password'] = password
        return self.userItems

    def paymentInfo(self, cardFirstName, cardLastName, cardNum, expMonth, expYear, cvv, phone):
        self.paymentItems['cardFirstName'] = cardFirstName
        self.paymentItems['cardLastName'] = cardLastName
        self.paymentItems['cardNum'] = cardNum
        self.paymentItems['phone'] = expMonth
        self.paymentItems['city'] = expYear
        self.paymentItems['cvv'] = cvv
        self.paymentItems['cardPhone'] = phone
        return self.paymentItems

    def itemInfo(self, itemName, itemID, itemAmount, itemUrl):
        self.productItems['name'] = itemName
        self.productItems['id'] = itemID
        self.productItems['amount'] = itemAmount
        self.productItems['url'] = itemUrl
        return self.productItems

    def getFirstName(self):
        return self.deliveryItems['firstName']

    def getLastName(self):
        return self.deliveryItems['lastName']

    def getPhoneNumber(self):
        return self.deliveryItems['phone']

    def getAddress(self):
        return self.deliveryItems['address']

    def getCity(self):
        return self.deliveryItems['city']

    def getState(self):
        return self.deliveryItems['state']

    def getZip(self):
        return self.deliveryItems['zip']

    def getEmail(self):
        return self.userItems['email']

    def getUserName(self):
        return self.userItems['username']

    def getPassword(self):
        return self.userItems['password']

    def getCardFirstName(self):
        return self.paymentItems['cardFirstName']

    def getCardLastName(self):
        return self.paymentItems['cardLastName']

    def getCardNumber(self):
        return self.paymentItems['cardNum']

    def getExpirationMonth(self):
        return self.paymentItems['expMonth']

    def getExpirationYear(self):
        return self.paymentItems['expYear']

    def getCVV(self):
        return self.paymentItems['cvv']

    def getCardPhone(self):
        return self.paymentItems['cardPhone']

    def getItemName(self):
        return self.productItems['name']

    def getItemID(self):
        return self.productItems['id']

    def getItemAmount(self):
        return self.productItems['amount']

    def getItemURL(self):
        return self.productItems['url']

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
                return userInput
            print("y or n! try again.")
