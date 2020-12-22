from rest_framework import viewsets


class BaseViewSet(viewsets.ModelViewSet):
    """
    Base viewset
    """
    queryset = None
    serializer_class = None
    
    @property
    def access_policy(self):
        return self.permission_classes[0]

    def get_queryset(self):
        return self.access_policy.scope_queryset(
            self.request, self.queryset
        )
