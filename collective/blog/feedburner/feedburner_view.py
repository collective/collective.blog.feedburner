from Products.Five.browser import BrowserView
from Products.statusmessages.interfaces import IStatusMessage
from zope.interface import implements

from collective.blog.feedburner.feedurlmanager import FeedManagerAdapter
from collective.blog.feedburner.interfaces import IFeedburnerView

class FeedburnerView(BrowserView):
    """View class for the feedburner
    """
    implements(IFeedburnerView)

    def getFeedBurnerProperties(self):
        """ Returns the locally defined feedburner for the item """
        adapter = FeedManagerAdapter(self.context)
        dico = adapter.getFeedURL()
        return dico

    def setFeedBurnerProperties(self):
        """ Saves the locally defined properties for a Slideshow """
        status = IStatusMessage(self.request)
        adapter = FeedManagerAdapter(self.context)
        feedburnerurl, use_feedburner, use_fastsyndication = '', '', ''
        if self.request.form.has_key('feedburnerurl'):
            feedburnerurl = self.request.form['feedburnerurl']
        if self.request.form.has_key('use_feedburner'):
            use_feedburner = self.request.form['use_feedburner']
        else:
            use_feedburner = 'no'
        if self.request.form.has_key('use_fastsyndication'):
            use_fastsyndication = self.request.form['use_fastsyndication']
        else:
            use_fastsyndication = 'no'
        if use_feedburner != 'yes' or feedburnerurl:
            adapter.setFeedURL(use_fastsyndication, use_feedburner,
                               feedburnerurl)
            status.addStatusMessage(
                'Local feedburner properties have been saved',
                type='info')
        else:
            status.addStatusMessage('Missing properties',
                                type='info')
        self.request.response.redirect(self.request.URL.split('@@')[0])
