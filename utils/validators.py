class PhoneNumberValidator(RegexValidator):
    regex = r'^989[0-3,9]\d{8}$'
    message = "phone number must be valid 12 digits like 98**********"
    code = 'invalid_phone_number'


class UsernameValidators(RegexValidator):
    regex = r'^[a-zA-Z][a-zA-Z0-9\-\.]+$'
    message = _(
        "Enter a valid username starting with -z. This value may contain only letters, numbers and underscore characters.")
    code = 'invalid_username'


class SKUValidator(RegexValidator):
    regex = r'^[a-zA-Z0-9\-\ ]{6,20}$'
    message = "SKU must be alphanumeric with 6 to 20 characters"
    code = 'invalid_sku'


class PostalCodeValidator(RegexValidator):
    regex = r'^[0-9]{10}$'
    message = _("Enter a valid postal code. This value may contain only digits.")
    code = 'invalid_postal_code'


class IDNumberValidator(RegexValidator):
    regex = r'^[0-9]{10}$'
    message = _("Enter a valid ID number. This value may contain only digits.")
    code = 'invalid_id_number'


class IBanNumberValidator(RegexValidator):
    regex = r'^$'
    message = _("Enter a valid IBAN number.")
    code = 'invalid_iban_number'


class BankCardNumberValidator(RegexValidator):
    regex = r'^[0-9]{16}$'
    message = _("Enter a valid bank card number.")
    code = 'invalid_bank_card_number'


phone_number_validator = PhoneNumberValidator()
username_validators = UsernameValidators()
sku_validator = SKUValidator()
postal_code_validator = PostalCodeValidator()
id_number_validator = IDNumberValidator()
iban_number_validator = IBanNumberValidator()
bank_card_number_validator = BankCardNumberValidator()
