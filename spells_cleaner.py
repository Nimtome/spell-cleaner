from typing import List
import xml.etree.ElementTree as ET

from Spell import Spell

def parse_xml(xmlfile) -> List[Spell]:
    tree = ET.parse(xmlfile)
    
    root = tree.getroot()
    
    spell_items = {}
    
    for spell in root:
        spell = parse_spell(spell)
        if (not spell.name in spell_items):
            spell_items[spell.name] = spell
            
    return spell_items.values()
        
def parse_spell(spell: ET.Element) -> Spell:
    new_spell = Spell()
    for child in spell:
        match (child.tag):
            case "name":
                new_spell.name = child.text.strip("*").strip()
            case "level":
                new_spell.level = int(child.text)
            case "school":
                new_spell.school = child.text
            case "ritual":
                new_spell.ritual = child.text == "YES"
            case "time":
                new_spell.time = child.text
            case "range":
                new_spell.range = child.text
            case "components":
                new_spell.components = child.text
            case "duration":
                new_spell.duration = child.text
            case "classes":
                if child.text is not None:
                    new_spell.classes = child.text.strip()
            case "text":
                if child.text is not None:
                    new_spell.description += child.text.replace("\n","").replace("\t", "")
                else :
                    new_spell.description += "\n"
            case "roll":
                new_spell.roll = child.text
        
    return new_spell

def spells_to_xml(spell_list: List[Spell]):
    root = ET.Element("compendium")
    for spell in spell_list:
        root.append(spell.to_xml())
    
        
    tree = ET.ElementTree(root)
    
    tree.write("out_spells.xml", "UTF-8", xml_declaration=True)
          
            
def main():
    spells = list(parse_xml('Spells.xml'))
    spells_to_xml(spells)  
    
main()

