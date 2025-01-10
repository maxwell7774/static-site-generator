import unittest

from block_markdown import markdown_to_blocks

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

if __name__ == "__main__":
    unittest.main()
