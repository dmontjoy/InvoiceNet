FIELD_TYPES = {
    "general": 0,
    "optional": 1,
    "amount": 2,
    "date": 3
}

FIELDS = dict()

FIELDS["invoicenumber"] = FIELD_TYPES["general"]
FIELDS["vendorname"] = FIELD_TYPES["general"]

FIELDS["invoicedate"] = FIELD_TYPES["date"]

FIELDS["amountnet"] = FIELD_TYPES["amount"]
FIELDS["amounttax"] = FIELD_TYPES["amount"]
FIELDS["amounttotal"] = FIELD_TYPES["amount"]
