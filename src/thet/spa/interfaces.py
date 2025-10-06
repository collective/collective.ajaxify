from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.app.contenttypes.interfaces import IPloneAppContenttypesLayer


class IBrowserLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IFrontendTheme(IDefaultBrowserLayer, IPloneAppContenttypesLayer):
    """Marker interface for the frontend theme layer."""
