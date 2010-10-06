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

    def setFeedURL(self, usefs, usefb, data):
        self.annotations[FEED_MANAGER_PROPERTIES]['use_fastsyndication'] =\
                usefs
        self.annotations[FEED_MANAGER_PROPERTIES]['use_feedburner'] = usefb
        self.annotations[FEED_MANAGER_PROPERTIES]['feedburnerurl'] = data
