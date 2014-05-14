from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent
from collective import dexteritytextindexer
from plone.multilingualbehavior.directives import languageindependent
from wcc.churches.source import ObjectProvidesPathSourceBinder

from wcc.committee import MessageFactory as _


# Interface class; used to define content-type schema.

class ICommittee(form.Schema, IImageScaleTraversable):
    """
    """
    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
        title=_(u"Name"),
        description=_(u"First and last name of the committee member"),
        required=True
        )

    committee_title = schema.TextLine(
        title=_(u"Title"),
        description=_(u"Title of the committee member"),
        required=True
        )

    description = schema.Text(
        title=_(u"Description"),
        description=_(u"Description of the committee member"),
        required=False
        )

    languageindependent("committee_churchmember")
    dexteritytextindexer.searchable('committee_churchmember')
    committee_churchmember = RelationChoice(
        title=_(u'Church'),
        source=ObjectProvidesPathSourceBinder(
            object_provides='wcc.churches.churchmember.IChurchMember'),
        required=False
    )

    languageindependent('committee_country')
    dexteritytextindexer.searchable('committee_country')
    committee_country = schema.Choice(
        title=_(u'Country'),
        vocabulary='wcc.vocabulary.country',
        description=_(u''),
        required=False,
        )

    languageindependent('image')
    image = NamedBlobImage(
        title=_(u"Photo"),
        description=_(u"Size 290x400 for best result"),
        required=False
        )


alsoProvides(ICommittee, IFormFieldProvider)
