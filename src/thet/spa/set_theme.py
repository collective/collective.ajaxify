from .interfaces import IFrontendTheme
from zope.interface import alsoProvides

# Use plone.app.theming / Plone standard theme only for these domains,
# starting with:
NOTHEME_DOMAINS = (
    "admin",
    "cms",
)


def set_theme(obj, event):
    """Set the theme in use."""
    request = event.request

    # Set the ajax_load parameter depending on an AJAX request or not.
    if request.getHeader("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
        print("ajax load")  # debug TODO
        request.set("ajax_load", "1")
    else:  # debug TODO
        print("NO ajax load")  # debug TODO

    # Maybe switch the theme.
    http_host = request.HTTP_HOST
    if not any((http_host.startswith(domain) for domain in NOTHEME_DOMAINS)):
        request.response.setHeader("X-Theme-Disabled", True)
        alsoProvides(request, IFrontendTheme)
