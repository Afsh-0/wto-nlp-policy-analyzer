import re #Used to remove unwanted characters

def clean_text(text): #Takes raw PDF text and Returns cleaned version
    # remove weird characters and artifacts
    text = re.sub(r'\n+', ' ', text) #replace multiple line breaks with space and makes text continuous
    text = re.sub(r'[^a-zA-Z0-9.,%()\- ]', ' ', text) #Remove unwanted characters

    # remove extra spaces
    text = ' '.join(text.split())

    return text