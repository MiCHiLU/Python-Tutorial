class Point(object):
    """Example point class"""

    def __init__(self, x=0, y=0):
        # Note that self exists by now
        self.x, self.y = x, y

    def __repr__(self):
        return 'Point({0}.x, {0}.y)'.format(self)

    __str__ = __repr__

    def translate(self, deltax=None, deltay=None):
        """Translate the point"""
        if deltax:
            self.x += deltax
        if deltay:
            self.y += deltay
