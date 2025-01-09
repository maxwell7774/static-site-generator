import unittest

from inline_markdown import split_nodes_delimiter, extract_markdown_links, extract_markdown_images, split_nodes_image, split_nodes_link
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

    def test_extract_images_empty(self):
        text = "This is text with a"
        images = extract_markdown_images(text)
        self.assertListEqual(
            [],
            images
        )

    def test_extract_images_single(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        images = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif")
            ],
            images
        )

    def test_extract_images_multiple(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            images
        )

    def test_extract_links_empty(self):
        text = "This is text with a link"
        links = extract_markdown_links(text)
        self.assertListEqual(
            [],
            links
        )

    def test_extract_links_single(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        links = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
            ],
            links
        )

    def test_extract_links__multiple(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev")
            ],
            links
        )

    def test_split_nodes_image_empty(self):
        node = TextNode(
            "This is text with a ",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
            ],
            new_nodes
        )


    def test_split_nodes_image_single(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            ],
            new_nodes
        )

    def test_split_nodes_image_multiple(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", TextType.TEXT),
                TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            new_nodes
        )

    def test_split_nodes_link_empty(self):
        node = TextNode(
            "This is text with a link ",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
            ],
            new_nodes
        )

    def test_split_nodes_link_single(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            ],
            new_nodes
        )

    def test_split_nodes_link_multiple(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
            ],
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()
