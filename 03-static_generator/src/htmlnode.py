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
  
