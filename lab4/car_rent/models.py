from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse
import datetime


class Brand(models.Model):
    """
    Model representing brand of a car
    """

    name = models.CharField('Brand', max_length=30, help_text='Enter a auto brand (e.g. Toyota, Ford etc.)')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('car_rent:car_list_by_brand',
                       args=[str(self.name)])


class CarModel(models.Model):
    """
    Model representing model of a car, e.g. sedan, hatchback, lift back, crossover etc
    """

    name = models.CharField(max_length=30, help_text='Enter a auto model (sedan, hatchback, lift back, crossover etc.)')

    def __str__(self):
        return self.name


'''
class Discount(models.Model):
    """
    Model representing a discount for clients
    """

    name = models.CharField(max_length=15, help_text='Name of the discount (bronze, silver, gold, platinum)')
    percentage = models.PositiveIntegerField(max_length=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('discount-detail', args=[str(self.name)])


class Fine(models.Model):
    """
    Model representing a fine for clients
    """

    name = models.CharField(max_length=30, help_text='Name of the fine: parking in inappropriate place, car damage etc')
    sum_fine = models.IntegerField(max_length=4)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('fine-detail', args=[str(self.name)])
'''


class Client(models.Model):
    """
    Model representing a client
    """

    first_name = models.CharField(max_length=100, help_text='Enter your first name')
    last_name = models.CharField(max_length=100, help_text='Enter your last name')
    date_birthday = models.DateField(help_text='Enter your birthday')
    email = models.EmailField(help_text='Enter your email')
    phone_number = models.CharField(max_length=20, help_text='Enter your phone number')
    #number_of_rents = models.PositiveIntegerField(max_length=5)
    #discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    #fines = models.ForeignKey(Fine, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])


class Car(models.Model):
    """
    Model representing a specific copy of a car (car for rent)
    """

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          # help_text="Unique ID for this particular car across whole auto park")
    # car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    car_model = models.ForeignKey('CarModel', on_delete=models.SET_NULL, null=True)
    release_year = models.IntegerField('Release year', max_length=4)
    cost = models.IntegerField('Cost', max_length=9)
    rent_per_day = models.IntegerField('Rent per day', max_length=6)
    image = models.ImageField(upload_to='car/%Y/%m/%d', blank=True)
    # amount_of_rent_days = models.PositiveIntegerField(default=0)
    # client = models.OneToOneField(Client, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["release_year"]

    def __str__(self):
        return '{0}'.format(self.id)

    def get_absolute_url(self):
        return reverse('car_rent:car_detail',
                       args=[str(self.id)])


class Rent(models.Model):
    car = models.OneToOneField(Car, on_delete=models.SET_NULL, null=True)
    client = models.OneToOneField(Client, on_delete=models.SET_NULL, null=True)

    start_date = models.DateField(null=True, blank=True)
    finish_date = models.DateField(null=True, blank=True)
    amount_of_rent_days = models.IntegerField(max_length=3, default=1)
    rent_cost = models.IntegerField(max_length=6)
    discount_sum = models.IntegerField(max_length=6)
    fine_sum = models.IntegerField(max_length=4)
    result_sum = models.IntegerField(max_length=6)

    RENT_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On rent'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=RENT_STATUS, blank=True, default='m', help_text='Car availability')

    class Meta:
        ordering = ["start_date"]

    def __str__(self):
        return '{0}'.format(self.id)


class Advertisement(models.Model):
    image = models.ImageField(upload_to='car/%Y/%m/%d', blank=True)
    link = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)


class CompanyPartner(models.Model):
    image = models.ImageField(upload_to='car/%Y/%m/%d', blank=True)
    link = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)


class Article(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    short = models.TextField()
    image = models.ImageField(upload_to='car/%Y/%m/%d', blank=True)


class Company(models.Model):
    info = models.TextField()
    company_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='car/%Y/%m/%d', blank=True)
    video_link = models.CharField(max_length=100)
    certificate = models.TextField()
    requisites = models.TextField()
    company_history = models.TextField()


class NewsArticle(models.Model):
    title = models.CharField(max_length=100)
    short = models.TextField()
    image = models.ImageField(upload_to='car/%Y/%m/%d', blank=True)
    full_link = models.CharField(max_length=100)


class Question(models.Model):
    question = models.TextField()
    answer = models.TextField()
    date = models.DateTimeField("Date", auto_now_add=True)


class Worker(models.Model):
    name = models.CharField(max_length=100)
    work_info = models.TextField()
    phone_number = models.CharField(max_length=20, help_text='Enter your phone number')
    email = models.EmailField(help_text='Enter your email')
    image = models.ImageField(upload_to='car/%Y/%m/%d', blank=True)


class Vacancy(models.Model):
    position = models.CharField(max_length=100)
    position_info = models.TextField()
    salary = models.IntegerField()


'''
class Car(models.Model):
    """
    Model representing a car (but not a specific copy)
    """

    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    car_model = models.ForeignKey('CarModel', on_delete=models.SET_NULL, null=True)
    release_year = models.IntegerField('Release year', validators=[MinLengthValidator(4), MaxLengthValidator(4)])
    cost = models.IntegerField('Cost', validators=[MinLengthValidator(4), MaxLengthValidator(9)])
    rent_per_day = models.IntegerField('Rent per day', validators=[MinLengthValidator(2), MaxLengthValidator(4)])

    def __str__(self):
        return '{0} {1}'.format(self.brand, self.car_model)

    def get_absolute_url(self):
        return reverse('car-detail', args=[str(self.id)])
'''
