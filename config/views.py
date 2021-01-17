from django.views.generic import TemplateView
from appmanager.core.models import User
from django.core.serializers import serialize
from rest_framework import serializers
import json
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['first_name','email']
        model = User

class SpaPage(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = super(SpaPage, self).get_context_data(**kwargs)
        context['user'] = json.dumps(UserSerializer(User.objects.all(),many=True).data,indent=4)
        return context