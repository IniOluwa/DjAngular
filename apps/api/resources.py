from tastypie.resources import ModelResource
from ..resources.models import Resources


class ResourcesModelResource(ModelResource):
    """ Api facet """
    class Meta:
        queryset = Resources.objects.all()
        resource_name = 'resource'
        allowed_methods = ['get', 'post', 'patch', 'delete']
        # authorization = Authorization()
        # authentication = Authentication()
        always_return_data = True
