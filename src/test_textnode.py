import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is another text node", TextType.TEXT, "https://google.com")
        node2 = TextNode("This is another text node", TextType.TEXT, "https://google.com")
        self.assertEqual(node, node2)

    def test_eq_false_text(self):
        node = TextNode("This is not the same text", TextType.ITALIC, "https://google.com")
        node2 = TextNode("This is another text node", TextType.ITALIC, "https://google.com")
        self.assertNotEqual(node, node2)

    def test_eq_false_text_type(self):
        node = TextNode("This is another text node", TextType.IMAGE, "https://google.com")
        node2 = TextNode("This is another text node", TextType.ITALIC, "https://google.com")
        self.assertNotEqual(node, node2)

    def test_eq_false_url(self):
        node = TextNode("This is another text node", TextType.ITALIC, "https://googles.com")
        node2 = TextNode("This is another text node", TextType.ITALIC, "https://google.com")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("Test Node", TextType.CODE, "https://google.com");
        self.assertEqual("TextNode(Test Node, code, https://google.com)", repr(node))

    def test_text_to_html(self):
        textnode = TextNode("This is a text type", TextType.TEXT)
        self.assertEqual(repr(text_node_to_html_node(textnode)), "LeafNode(None, This is a text type, None)")

    def test_bold_to_html(self):
        textnode = TextNode("This is bold", TextType.BOLD)
        self.assertEqual(repr(text_node_to_html_node(textnode)), "LeafNode(b, This is bold, None)")

    def test_italic_to_html(self):
        textnode = TextNode("This is italic", TextType.ITALIC)
        self.assertEqual(repr(text_node_to_html_node(textnode)), "LeafNode(i, This is italic, None)")

    def test_code_to_html(self):
        textnode = TextNode("def Testing(self):", TextType.CODE)
        self.assertEqual(repr(text_node_to_html_node(textnode)), "LeafNode(code, def Testing(self):, None)")

    def test_link_to_html(self):
        textnode = TextNode("This is a link", TextType.LINK, "https://google.com")
        self.assertEqual(repr(text_node_to_html_node(textnode)), "LeafNode(a, This is a link, {'href': 'https://google.com'})")

    def test_image_to_html(self):
        textnode = TextNode("This is an image", TextType.IMAGE, "https://image.url")
        self.assertEqual(repr(text_node_to_html_node(textnode)), "LeafNode(img, , {'src': 'https://image.url', 'alt': 'This is an image'})")

if __name__ == "__main__":
    unittest.main()
