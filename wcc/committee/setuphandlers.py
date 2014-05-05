from collective.grok import gs
from wcc.committee import MessageFactory as _

@gs.importstep(
    name=u'wcc.committee', 
    title=_('wcc.committee import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.committee.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
