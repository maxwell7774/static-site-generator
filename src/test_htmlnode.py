import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            "Hello World!",
            None,
            {"id": "div_1", "class": "m-3 p-3"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' id="div_1" class="m-3 p-3"'
        )
        
    def test_values(self):
        node = HTMLNode(
            "span",
            "I am a span",
            None
        )

        self.assertEqual(
            node.tag,
            "span"
        )

        self.assertEqual(
            node.value,
            "I am a span"
        )

        self.assertEqual(
            node.children,
            None
        )

        self.assertEqual(
            node.props,
            None
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "I am a p tag",
            None,
            {"class": "m-3 p-3"}
        )

        self.assertEqual(
            repr(node),
            "HTMLNode(p, I am a p tag, children: None, {'class': 'm-3 p-3'})"
        )
