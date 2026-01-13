from plone.memoize.view import memoize
from Products.CMFPlone.browser import main_template
from Products.CMFPlone.browser.interfaces import IMainTemplate
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implementer


@implementer(IMainTemplate)
class MainTemplate(main_template.MainTemplate):
    """reimplementation of 6.2 main_template logic for Plone 6.1"""

    ajax_template = ViewPageTemplateFile("main_template_ajax.pt")
    main_template = ViewPageTemplateFile("main_template.pt")

    def __call__(self):
        return self.template()

    @property
    @memoize
    def use_ajax(self):
        try:
            # Plone 6.2 has "use_ajax" factory.
            return super().use_ajax
        except AttributeError:
            # From here on: Plone 6.1
            pass

        # Backport from Products.CMFPlone 6.2 main_template.py

        if "ajax_load" in self.request:
            return bool(self.request.get("ajax_load", False))

        is_ajax = self.request.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"
        if not is_ajax:
            # Not an ajax request. Use the normal main template.
            return False

        # ajax case.
        # defaults to True - we're in Plone 6.1 and want to make use of the
        # ajax main template. In 6.2 the automatic usage of the ajax main
        # template is configurable.
        return True

    @property
    def template(self):
        if self.use_ajax:
            return self.ajax_template
        else:
            return self.main_template

    @property
    def macros(self):
        return self.template.macros


class MainTemplateContent(MainTemplate):
    """Core content template used in main_template.pt.
    This is the same as the main_template_ajax.pt.
    """

    @property
    def template(self):
        return self.ajax_template
