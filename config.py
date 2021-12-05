import faker
import faker.providers.phone_number as phoneLib
import random
import unittest

from faker.proxy import Faker
fake = faker.Faker()
phoneFake = phoneLib.Provider(faker.Generator())

class Provider(faker.providers.BaseProvider):
    ### Phone Numbers (could move to separate class)
    """Built around the North American Numbering Plan"""

    def phone_areacode(self):
        """Generates Area Codes from the of the North American Numbering Plan
        Allowed ranges: [2–9] for the first digit, and [0-9] for the second and third digits.
        When the second and third digits of an area code are the same,
        that code is called an easily recognizable code (ERC).
        ERCs designate special services; e.g., 800 for toll-free service.
        The NANP is not assigning area codes with 9 as the second digit.[34]"""
        firstdigit = random.randint(2, 9)
        seconddigit = random.randint(0, 9)
        thirddigit = random.randint(0, 9)
        while seconddigit == thirddigit:
            thirddigit = random.randint(0, 9)
        return str(firstdigit) + str(seconddigit) + str(thirddigit)

    def phone_exchange(self):
        """generally follows the same pattern as area code. While this doesn't capture
        every single option for phone numbers, it gets us pretty close."""
        return self.phone_areacode()

    def phone_lastfour(self):
        return fake.numerify(text="####")

    def full_phone(self, isRandomFormat) -> str:
        #todo: #1 https://realpython.com/python-string-formatting/
        if(isRandomFormat is None):
            isRandomFormat = False
        phoneString = ''
        if(isRandomFormat):
            concatPhone = self.phone_areacode+self.phone_exchange+self.phone_lastfour
            phoneString = fake.random_choices(phoneLib.Provider.formats).format_map()
        else: phoneString = ("{0}-{1}-{2}").format(
            self.phone_areacode(), self.phone_exchange(), self.phone_lastfour())
        return phoneString


if __name__ == "__main__":
    prov1 = Provider(faker.Generator())
    print(prov1.full_phone(False))
    print(prov1.full_phone(True))
