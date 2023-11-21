from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget

from tinydb import TinyDB, Query

db = TinyDB('db.json', indent=4)
template_db = db.table('MyForm')

def insert():
    existing_db = template_db.all()
    if not existing_db:
        template_db.insert_multiple([
            {'date': '1995-12-08', 'phone': '+7 908 105 80 73', 'email': 'alex@mail.ru', 'text': 'text', 'name': 'Alex'},
            {'date': '1996-12-08', 'phone': '+7 908 105 80 70', 'email': 'lena@mail.ru', 'text': 'text', 'name': 'Lena'},
            {'date': '1997-12-08', 'phone': '+7 908 105 80 79', 'email': 'vova@mail.ru', 'text': 'text', 'name': 'Vova'},
            {'date': '1998-12-08', 'phone': '+7 908 105 80 76', 'email': 'tanya@mail.ru', 'text': 'text', 'name': 'Tanya'},
            {'date': '1999-12-08', 'phone': '+7 908 105 80 83', 'email': 'yan@mail.ru', 'text': 'text', 'name': 'Yan'},
        ])

insert()

