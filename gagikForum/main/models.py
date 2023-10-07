from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
import random
import string
GENDER_CHOICE = (("Male", "М"), ("Woman", "Ж"))
EDUCATION_CHOICE = (
    ("1", "Дошкольное"),
    ("2", "Начальное общее — 1—4 классы"),
    ("3", "Основное общее — 5—9 классы"),
    ("4", "Среднее общее — 10—11 классы"),
    ("5", "Среднее профисеональное"),
    ("6", "Высшее I степени — бакалавриат"),
    ("7", "Высшее II степени — специалитет, магистратура"),
    ("8", "Высшее III степени — подготовка кадров высшей квалификации")
)


class User(AbstractUser):
    image = models.ImageField(upload_to="Users", default="Users/no-image.svg", verbose_name="Фото", null=True)
    wasBorn = models.DateField(verbose_name="Дата рождения", null=True)
    # rang = models.ManyToManyField("Rang", blank=True, related_name="rang", verbose_name="Роль")
    my_story = models.TextField(verbose_name="Об авторе", null=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICE, verbose_name="Гендер")
    education = models.CharField(max_length=255, choices=EDUCATION_CHOICE, verbose_name="Образование")
    phone_number = PhoneNumberField(verbose_name = 'Номер телефона')
    code_word = models.CharField(max_length=255, verbose_name="Кодовое слово", default=''.join(random.choices(string.ascii_uppercase + string.digits, k=4)))
    country = models.CharField(max_length=255, verbose_name="Страна", null=True)
    region = models.CharField(max_length=255, verbose_name="Область(Только для россиян)", null=True)
    # my_contests = models.ManyToManyField("Contest", blank = True, related_name="my_contests", verbose_name="Мои конкурсы")

