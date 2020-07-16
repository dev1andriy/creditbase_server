notes_tabs = [
    {"name": "executive_summary", "title": "Executive Summary"},
    {"name": "application_details", "title": "Application Details"},
    {"name": "repayment_analysis", "title": "Repayment Analysis"},
    {"name": "business_analysis", "title": "Business Analysis"},
    {"name": "note_5", "title": "Note 5"},
    {"name": "note_6", "title": "Note 6"},
    {"name": "note_7", "title": "Note 7"},
    {"name": "note_8", "title": "Note 8"},
]


def generate_credit_applications_notes_config():
    config = []

    for tab in notes_tabs:
        tab_config = {
            "title": tab['title'],
            "name": tab['name'],
        }

        config.append(tab_config)

    return config

