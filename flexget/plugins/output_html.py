import os
import logging
from flexget.plugin import *

log = logging.getLogger('make_html')


class OutputHtml:

    # TODO: implement
    def __validator(self):
        from flexget import validator
        return validator.factory('text')

    def on_feed_output(self, feed):
        try:
            from Cheetah.Template import Template
        except:
            raise PluginError('make_html requires Cheetah template engine')

        config = feed.config['make_html']

        filename = os.path.expanduser(config['template'])
        output = os.path.expanduser(config['file'])

        import warnings
        warnings.simplefilter('ignore', UserWarning)

        # create the template
        template = Template(file=filename)

        # populate it
        template.accepted = feed.accepted
        template.rejected = feed.rejected
        template.entries = feed.entries

        f = open(output, 'w')
        f.write(template.__str__())
        f.close()

register_plugin(OutputHtml, 'make_html')
