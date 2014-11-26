__author__ = 'rospena'

#NOTE: Static methods doesn't use the self parameter
class Utilities(object):

    @staticmethod
    def config(section, settings):
        value = {}
        options = settings.options(section)

        for option in options:
            try:
                value[option] = settings.get(section, option)
                if value[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                value[option] = None

        return value