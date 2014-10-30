""" Criteria widget
"""
from Products.Archetypes.public import Schema
from Products.Archetypes.public import BooleanField, BooleanWidget

from eea.facetednavigation.widgets import ViewPageTemplateFile
from eea.facetednavigation.widgets.widget import Widget as AbstractWidget
from eea.facetednavigation import EEAMessageFactory as _


EditSchema = Schema((
    BooleanField('hidecriteriaenabled',
        schemata="default",
        widget=BooleanWidget(
            label=_(u'Enable hide/show criteria'),
            description=_(u"Uncheck this box if you don't want hide/show "
                         "criteria feature enabled on this widget"),
            i18n_domain="eea"
        )
    ),
))

class Widget(AbstractWidget):
    """ Widget
    """
    # Widget properties
    widget_type = 'wcc_committe_filter'
    widget_label = _('Committee Filters')
    view_js = '++resource++wcc.committee.eeawidget.view.js'
    view_css = '++resource++wcc.committee.eeawidget.view.css'
    edit_css = '++resource++wcc.committee.eeawidget.edit.css'
    css_class = 'faceted-criteria-widget'

    index = ViewPageTemplateFile('widget.pt')
    edit_schema = AbstractWidget.edit_schema.copy() + EditSchema
    edit_schema['title'].default = 'Current search'
    edit_schema['hidecriteriaenabled'].default = False
