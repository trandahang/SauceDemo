class CheckoutStepOne:
    def __init__(self, firstname, lastname, zipcode):
        self.firstname = firstname
        self.lastname = lastname
        self.zipcode = zipcode

    def __str__(self):
        return '{"firstname":"%s", "lastname": "%s","zipcode":"%s"' % (self.firstname, self.lastname, self.zipcode)