from collective.blog.feeds.viewlets import FeedsViewlet as ViewletBase
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile

class FeedsViewlet(ViewletBase):
    render = ViewPageTemplateFile('feedsviewlet.pt')
