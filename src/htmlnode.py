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
