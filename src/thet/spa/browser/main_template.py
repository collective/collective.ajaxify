from Products.CMFPlone.browser.interfaces import IMainTemplate
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implementer


@implementer(IMainTemplate)
class MainTemplate(BrowserView):
    ajax_template_name = "templates/main_template_ajax.pt"
    main_template_name = "templates/main_template.pt"

    def __call__(self):
        return ViewPageTemplateFile(self.template_name)

    @property
    def template_name(self):
        # Return the ajax or non-ajax version of the main template, depending
        # on a Ajax request or not.
        # NOTE: The ajax_load parameter is set in `adm.sfd.site.theme.set_theme.
        if self.request.get("ajax_load"):
            self.request.response.setHeader("sfd-template", "main_template_ajax")
            return self.ajax_template_name

        self.request.response.setHeader("sfd-template", "main_template")
        return self.main_template_name

    @property
    def macros(self):
        # Reinstantiating the templatefile is a workaround for
        # https://github.com/plone/Products.CMFPlone/issues/2666
        # Without this an infinite recursion in a template
        # (i.e. a template that calls its own view)
        # kills the instance instead of raising a RecursionError.
        return ViewPageTemplateFile(self.template_name).macros


class MainTemplateContent(MainTemplate):
    """Core content template used in main_template.pt.
    This is the same as the main_template_ajax.pt.
    """

    @property
    def template_name(self):
        return "templates/main_template_ajax.pt"
