import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_value_error(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_no_tag(self):
        node = LeafNode(None, "This is no tag")
        self.assertEqual(node.to_html(), "This is no tag")

    def test_to_html(self):
        node = LeafNode("div", "This is a div", {"class": "flex"})
        self.assertEqual(
            node.to_html(),
            '<div class="flex">This is a div</div>'
        )

    def test_repr(self):
        node = LeafNode("div", "This is a div", {"class": "flex"})
        self.assertEqual(
            repr(node),
            "LeafNode(div, This is a div, {'class': 'flex'})"
        )

if __name__ == "__main__":
    unittest.main()
