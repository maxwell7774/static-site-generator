from textnode import TextNode, TextType
def main():
    text_node = TextNode("Test", TextType.BOLD, "https://google.com")
    print(text_node)

if __name__ == "__main__":
    main()
