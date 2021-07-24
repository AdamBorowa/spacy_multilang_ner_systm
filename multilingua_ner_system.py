import spacy

def multilingua_ner_system(string_text, language_code):
    
    nlp = spacy.load(f"{language_code}_core_web_sm")
    doc = nlp(string_text)
    
    ner_list = []
    for ent in doc.ents:
        
        ner_dict = {'text': ent.text, 'type': ent.label_, 'start_pos': ent.start_char, 'end_pos': ent.end_char}
        
        ner_list.extend([ner_dict])
        
    return ner_list
