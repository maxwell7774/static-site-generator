import unittest

from block_markdown import BlockType, block_to_block_type, markdown_to_blocks, markdown_to_html_node
from htmlnode import HTMLNode
from leafnode import LeafNode


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks_empty(self):
        markdown = ""
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            [],
            blocks
        )

    def test_markdown_to_blocks_single(self):
        markdown = "# This is a heading"
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            ["# This is a heading"],
            blocks
        )

    def test_markdown_to_blocks_multiple(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
            ],
            blocks
        )

    def test_block_to_block_type_paragraph(self):
        block = "This is a block of heading 1\nThis is a newline"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_block_type_heading(self):
        block = "# This is a block of heading 1"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, block_type)

    def test_block_to_block_type_code(self):
        block = "```\nThis is a block of heading 1\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.CODE, block_type)

    def test_block_to_block_type_quote(self):
        block = ">This is a block of heading 1\n>This is the second line\n>This is the third line"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.QUOTE, block_type)

    def test_block_to_block_type_unordered_list_asterick(self):
        block = "* Item 1\n* Item 2\n* Item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.UNORDERED_LIST, block_type)

    def test_block_to_block_type_unordered_list_hyphen(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.UNORDERED_LIST, block_type)

    def test_block_to_block_type_ordered_list(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.ORDERED_LIST, block_type)

    def test_markdown_to_html_node_heading(self):
        markdown = "# heading 1"
        node = markdown_to_html_node(markdown)
        needed_node = HTMLNode(
            "div",
            children=[
                HTMLNode("h1", children=[
                    LeafNode(None, value="heading 1")
                ]),
            ]
        )
        self.assertEqual(repr(needed_node), repr(node))

    def test_markdown_to_html_node_all_headings(self):
        markdown = "# heading 1\n\n## heading 2\n\n### heading 3\n\n#### heading 4\n\n##### heading 5\n\n###### heading 6"
        node = markdown_to_html_node(markdown)
        needed_node = HTMLNode(
            "div",
            children=[
                HTMLNode("h1", children=[
                    LeafNode(None, value="heading 1")
                ]),
                HTMLNode("h2", children=[
                    LeafNode(None, value="heading 2")
                ]),
                HTMLNode("h3", children=[
                    LeafNode(None, value="heading 3")
                ]),
                HTMLNode("h4", children=[
                    LeafNode(None, value="heading 4")
                ]),
                HTMLNode("h5", children=[
                    LeafNode(None, value="heading 5")
                ]),
                HTMLNode("h6", children=[
                    LeafNode(None, value="heading 6")
                ]),
            ]
        )
        self.assertEqual(repr(needed_node), repr(node))




if __name__ == "__main__":
    unittest.main()
