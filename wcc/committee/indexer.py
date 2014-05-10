from wcc.committee.content.committee import ICommittee
from plone.indexer.decorator import indexer


@indexer(ICommittee)
def committee_churchmember(obj):
    if obj.committee_churchmember:
        return obj.committee_churchmember.to_object.title
