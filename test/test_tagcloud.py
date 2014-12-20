__author__ = 'kareem'

import unittest
from beetsplug.tagcloud.tagcloud import TagCloud

class TestTagCloud(unittest.TestCase):

    def test_constructor(self):
        tagcloud = TagCloud()
        self.assertIsNotNone(tagcloud)
        self.assertIsNotNone(TagCloud.ATTRIB_1_NAME)
        self.assertEqual("tag1", TagCloud.ATTRIB_1_NAME)
        self.assertIsNotNone(TagCloud.ATTRIB_2_NAME)
        self.assertEqual("tag2", TagCloud.ATTRIB_2_NAME)
        self.assertIsNotNone(TagCloud.ATTRIB_3_NAME)
        self.assertEqual("tag3", TagCloud.ATTRIB_3_NAME)



