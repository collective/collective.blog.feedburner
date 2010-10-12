from Products.Five.browser import BrowserView
from Products.statusmessages.interfaces import IStatusMessage
from zope.interface import implements

from collective.blog.feedburner.feedurlmanager import FeedManagerAdapter
from collective.blog.feedburner.interfaces import IFeedburnerView

class FeedburnerView(BrowserView):
    """View class for the feedburner
    """
    implements(IFeedburnerView)

    def __init__(self, context, request):
        self.context = context
        self.request = request
        try:
            self.adapter = FeedManagerAdapter(self.context)
        except TypeError:
            # Could not adapt
            self.adapter = None

    def getFeedBurnerProperties(self):
        """ Returns the locally defined feedburner for the item """
        if self.adapter:
            return self.adapter.getFeedURL()
        return {}

    def setFeedBurnerProperties(self):
        """ Saves the locally defined properties for a Slideshow """
        status = IStatusMessage(self.request)
        form = self.request.form
        feedburnerurl = form.get('feedburnerurl', '')
        use_feedburner = form.get('use_feedburner', False)
        use_fastsyndication = form.get('use_fastsyndication', False)
        self.adapter.setFeedURL(use_fastsyndication,
                           use_feedburner,
                           feedburnerurl)
        status.addStatusMessage(
                'Local feedburner properties have been saved',
                type='info')
        self.request.response.redirect(self.context.absolute_url())
