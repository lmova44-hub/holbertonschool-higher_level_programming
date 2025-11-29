#!/usr/bin/env python3
"""Convert CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON and save it to 'data.json'.

    Args:
        csv_filename (str): The CSV file path.

    Returns:
        bool: True if conversion succeeded, False otherwise.
    """
    try:
        data_list = []

        # Read CSV file
        with open(csv_filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append(row)

        # Write JSON file
        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data_list, jsonfile, indent=4)

        return True

    except Exception:
        return False
