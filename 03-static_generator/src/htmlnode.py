class HTMLNode:
  def __init__(self, tag=None, value=None, children=None,props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  
  def to_html(self):
    raise NotImplementedError("to_html method not implemented")
  
  def props_to_html(self):
    props = ""
    if self.props is None:
      return props
    for prop in self.props:
      props += f' {prop}="{self.props[prop]}"'
    
    return props
  
  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
  

class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag, value, None, props)

  def to_html(self):
    if not self.value:
      raise ValueError('Not provided')
    
    if not self.tag:
      return self.value
    
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
  
  def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
  
