# coding=utf-8
import random
import string


class StringUtils:

    @staticmethod
    def get_random_string(length=3):
        """Method returns random string.

        Args:
            length: length of string that need to be generated .
        Return:
             randomly generated string.
        """
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
