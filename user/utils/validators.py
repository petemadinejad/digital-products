from django.core.validators import RegexValidator

username_validator = RegexValidator(regex=r'^[\w.@+-]+$',
                                    message="Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.")
phone_number_validator = RegexValidator(regex=r'^989[0-3,9]\d{8}$',
                                        message="Enter a valid phone number. This value may contain only digits.")
