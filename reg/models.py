from django.db import models
from django.contrib.auth.models import User


class Instrument(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    instruments = models.ManyToManyField(Instrument)

    def __str__(self):
        return self.name


class Parent(models.Model):
    """
    Represents a parent associated with a user in the application.

    Attributes:
        user (User): The user associated with the parent.
        first_name (str): The first name of the parent.
        last_name (str): The last name of the parent.
        cell_phone (str): The cell phone number of the parent.
        email (str): The email address of the parent.
        address (str): The address of the parent.
        city (str): The city of the parent's address.
        province (str): The province or state abbreviation of the parent's address.
        postal_code (str): The postal code of the parent's address.
        should_correspond (bool): Indicates whether the parent should receive correspondence.

    Fields:
        - user: ForeignKey to User model
        - first_name: CharField
        - last_name: CharField
        - cell_phone: CharField
        - email: EmailField
        - address: TextField
        - city: CharField
        - province: CharField
        - postal_code: CharField
        - should_correspond: BooleanField

    Methods:
        - __str__: Returns a string representation of the parent.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, help_text="The first name of the parent.")
    last_name = models.CharField(max_length=50, help_text="The last name of the parent.")
    cell_phone = models.CharField(max_length=15, help_text="The cell phone number of the parent.")
    email = models.EmailField(help_text="The email address of the parent.")
    address = models.TextField(help_text="The address of the parent.")
    city = models.CharField(max_length=100, help_text="The city of the parent's address.")
    province = models.CharField(max_length=3, help_text="The province or state abbreviation of the parent's address.")
    postal_code = models.CharField(max_length=6, help_text="The postal code of the parent's address.")
    should_correspond = models.BooleanField(help_text="Indicates whether the parent should receive correspondence.")

    def __str__(self):
        """
        Returns a string representation of the parent.
        """
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    """
    Represents a student in the application.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        cell_phone (str): The cell phone number of the student.
        email (str): The email address of the student.
        allergies_medical (str): Information about any allergies or medical conditions of the student.
        media_ok (bool): Indicates whether media coverage is allowed for the student.
        parents (ManyToManyField[Parent]): The parents associated with the student.
        teachers (ManyToManyField[Teacher]): The teachers associated with the student.
        instruments (ManyToManyField[Instrument]): The instruments played by the student.

    Fields:
        - first_name: CharField
        - last_name: CharField
        - cell_phone: CharField
        - email: EmailField
        - allergies_medical: CharField
        - media_ok: BooleanField
        - parents: ManyToManyField[Parent]
        - teachers: ManyToManyField[Teacher]
        - instruments: ManyToManyField[Instrument]

    Methods:
        - __str__: Returns a string representation of the student.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, help_text="The first name of the student.")
    last_name = models.CharField(max_length=50, help_text="The last name of the student.")
    dob = models.DateField(help_text="Student date of birth")
    cell_phone = models.CharField(max_length=15, help_text="The cell phone number of the student.")
    email = models.EmailField(help_text="The email address of the student.")
    allergies_medical = models.CharField(max_length=250, help_text="Information about any allergies or medical conditions of the student.")
    media_ok = models.BooleanField(default=True, help_text="Indicates whether media coverage is allowed for the student.")
    # parents = models.ManyToManyField(Parent, help_text="The parents associated with the student.")
    teachers = models.ManyToManyField(Teacher, help_text="The teachers associated with the student.")
    instruments = models.ManyToManyField(Instrument, help_text="The instruments played by the student.")

    def __str__(self):
        """
        Returns a string representation of the student.
        """
        return f"{self.first_name} {self.last_name}"


class Event(models.Model):
    """
    Represents an event in the application.

    Attributes:
        name (str): The name of the event.
        date (datetime.date): The date of the event.
        location (str): The location where the event will take place.
        reg_open_date (datetime.date): The date when event registration opens.
        reg_close_date (datetime.date): The date when event registration closes.
        more_info_link (str): A link to additional information about the event.
        students (ManyToManyField[Student]): The students registered for the event.

    Fields:
        - name: CharField
        - date: DateField
        - location: CharField
        - reg_open_date: DateField
        - reg_close_date: DateField
        - more_info_link: CharField
        - students: ManyToManyField[Student]

    Methods:
        - __str__: Returns a string representation of the event.
    """

    name = models.CharField(max_length=100, help_text="The name of the event.")
    date = models.DateField(help_text="The date of the event.")
    location = models.CharField(max_length=250, help_text="The location where the event will take place.")
    reg_open_date = models.DateField(help_text="The date when event registration opens.")
    reg_close_date = models.DateField(help_text="The date when event registration closes.")
    more_info_link = models.CharField(max_length=250, help_text="A link to additional information about the event.")
    students = models.ManyToManyField(Student, help_text="The students registered for the event.")

    def __str__(self):
        """
        Returns a string representation of the event.
        """
        return self.name
