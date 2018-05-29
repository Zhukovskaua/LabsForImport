import string

text = """adofl hitler 
mein kampf 

"""
for i in str(text):
    if i == " " or i not in string.ascii_letters:
        print("    ")
    else:
        textindisc = ":regional_indicator_%s:" %i
        print(''.join(textindisc))