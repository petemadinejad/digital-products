from django.core.validators import RegexValidator

username_validator = RegexValidator(regex='^[\w.@+-]+$',
                                    message="Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.")
# phone_number_validator = RegexValidator(regex='^[0-9]{11}$',
#                                         message="Enter a valid phone number. This value may contain only digits.")
