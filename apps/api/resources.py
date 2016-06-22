from tastypie.resources import ModelResource
from ..resources.models import Resources


class ResourcesModelResource(ModelResource):
    class Meta:
        queryset = Resources.objects.all()
        allowed_methods = ['get']
