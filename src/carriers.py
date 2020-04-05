# https://20somethingfinance.com/how-to-send-text-messages-sms-via-email-for-free/
from enum import Enum


class Carrier(Enum):

    def __init__(self, *args):
        self.carrier_key = self.name.lower()

    ATT = 1
    SPRINT = 2
    TMOBILE = 3
    VERIZON = 4


carrier2email = {
    Carrier.ATT.carrier_key: {
        'sms': '@txt.att.net ',
        'mms': '@mms.att.net '
    },
    Carrier.SPRINT.carrier_key: {
        'sms': '@messaging.sprintpcs.com',
        'mms': '@pm.sprint.com'
    },
    Carrier.TMOBILE.carrier_key: {
        'sms': '@tmomail.net',
        'mms': '@tmomail.net'
    },
    Carrier.VERIZON.carrier_key: {
        'sms': '@vtext.com',
        'mms': '@vzwpix.com'
    }
}
