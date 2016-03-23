from wagtail.wagtailcore.models import Site


class SiteMiddleware(object):
    def process_request(self, request):
        """
        Set request.wagtail_site to contain the Site object responsible for handling this request,
        according to hostname matching rules
        """
        try:
            request.wagtail_site = Site.find_for_request(request)
        except Site.DoesNotExist:
            request.wagtail_site = None
