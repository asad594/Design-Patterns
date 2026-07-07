# Structural patern woh pattern hai jo batatay ha ka classes 
#and objects ko kesay assemble karay large structures ma while 
# keeping strucure flexible and efficient

# Adapter pattern ka use hota ha jab hum existing class ko 
# dusri class ke interface ke sath compatible banana chahte hain.
# Ye pattern ek bridge provide karta hai jo incompatible 
# interfaces ko connect karta hai.

#like agr humare pass ek existing class hai jo kisi specific 
# interface ko implement karti hai, lekin humein us class ko 
# kisi dusri interface ke sath use karna hai, to hum adapter 
# pattern ka use karte hain. Adapter class existing class ko 
# wrap karti hai aur required interface ko implement karti hai.

import json
import xml.etree.ElementTree as ET

class XMLData:

    def get_data(self):
        return """
        <person>
            <name>Asad</name>
            <age>21</age>
        </person>
        """


class XMLToJSONAdapter:

    def __init__(self, xml_data):
        self.xml_data = xml_data

    def get_json(self):
        root = ET.fromstring(self.xml_data.get_data())

        data = {
            "name": root.find("name").text,
            "age": root.find("age").text
        }

        return json.dumps(data, indent=4)


xml = XMLData()
adapter = XMLToJSONAdapter(xml)

print("Converted XML to JSON using Adapter Pattern:")
print(adapter.get_json())