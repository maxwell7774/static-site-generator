import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_no_tag(self):
        node = ParentNode(
            None,
            [
                LeafNode("p", "Hello I am a p tag"),
                LeafNode("div", "Hello I am a div tag"),
                LeafNode("span", "Hello I am a span tag"),
            ]
        )
        self.assertRaises(ValueError, node.to_html)

    def test_no_children(self):
        node = ParentNode(
            "div",
            None
        )
        self.assertRaises(ValueError, node.to_html)

    def test_empty_children(self):
        node = ParentNode(
            "div",
            []
        )
        self.assertRaises(ValueError, node.to_html)

    def test_to_html(self):
        node = ParentNode(
            "div",
            [
                ParentNode("div", [
                    LeafNode("p", "Hello I am a p tag"),
                ]),
                LeafNode(None, "Hello I am nothing"),
                LeafNode("span", "Hello I am a span tag"),
            ],
            {"class": "flex items-center"}
        )
        self.assertEqual(
            node.to_html(),
            '<div class="flex items-center"><div><p>Hello I am a p tag</p></div>Hello I am nothing<span>Hello I am a span tag</span></div>'
        )


    def test_repr(self):
        pass

if __name__ == "__main__":
    unittest.main()
