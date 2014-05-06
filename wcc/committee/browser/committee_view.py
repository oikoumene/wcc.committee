from five import grok
from plone.directives import dexterity, form
from wcc.committee.content.committee import ICommittee
from plone.api.portal import get_tool

grok.templatedir('templates')


class Index(dexterity.DisplayForm):
    grok.context(ICommittee)
    grok.require('zope2.View')
    grok.template('committee_view')
    grok.name('view')

    def get_country_info(self, country_code):
        catalog = get_tool('portal_catalog')
        return catalog(portal_type="wcc.churches.country",
                       countries=country_code)
