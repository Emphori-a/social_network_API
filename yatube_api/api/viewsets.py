from rest_framework import mixins
from rest_framework import viewsets


class ListAndCreateViewSet(mixins.CreateModelMixin,
                           mixins.ListModelMixin, viewsets.GenericViewSet):
    pass
