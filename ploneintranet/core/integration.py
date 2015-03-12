# -*- coding: utf-8 -*-
from zope.component import queryUtility

try:
    from ploneintranet.microblog.interfaces import IMicroblogTool
    from ploneintranet.microblog.utils import get_microblog_context
    HAVE_PLONEINTRANET_MICROBLOG = True
except ImportError:
    HAVE_PLONEINTRANET_MICROBLOG = False

try:
    from ploneintranet.network.interfaces import INetworkTool
    HAVE_PLONEINTRANET_NETWORK = True
except ImportError:
    HAVE_PLONEINTRANET_NETWORK = False


class PloneIntranetIntegration(object):
    """Provide runtime utility lookup that does not throw
    ImportErrors if some components are not installed."""

    @property
    def microblog(self):
        if HAVE_PLONEINTRANET_MICROBLOG:
            return queryUtility(IMicroblogTool)
        else:
            return None

    @property
    def network(self):
        if HAVE_PLONEINTRANET_NETWORK:
            return queryUtility(INetworkTool)
        else:
            return None

    def context(self, context):
        if HAVE_PLONEINTRANET_MICROBLOG:
            return get_microblog_context(context)
        else:
            return None

PLONEINTRANET = PloneIntranetIntegration()
