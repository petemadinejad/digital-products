from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager, send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from .utils import exceptions, help_text, validators


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, phone_number, email, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, username=username, email=email, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, date_joined=now, **extrafields)
        if not extra_fields.get('no_password'):
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, email=None, phone_number=None, password=None, **extra_fields):
        if username is None:
            if email:
                username = email.split('@')[0]
            if phone_number:
                username = random.choice(string.ascii_letters) + ''.join(
                    random.choice(string.digits) for _ in range(10))
            while user.objects.filter(username=username).exists():
                username = random.choice(string.ascii_letters) + ''.join(
                    random.choice(string.digits) for _ in range(10))
        return self._create_user(username, phone_number, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, phone_number, password, **extra_fields):
        return self._create_user(username, phone_number, email, password, True, True, **extra_fields)


class User(AbstractUser, PermissionMixin):
    """
    An abstract base class implementing a fully featured User model with admin-compliant permissions.
    Username and password and email is required. other fields are optional.
    """
    username = models.CharField(_('username'), max_length=32, unique=True, blank=True,
                                help_text=_(help_text.username_help_text), validators=[validators.username_validator],
                                error_messages={'unique': _(exceptions.username_unique_error)})
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=100, blank=True)
    nick_name = models.CharField(_('nick name'), max_length=100, blank=True)
    phone_number = models.BigIntegerField(_('phone number'), max_length=20, blank=True, unique=True, null=True,
                                          validators=[validators.phone_number_validator],
                                          error_messages={'invalid': _(exceptions.phone_number_invalid_error)})
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_(help_text.is_staff_help_text))
    is_active = models.BooleanField(_('active'), default=True, help_text=_(help_text.is_active_help_text))
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    last_seen = models.DateTimeField(_('last seen date'), auto_now=True)

    objects = UserManager()

    USER_NAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['username']

    @property
    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    @property
    def get_nickname(self):
        return self.nick_name if self.nick_name else self.username

    def __str__(self):
        return self.username


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField(_('nick name'), max_length=32, blank=True)
    avatar = models.ImageField(_('avatar'), upload_to='avatar/%Y/%m', blank=True)
    birthday = models.DateField(_('birthday'), blank=True, null=True)
    gender = models.BooleanField(_('gender'), default=True, help_text=help_text.gender_help_text)
    province = models.ForeignKey(verbose_name=_('province'), to='Province', on_delete=models.CASCADE, blank=True,
                                 null=True)

    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')
        ordering = ['user']

    def __str__(self):
        return self.user.username


class Device(BaseModel):
    WEB = 1
    IOS = 2
    ANDROID = 3
    DEVICE_TYPE_CHOICES = ((WEB, 'web'),
                           (IOS, 'ios'),
                           (ANDROID, 'android'))
    user = models.ForeignKey(verbose_name=_('user'), to=User, on_delete=models.CASCADE)
    device_type = models.PositiveSmallIntegerField(_('device type'), choices=DEVICE_TYPE_CHOICES, default=WEB)
    device_uuid = models.CharField(_('device uuid'), max_length=64, blank=True, null=True)
    last_login = models.DateTimeField(_('last login'), auto_now=True)
    device_os = models.CharField(_('device os'), max_length=32, blank=True, null=True)
    device_model = models.CharField(_('device model'), max_length=32, blank=True, null=True)
    app_version = models.CharField(_('app version'), max_length=32, blank=True, null=True)

    class Meta():
        db_table = 'user_devices'
        verbose_name = _('Device')
        verbose_name_plural = _('Devices')
        ordering = ['user']
        unique_together = ('user', 'device_type')


class Province(BaseModel):
    name = models.CharField(_('name'), max_length=32, blank=True)
    code = models.CharField(_('code'), max_length=32, blank=True)

    class Meta():
        db_table = 'provinces'
        verbose_name = _('Province')
        verbose_name_plural = _('Provinces')
        ordering = ['name']
        unique_together = ('name', 'code')

    def __str__(self):
        return self.name