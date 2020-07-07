text_data = [
'Test!!!! hello. esim. test2...',
'100% ola!! #HashTag',
'testText???!!?'
]
import sys 
import unicodedata
tbl=dict.fromkeys(i for i in range(sys.maxunicode)
                 if unicodedata.category(chr(i)).startswith('P'))
def remove_punct(text):
    return text.translate(tbl)
for i in range(3):
    text_data[i]=remove_punct(text_data[i])

print(text_data)
