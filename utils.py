import re
import logging

TESTING_ACCOUNTS_IDENTIFIERS_LIST = ['arrivy.com', 'muhio.com', 'getnada.com']


class Util:
    def __int__(self):
        pass

    @classmethod
    def fun(cls):
        return 'Hello World'

    @classmethod
    def strip_email_address(cls, email_address):
        if email_address:
            # Remove all whitespaces and special characters
            updated_email_address = email_address.strip()
            updated_email_address = re.sub('\s+', '', updated_email_address)
            return updated_email_address
        else:
            return email_address

    @classmethod
    def is_email_valid(cls, email_address):
        # return re.match(r"(^[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+$)", email_address.lower())
        return re.match(
            r"(^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$)",
            email_address.lower())

    @classmethod
    def check_if_true(cls, key, value):
        new_value = None
        if isinstance(value, bool):
            new_value = str(value).lower()
        # elif isinstance(value, unicode):
        #     new_value = value.lower()
        elif isinstance(value, str):
            new_value = value.lower()

        if new_value and new_value == 'true':
            return True
        else:
            logging.info(u"Key: {0}, does not contain a valid TRUE boolean value. Value is: {1}".format(key, value))
            return False

    @classmethod
    def check_if_false(cls, key, value):
        new_value = None
        if isinstance(value, bool):
            new_value = str(value).lower()
        # elif isinstance(value, unicode):
        #     new_value = value.lower()
        elif isinstance(value, str):
            new_value = value.lower()

        if new_value and new_value == 'false':
            return True
        else:
            logging.info(u"Key: {0}, does not contain a valid FALSE boolean value. Value is: {1}".format(key, value))
            return False

    @classmethod
    def check_if_integer(cls, key, value, log_error=True):
        try:
            convert_to_int = int(value)
        except:
            if log_error:
                logging.error(u"Key: {0}, does not contain a valid integer value. Value is: {1}".format(key, value))
            return False
        return True

    @classmethod
    def check_if_string(cls, key, value):
        try:
            convert_to_string = str(value)
        except:
            logging.error(u"Key: {0}, does not contain a valid string value. Value is: {1}".format(key, value))
            return False
        return True

    @classmethod
    def check_attribute_type(cls, key, value):
        # if isinstance(value, unicode):
        #     logging.info(u"Key: {0}, contains a unicode string object".format(key))
        #     return 'string'
        if isinstance(value, str):
            logging.info(u"Key: {0}, contains a string object".format(key))
            return 'string'
        elif isinstance(value, dict):
            logging.info(u"Key: {0}, contains a dict object".format(key))
            return 'dict'
        elif isinstance(value, list):
            logging.info(u"Key: {0}, contains a list object".format(key))
            return 'list'

    @classmethod
    def check_if_email_is_test(cls, email_for_verification):
        is_email_test = False
        if not email_for_verification:
            logging.error('email_for_verification not found')
            return is_email_test

        logging.info(u'checking if email domain is test for email: {}'.format(email_for_verification))
        email_for_verification = email_for_verification.lower()
        for identifier in TESTING_ACCOUNTS_IDENTIFIERS_LIST:
            if email_for_verification.endswith(identifier):
                is_email_test = True
                break
        if is_email_test:
            logging.info(u'testing email domain found against email: {}'.format(email_for_verification))
        else:
            logging.info(u'testing email domain not found against email: {}'.format(email_for_verification))
        return is_email_test

    @classmethod
    def verify_data(cls, **kv):
        exceptions = ['exclude'] + kv.get('exclude', [])
        for k, v in kv.items():
            if k not in exceptions:
                if v is None:
                    return False
                if len(v) > 128:
                    return False
                if 'email' in k and '@' not in v:
                    return False
        return True
