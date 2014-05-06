from five import grok
from plone.directives import dexterity, form
from wcc.committee.content.committee import ICommittee

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ICommittee)
    grok.require('zope2.View')
    grok.template('committee_view')
    grok.name('view')

