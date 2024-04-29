from rest_framework.serializers import HyperlinkedModelSerializer
from kaland.models import Location

class LocationSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'