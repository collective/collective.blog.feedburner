from plone.theme.interfaces import IDefaultPloneLayer
from zope.interface import Interface


class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """

class IFeedburnerView(Interface):
    """View class for the feedburner
    """

    def getFeedBurnerProperties(self):
        """ Returns the locally defined feedburner for the item """

    def setFeedBurnerProperties(self):
        """ Saves the locally defined properties for a Slideshow """
