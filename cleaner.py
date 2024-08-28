import re
import unicodedata

def normalize_text(text):
    # Replace curly quotes with straight quotes
    text = re.sub(r'[‘’]', '\'', text)  # Replace left and right single quotes with '
    text = re.sub(r'[“”]', '"', text)   # Replace left and right double quotes with "

    # Replace en dash and em dash with a hyphen or double hyphen
    text = re.sub(r'–', '-', text)  # Replace en dash with hyphen
    text = re.sub(r'—', '--', text) # Replace em dash with double hyphen

    # Replace ellipsis with three dots
    text = re.sub(r'…', '...', text)

    # Replace other non-ASCII punctuation with ASCII equivalents
    text = re.sub(r'«', '<<', text)  # Replace left double angle quote with <<
    text = re.sub(r'»', '>>', text)  # Replace right double angle quote with >>
    text = re.sub(r'§', 'SS', text)  # Replace section sign with SS
    text = re.sub(r'•', '*', text)   # Replace bullet with asterisk
    text = re.sub(r'‽', '?!', text)  # Replace interrobang with ?!
    text = re.sub(r'′', "'", text)   # Replace prime with single quote
    text = re.sub(r'″', '"', text)   # Replace double prime with double quote
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')