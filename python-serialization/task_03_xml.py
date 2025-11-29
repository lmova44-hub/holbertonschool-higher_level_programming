#!/usr/bin/env python3
"""Serialization and deserialization of Python dictionary to/from XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save it to a file.

    Args:
        dictionary (dict): Python dictionary to serialize.
        filename (str): Output XML file path.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML file to a Python dictionary.

    Args:
        filename (str): XML file path.

    Returns:
        dict: Python dictionary reconstructed from XML.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text

    return result
