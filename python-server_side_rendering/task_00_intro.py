#!/usr/bin/python3
"""
Module: task_00_intro
Contains function generate_invitations
"""


def generate_invitations(template, attendees):
    """Generate invitation files from template and attendees list"""

    # ✅ Check type of template
    if not isinstance(template, str):
        print("Error: template must be a string")
        return

    # ✅ Check type of attendees
    if not isinstance(attendees, list):
        print("Error: attendees must be a list")
        return

    # ✅ Check each element in attendees
    for person in attendees:
        if not isinstance(person, dict):
            print("Error: attendees must be a list of dictionaries")
            return

    # ✅ Empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # ✅ Empty attendees
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # ✅ Process each attendee
    for i, person in enumerate(attendees, start=1):

        # Get values with fallback "N/A"
        name = person.get("name") if person.get("name") else "N/A"
        title = person.get("event_title") if person.get("event_title") else "N/A"
        date = person.get("event_date") if person.get("event_date") else "N/A"
        location = person.get("event_location") if person.get("event_location") else "N/A"

        # Replace placeholders
        output = template
        output = output.replace("{name}", str(name))
        output = output.replace("{event_title}", str(title))
        output = output.replace("{event_date}", str(date))
        output = output.replace("{event_location}", str(location))

        # Write to file
        filename = f"output_{i}.txt"
        try:
            with open(filename, "w") as f:
                f.write(output)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
