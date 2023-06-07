import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if level >= maxdepth:
        maxdepth = level + 1
    for child in elem:
        depth(child, level +1)
N= int(input())
xml_lines = []
for _ in range(N):
    xml_lines.append(input())
    xml_str = '\n'.join(xml_lines)
tree = etree.ElementTree(etree.fromstring(xml_str))
root = tree.getroot()
depth(root, 0)
print(maxdepth - 1)





