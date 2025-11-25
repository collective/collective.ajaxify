from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.ajaxify


class CollectiveAjaxifyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.ajaxify)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.ajaxify:default")


COLLECTIVE_AJAXIFY_FIXTURE = CollectiveAjaxifyLayer()


COLLECTIVE_AJAXIFY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_AJAXIFY_FIXTURE,),
    name="CollectiveAjaxifyLayer:IntegrationTesting",
)


COLLECTIVE_AJAXIFY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_AJAXIFY_FIXTURE,),
    name="CollectiveAjaxifyLayer:FunctionalTesting",
)

COLLECTIVE_AJAXIFY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_AJAXIFY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="CollectiveAjaxifyLayer:AcceptanceTesting",
)
