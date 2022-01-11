from typing import Optional
import xml.etree.ElementTree as ET

class Spell():
    name: str
    level: int = 0
    school: str = ""
    ritual: bool = False
    time: str = ""
    range: str = ""
    components: Optional[str] = None
    duration: Optional[str] = None
    classes: str = ""
    description: str = ""
    roll: Optional[str] = None
    
    def to_xml(self) -> ET.ElementTree:
        spell_element = ET.Element("spell")
        
        name_element = ET.SubElement(spell_element, "name")
        name_element.text = self.name
        
        level_element = ET.SubElement(spell_element, "level")
        level_element.text = str(self.level)
        
        school_element = ET.SubElement(spell_element, "school")
        school_element.text = self.school
        
        ritual_element = ET.SubElement(spell_element, "ritual")
        if self.ritual:
            ritual_element.text = "YES"
        else:
            ritual_element.text = "NO"
        
        time_element = ET.SubElement(spell_element,"time")
        time_element.text = self.time
        
        range_element = ET.SubElement(spell_element, "range")
        range_element.text = self.range
        
        components_element = ET.SubElement(spell_element, "components")
        components_element.text = self.components
        
        duration_element = ET.SubElement(spell_element, "duration")
        duration_element.text = self.duration
        
        classes_element = ET.SubElement(spell_element, "classes")
        classes_element.text = self.classes
        
        for row in self.description.split("\n"):
            text = ET.SubElement(spell_element,"text")
            text.text = row
        if self.roll is not None:
            roll_element = ET.SubElement(spell_element, "roll")
            roll_element.text = self.roll
            
        return spell_element
    
    def __str__(self) -> str:
        str = ""
        
        str += self.name
        
        return str 
        
    