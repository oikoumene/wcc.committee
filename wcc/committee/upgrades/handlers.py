from collective.grok import gs
from Products.CMFCore.utils import getToolByName
from plone.app.textfield.value import RichTextValue

# -*- extra stuff goes here -*- 


@gs.upgradestep(title=u'Upgrade wcc.committee to 2',
                description=u'Upgrade wcc.committee to 2',
                source='1', destination='2',
                sortkey=1, profile='wcc.committee:default')
def to2(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.committee.upgrades:to2')

    catalog = getToolByName(context, 'portal_catalog')

    for brain in catalog(portal_type=['wcc.committee.committee'], Language='all'):

        obj = brain.getObject()

        obj.description = RichTextValue(obj.description,
                                        'text/plain',
                                        'text/html')
        obj.reindexObject()
