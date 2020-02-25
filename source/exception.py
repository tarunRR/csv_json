"""
exception module. This contains a exception framework
for user specific message for differeent exception types
"""
import uuid
from datetime import datetime
import json


class SysError(Exception):
    """
    System Error Base Exception classs
    """
    code = 'SE0000'
    message = 'System Error'

    def __init__(self, additionalmessage):
        self.additionalmessage = additionalmessage

    def __repr__(self):
        return repr(self.additionalmessage)


class BusinessError(Exception):
    """
    Business Error Base Exception class
    """
    code = 'BE0000'
    message = 'Business Error'

    def __init__(self, additionalmessage):
        self.additionalmessage = additionalmessage

    def __repr__(self):
        return repr(self.additionalmessage)


class S3Error(SysError):
    """
    S3 Error System Error Exception class
    """
    code = 'SE0100'
    message = 'S3 failure'


class FileNotExist(BusinessError):
    """
    FIleNotFound Business Error Exception classs
    """
    code = 'BE0200'
    message = 'Expected Input File not Found in Concur'

class ValidationError(BusinessError):
    """
    Validation Business Exception classs
    """
    code = 'BE0300'
    message = 'Validation errors'


class InternalError(SysError):
    """
    Internal error Business error base exception classs
    """
    code = 'SE0000'
    message = 'Internal error while processing.'


def error_message(error_code, message, additional_message):
    """
    Method to print error message in a standard format
    :param error_code: Error code for each error type
    :param error_message: Error message for each error type
    :param additional_message: More discrete message for each error type
    :return: message in the form of JSON
    """
    message_dict = {'createdTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'errorCode': error_code,
                    'systemId': 'Test',
                    'componentId': 'Test',
                    'messageId': str(uuid.uuid4()),
                    'logType': 'ERROR',
                    'message': message,
                    'data': additional_message
                    }
    return json.dumps(message_dict)
