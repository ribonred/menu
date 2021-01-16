from django.db import models


class Province(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class City(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='province_city')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class District(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='district_of_city')
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Villages(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='villages_of_district')
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

