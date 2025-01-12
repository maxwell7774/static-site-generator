import unittest

from generate_html import extract_title


class TestGenerateHTML(unittest.TestCase):
    def test_extract_title_from_markdown(self):
        markdown = """
# This is the title

This is not a title
            """
        self.assertEqual("This is the title", extract_title(markdown))

    def test_extract_title_from_markdown_error(self):
        markdown = """
This is the title

This is not a title
            """
        def callable():
            extract_title(markdown)

        self.assertRaises(Exception, callable)


if __name__ == "__main__":
    unittest.main()
