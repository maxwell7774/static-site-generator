import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextType, TextNode


class TestNodeTools(unittest.TestCase):
    def test_delimiter_bold(self):
        node = TextNode("This is my **bold** test", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is my ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" test", TextType.TEXT),
            ],
            new_nodes
        )

    def test_delimiter_double_bold(self):
        node = TextNode("This is my **double** trouble **bold** test", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is my ", TextType.TEXT),
                TextNode("double", TextType.BOLD),
                TextNode(" trouble ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" test", TextType.TEXT),
            ],
            new_nodes
        )

    def test_delimiter_italic(self):
        node = TextNode("This is my *italic* test", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is my ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" test", TextType.TEXT),
            ],
            new_nodes
        )

    def test_delimiter_bold_multiword(self):
        node = TextNode("This is my **double trouble bold** test", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is my ", TextType.TEXT),
                TextNode("double trouble bold", TextType.BOLD),
                TextNode(" test", TextType.TEXT),
            ],
            new_nodes
        )

    def test_delimiter_bold_and_italic(self):
        node = TextNode("This is my *italic* and **bold** test", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is my ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" test", TextType.TEXT),
            ],
            new_nodes
        )

    def test_delimiter_code(self):
        node = TextNode("This is my `code` test", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is my ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" test", TextType.TEXT),
            ],
            new_nodes
        )

    def test_not_closed_delimiter(self):
        node = TextNode("This is my `code test", TextType.TEXT)
        def callable():
            return  split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertRaises(Exception, callable)

if __name__ == "__main__":
    unittest.main()
