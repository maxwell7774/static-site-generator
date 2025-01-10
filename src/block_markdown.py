def markdown_to_blocks(markdown):
    blocks = []
    sections = markdown.split("\n\n")
    for section in sections:
        if section  == "":
            continue
        blocks.append(section.strip(" "))

    return blocks
