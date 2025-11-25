from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import INonInstallable
from zope.component import getUtility
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles:
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "collective.ajaxify:uninstall",
        ]


def post_install(context):
    """Post install script"""
    registry = getUtility(IRegistry)

    try:
        registry["plone.use_ajax_main_template"] = True
    except KeyError:
        # Plone 6.1 compatibility
        pass
