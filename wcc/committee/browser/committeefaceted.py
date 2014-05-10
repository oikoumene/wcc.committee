from five import grok
from Products.CMFCore.interfaces import IContentish

grok.templatedir('templates')

class CommitteeFaceted(grok.View):
    grok.context(IContentish)
    grok.name('committeefaceted')
    grok.require('zope2.View')
    grok.template('committeefaceted')

    def trim_text(self, value):
        if len(value) > 80:
            return value[:85] + "..."
        return value
