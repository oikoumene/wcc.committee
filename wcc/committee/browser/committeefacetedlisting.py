from five import grok
from Products.CMFCore.interfaces import IContentish

grok.templatedir('templates')

class CommitteeFacetedListing(grok.View):
    grok.context(IContentish)
    grok.name('committeefacetedlisting')
    grok.require('zope2.View')
    grok.template('committeefacetedlisting')
