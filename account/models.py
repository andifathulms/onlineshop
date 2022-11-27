from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AnonymousUser

from django.utils.translation import gettext_lazy as _

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=False)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	def __str__(self):
		return self.username

    # For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True
    
class Customer(models.Model):

    class Member(models.TextChoices):
        EMPTY = 'NO', _('Not a member')
        SILVER = 'SV', _('Silver')
        GOLD = 'GD', _('Gold')
        PLATINUM = 'PT', _('Platinum')
        DIAMOND = 'DM', _('Diamond')

    account                 = models.OneToOneField('Account', primary_key=True, on_delete=models.CASCADE, related_name="user_customer")
    phone_number            = models.CharField(max_length=30, blank=True, null=True)
    transaction_count       = models.PositiveIntegerField(default=0)
    transaction_item_count  = models.PositiveIntegerField(default=0)
    transaction_total_count = models.BigIntegerField(default=0)
    membership_status       = models.CharField(max_length=2, choices=Member.choices, default=Member.EMPTY)
    membership_points       = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return self.account.username + " " + self.account.email
    
    def strMembershipStatus(self):
        if self.membership_status == "NO":
            return "Not a member yet"
        elif self.membership_status == "SV":
            return "Silver"
        elif self.membership_status == "GD":
            return "Gold"
        elif self.membership_status == "PT":
            return "Platinum"
        elif self.membership_status == "DM":
            return "Diamond"

class Address(models.Model):
    customer          = models.ForeignKey('Customer', on_delete=models.CASCADE)
    province          = models.CharField(max_length=255)
    regency           = models.CharField(max_length=255)
    district          = models.CharField(max_length=255)
    zipcode           = models.CharField(max_length=10)
    address            = models.TextField()

    def __str__(self) -> str:
        return self.pk + " " + self.province + " " + self.regency + " " + self.district


