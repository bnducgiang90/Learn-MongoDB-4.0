# sweetscomplete.entity.purchase

import json
from sweetscomplete.entity.base import Base
from sweetscomplete.entity.product_purchased import ProductPurchased

class Purchase(Base) :
    fields = dict({
        # purchase info
        'transactionId'            : '',
        'dateOfPurchase'           : '',
        'extendedPrice'            : 0.00,
        # customer info
        'customerKey'              : '',
        'firstName'                : '',
        'lastName'                 : '',
        'phoneNumber'              : '',
        'email'                    : '',
        'streetAddressOfBuilding'  : '',
        'city'                     : '',
        'stateProvince'            : '',
        'locality'                 : '',
        'country'                  : '',
        'postalCode'               : '',
        'latitude'                 : 0.00,
        'longitude'                : 0.00,
        # products purchased
        'productsPurchased'        : []
    })
    def getKey(self) :
        return self['transactionId']
    def setKey(self, key) :
        self['transactionId'] = key
    def getCustomerName(self) :
        return self['firstName'] + ' ' + self['lastName']
