def extract_fields(text):
    extracted_data = {
        "Type": "",
        "Card Number": "",
        "Date / Time": "",
        "Reference": "",
        "Amount":""
        
    }
    
    for line in text.split('\n'):
        if "TYPE" in line:
            extracted_data["Type"] = line.split()[-1]
        elif "CARD NUMBER" in line:
            extracted_data["Card Number"] = line.split()[-1]
        elif "DATE / TIME" in line:
            extracted_data["DATE / TIME"] = line.split()[-1]
        elif "REFERENCE" in line:
            extracted_data["Reference"] = line.split()[-1]
        elif "AMOUNT" in line:
            extracted_data["Amount"] = line.split()[-1]
    
    return extracted_data
