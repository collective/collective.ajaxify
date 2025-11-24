from Products.CMFPlone.browser import main_template
from Products.CMFPlone.browser.interfaces import IMainTemplate
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implementer
from plone.memoize.view import memoize


@implementer(IMainTemplate)
class MainTemplate(main_template.MainTemplate):
    """ reimplementation of 6.2 main_template logic for Plone 6.1 """

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
            pass

        if "ajax_load" in self.request:
            return bool(self.request.get("ajax_load", False))

        # defaults to False
        return False

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
