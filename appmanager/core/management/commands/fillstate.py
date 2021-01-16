from django.core.management import BaseCommand
import datetime
from .statehelper import create_province,create_regency,create_district,create_villages

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        province = create_province()
        regency = create_regency()
        district = create_district()
        village = create_villages()
