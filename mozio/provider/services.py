from provider.models import Provider

class ProviderService():

    def get_all(self):
        """
        A service for get all providers.
        """
        providers = Provider.objects.all()

        return providers
