import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        sections = node.text.split(delimiter)
        sections_length = len(sections)

        if sections_length % 2 == 0:
            raise Exception(f"Missing matching pair of delimeter {delimiter}")

        split_nodes = []

        for i in range(sections_length):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))

        new_nodes.extend(split_nodes)

    return new_nodes


def extract_markdown_images(text):
    images = []
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    images.extend(matches)
    return images


def extract_markdown_links(text):
    links = []
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    links.extend(matches)
    return links

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        old_node_text = old_node.text
        images = extract_markdown_images(old_node_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        for image in images:
            image_alt = image[0]
            image_url = image[1]
            sections = old_node_text.split(f"![{image_alt}]({image_url})", 1)
            
            if len(sections) != 2:
                raise ValueError("Markdown invalid: image section was not closed")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
            old_node_text = sections[1]

        if old_node_text != "":
            new_nodes.append(TextNode(old_node_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        old_node_text = old_node.text
        links = extract_markdown_links(old_node_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        for link in links:
            link_alt = link[0]
            link_url = link[1]
            sections = old_node_text.split(f"[{link_alt}]({link_url})", 1)
            
            if len(sections) != 2:
                raise ValueError("Markdown invalid: link section was not closed")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(link_alt, TextType.LINK, link_url))
            old_node_text = sections[1]

        if old_node_text != "":
            new_nodes.append(TextNode(old_node_text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)

    nodes = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
