from django.db import models, IntegrityError
from appmanager.core.models import User, BaseTimeStampModel
from appmanager.administrative.models import Province,City,Villages,District
import base64
import os

def generate_id():
    r_id = base64.b64encode(os.urandom(6)).decode('ascii')
    r_id = r_id.replace(
        '/', '').replace('_', '').replace('+', '').strip()
    return r_id

class Restaurant(BaseTimeStampModel):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owned_restaurant')
    name = models.CharField(max_length=300)
    phone_resto = models.CharField(max_length=12)
    description = models.TextField(null=True, blank=True)
    resto_province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='resto_in_province')
    resto_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='resto_in_city')
    resto_district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='resto_in_district')
    resto_village = models.ForeignKey(Villages, on_delete=models.CASCADE, related_name='resto_in_village')
    resto_street_address = models.CharField(max_length=300)
    resto_zip_code = models.CharField(max_length=25)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_id()
            success = False
            failures = 0
            while not success:
                try:
                    super(User, self).save(*args, **kwargs)
                except IntegrityError:
                    failures += 1
                    if failures > 5:  # or some other arbitrary cutoff point at which things are clearly wrong
                        raise KeyError
                    else:
                        # looks like a collision, try another random value
                        self.id = generate_id()
                else:
                    success = True
        else:
            super(User, self).save(*args, **kwargs)