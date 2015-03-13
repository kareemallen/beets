from beets.autotag.match import tag_album
from beets.plugins import BeetsPlugin
from beets.ui import Subcommand

tagcloud_command = Subcommand('add-tag', help='Add a tag to the tagcloud' )

def add_tag(lib, opts, args):
    print 'Add tag here'

tagcloud_command.func = add_tag

class TagCloud(BeetsPlugin):
    ATTRIB_1_NAME = "tag1"

    ATTRIB_2_NAME = "tag2"

    ATTRIB_3_NAME = "tag3"

    def commands(self):
        return [tagcloud_command]
