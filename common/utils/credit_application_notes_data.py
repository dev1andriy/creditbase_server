from common.models.other.note import *

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


def generate_credit_applications_notes_data(credit_application_id, base_party_id):
    config = {}

    for tab in notes_tabs:
        config[tab['name']] = {
            "1": Note.objects.get(BasePartyId_id=base_party_id, Tab=tab['name'], NoteLevel=1, NoteKey1=base_party_id).Note if Note.objects.filter(BasePartyId_id=base_party_id, Tab=tab['name'], NoteLevel=1, NoteKey1=base_party_id).exists() else "",
            "2": Note.objects.get(BasePartyId_id=base_party_id, Tab=tab['name'], NoteLevel=2, NoteKey1=credit_application_id).Note if Note.objects.filter(BasePartyId_id=base_party_id, Tab=tab['name'], NoteLevel=2, NoteKey1=credit_application_id).exists() else ""
        }

    return config

