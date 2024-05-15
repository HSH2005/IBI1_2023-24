import xml.dom.minidom
import time
start = time.time()
count1 = 0
count2 = 0
count3 = 0
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
namespaces = collection.getElementsByTagName('namespace')
for namespace in namespaces:
	ontology = namespace.firstChild.nodeValue.strip()
	if ontology == "molecular_function" : count1 += 1
	if ontology == "biological_process" : count2 += 1
	if ontology == "cellular_component" : count3 += 1
print(count1,count2,count3)
end = time.time()
runTime_ms = (end - start) * 1000
print("time is", runTime_ms, "millisecond")

import xml.sax
start = time.time()
class SMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.element_count = {}
        self.current_element = ""
 
    # 当遇到元素开始时调用
    def startElement(self, tag, attributes):
        self.current_element = tag
 
    # 当遇到元素结束时调用
    def endElement(self, tag):
        if self.current_element in self.element_count:
            self.element_count[self.current_element] += 1
        else:
            self.element_count[self.current_element] = 1
        self.current_element = ""
 
# 使用SAX解析器解析SML文件
def parse_sml_file(file_path, element_name):
    parser = xml.sax.make_parser()
    handler = SMLHandler()
    parser.setContentHandler(handler)
    parser.parse(file_path)
    return handler.element_count.get(element_name, 0)
 
# 示例SML文件路径
sml_file_path = 'heshenghaodeMacBook-Pro/Users/heshenghao/Desktop/practical14/go_obo.sml'
# 要计算的元素名称
element_name = 'molecular_function'
# 计算元素数量
count = parse_sml_file(sml_file_path, element_name)
count4 = count
print(f"{count}")
count = 0
element_name = 'biological_process'
count = parse_sml_file(sml_file_path, element_name)
count5 = count
print(f"{count}")
count = 0
element_name = 'cellular_component'
count = parse_sml_file(sml_file_path, element_name)
print(f"{count}")
count6 = count

end = time.time()
runTime_ms1 = (end - start) * 1000
print("time is", runTime_ms1, "millisecond")

if runTime_ms > runTime_ms1:
    print("SAX is faster")
else:
    print("DOM is better")

import matplotlib.pyplot as plt
list = ['molecular_function','biological_process',"cellular_component"]
list1 = [count1,count2,count3]
list2 = [count4,count5,count6]
plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
plt.bar(list,list1,color=['b'],width=0.5,hatch='\\')
for a,b,i in zip(list,list1,range(len(list))):
    plt.text(a,b+0.03,"%.2f"%list1[i],ha='center',fontsize=10)
plt.title('DOM')
plt.ylabel('frequency')
plt.xlabel('ontologies')

plt.subplot(1,2,2)
plt.bar(list,list2,cplpr=['r'],width=0.5,hatch='/')
for a,b,i in zip(list,list2,range(len(list))):
    plt.text(a,b+0.03,"%.2f"%list2[i],ha='center',fontsize=10)
plt.title('SAX')
plt.ylabel('frequency')
plt.xlabel('ontologies')
plt.show
plt.clf