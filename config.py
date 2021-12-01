from faker import Faker
from faker.generator import Generator
import faker.providers.address.en_US
import faker.providers.lorem.en_US
import faker.providers.company
import faker.providers.phone_number.en_US
import random


class Provider(faker.providers.BaseProvider):
    ### Phone Numbers (could move to separate class)
    """Built around the North American Numbering Plan"""
    fake = Faker()

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
