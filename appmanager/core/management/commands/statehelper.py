import datetime
from appmanager.administrative.models import City,Province,Villages,District
import csv


def create_province():
    with open('datahelper/provinces.csv',encoding='utf-8-sig') as files:
        reader = csv.DictReader(files, delimiter=';')
        obj = Province.objects.count()
        if obj < 1:
            objs = [
                    Province(
                        id=e['id'],
                        name=e['name'],

                    )
                    for e in reader
                ]
            province = Province.objects.bulk_create(objs)
            files.close()
            return province
        return Province


def create_regency():
    with open('datahelper/regencies.csv',encoding='utf-8-sig') as files:
        reader = csv.DictReader(files, delimiter=';')
        obj = City.objects.count()
        if obj < 1:
            objs = [
                    City(
                        id=e['id'],
                        province=Province.objects.get(id=e['province_id']),
                        name=e['name'],

                    )
                    for e in reader
                ]
            city = City.objects.bulk_create(objs)
            files.close()
            return city
        return City

def create_district():
    with open('datahelper/districts.csv',encoding='utf-8-sig') as files:
        reader = csv.DictReader(files, delimiter=';')
        obj = District.objects.count()
        if obj < 1:
            objs = [
                    District(
                        id=e['id'],
                        city=City.objects.get(id=e['regency_id']),
                        name=e['name'],
                    )
                    for e in reader
                ]
            districts = District.objects.bulk_create(objs)
            files.close()
            return districts
        return District

def create_villages():
    with open('datahelper/villages.csv',encoding='utf-8-sig') as files:
        reader = csv.DictReader(files, delimiter=';')
        obj = Villages.objects.count()
        if obj < 1:
            objs = [
                    Villages(
                        id=e['id'],
                        district=District.objects.get(id=e['district_id']),
                        name=e['name'],
                    )
                    for e in reader
                    ]
            villages = Villages.objects.bulk_create(objs)
            files.close()
            return villages
        return Province