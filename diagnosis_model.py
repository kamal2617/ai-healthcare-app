def get_diagnosis_and_treatment(symptoms):
    symptom_presence = {s: s in symptoms for s in ['fever', 'cough', 'fatigue', 'headache', 'nausea', 'sore-throat', 'shortness-breath']}
    
    if symptom_presence['fever'] and symptom_presence['cough'] and symptom_presence['shortness-breath']:
        diagnosis = "Possible COVID-19"
        treatments = ["Isolate", "Get tested", "Hydrate", "Seek care if symptoms worsen"]
    elif symptom_presence['fever'] and symptom_presence['fatigue']:
        diagnosis = "Influenza (Flu)"
        treatments = ["Rest", "Hydrate", "OTC meds", "Antivirals"]
    elif symptom_presence['headache'] and symptom_presence['nausea']:
        diagnosis = "Migraine"
        treatments = ["Rest in dark room", "Pain relievers", "Hydrate"]
    else:
        diagnosis = "General Illness"
        treatments = ["Monitor symptoms", "Hydrate", "See a doctor"]
    
    return diagnosis, treatments
