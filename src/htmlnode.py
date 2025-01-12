from block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This method has not yet been implemented")

    def props_to_html(self):
        if self.props == None:
            return ""
        attributes = list(map(lambda prop: f" {prop[0]}=\"{prop[1]}\"", self.props.items()))
        return "".join(attributes)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match(block_type):
            case(BlockType.PARAGRAPH):
                children.append(block_paragraph_to_html_node(block))
            case(BlockType.HEADING):
                children.append(block_heading_to_html_node(block))
            case(BlockType.CODE):
                children.append(block_code_to_html_node(block))
            case(BlockType.QUOTE):
                children.append(block_quote_to_html_node(block))
            case(BlockType.UNORDERED_LIST):
                children.append(block_unordered_list_to_html_node(block))
            case(BlockType.ORDERED_LIST):
                children.append(block_ordered_list_to_html_node(block))
    return HTMLNode(
        "div",
        children=children
    )


def block_paragraph_to_html_node(block):
    return HTMLNode(
        "p",
        children=text_to_children(block)
    )

def block_heading_to_html_node(block):
    sections = block.split(" ", 1)
    return HTMLNode(
        f"h{len(sections[0])}",
        children=text_to_children(sections[1])
    )

def block_code_to_html_node(block):
    lines = block.split("\n")
    code_node = HTMLNode(
        "code",
        children=text_node_to_html_node("\n".join(lines[1:-1]))
    )
    return HTMLNode(
        "pre",
        children=[code_node]
    )

def block_quote_to_html_node(block):
    lines = block.split("\n")
    for line in lines:
        line = line[2:]
    return HTMLNode(
        "blockquote",
        children=text_to_children("\n".join(lines))
    )

def block_unordered_list_to_html_node(block):
    lines = block.split("\n")
    li_nodes = []
    for line in lines:
        li_node = HTMLNode(
            "li",
            children=text_to_children(line[2:])
        )
        li_nodes.append(li_node)
    return HTMLNode(
        "ul",
        children=li_nodes
    )


def block_ordered_list_to_html_node(block):
    lines = block.split("\n")
    li_nodes = []
    for line in lines:
        li_node = HTMLNode(
            "li",
            children=text_to_children(line[3:])
        )
        li_nodes.append(li_node)
    return HTMLNode(
        "ol",
        children=li_nodes
    )

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes
