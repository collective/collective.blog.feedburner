from collective.blog.feeds.viewlets import FeedsViewlet as ViewletBase
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

class FeedsViewlet(ViewletBase):
    render = ViewPageTemplateFile('feedsviewlet.pt')
