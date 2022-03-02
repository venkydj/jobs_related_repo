import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','venkyjobs.settings')
import django
django.setup()

from testjobs.models import Hyderabadjobs
from faker import Faker
from random import *
fake=Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('project Manager','software Engineer','Associate Engineer','mean Stack','full stack','Mearn Stack'))
        feligibility=fake.random_element(elements=('Btech','Mtech','Mca','Bsc'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        bangalore_jobs_record=Hyderabadjobs.objects.get_or_create(
        date=fdate,
        company=fcompany,
        title=ftitle,
        eligibility=feligibility,
        address=faddress,
        email=femail,
        phonenumber=fphonenumber
        )
n=int(input("Enter Number of records:"))
populate(n)
print(f'{n} Records successfully inserted...')
