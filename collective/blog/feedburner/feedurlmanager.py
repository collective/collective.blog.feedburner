from zope.annotation.interfaces import IAnnotations
from persistent.dict import PersistentDict

FEED_MANAGER_PROPERTIES = 'blog.feedburner.props'

class FeedManagerAdapter(object):
    """
    """

    def __init__(self, context):
        self.context = context
        self.annotations = IAnnotations(self.context)
        if self.annotations.get(FEED_MANAGER_PROPERTIES, None) is None:
            self.annotations[FEED_MANAGER_PROPERTIES] = PersistentDict()

    def getFeedURL(self):
        return self.annotations[FEED_MANAGER_PROPERTIES]

    def setFeedURL(self, use, data):
        self.annotations[FEED_MANAGER_PROPERTIES]['use_feedburner'] = use
        self.annotations[FEED_MANAGER_PROPERTIES]['feedburnerurl'] = data
