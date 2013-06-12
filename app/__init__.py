__all__ = ['classifier','feeds','searcher']

VERSION=('0','0','1')
VERSION_STRING = '.'.join(VERSION)


DEFAULT_CONFIG=[
        ("DEBUG",True),
        ]

class _App(object):
    """app to wrap all functions and trigger scheduled tasks"""

    def __init__(self):
        """initialize an app with default configs """
        super(_App,self).__init__()
        self.read_config(DEFAULT_CONFIG)
        # TODO: implement this function

    def read_config(self, configs):
        """read from configs as an module or objects

        :configs: the confings kept in an object or module
        :returns: None

        """
        # TODO: implement this function
        pass

    def start(self):
        """start to work
        :returns: None

        """
        # TODO: implement this function
        pass

mainapp = _App()
