from Products.CMFPlone.browser import main_template
from Products.CMFPlone.browser.interfaces import IMainTemplate
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implementer


@implementer(IMainTemplate)
class MainTemplate(main_template.MainTemplate):
    ajax_template_name = ViewPageTemplateFile("main_template_ajax.pt")
    main_template_name = ViewPageTemplateFile("main_template.pt")


class MainTemplateContent(MainTemplate):
    """Core content template used in main_template.pt.
    This is the same as the main_template_ajax.pt.
    """

    @property
    def template_name(self):
        return "templates/main_template_ajax.pt"
