pip install gingerit
# This code will check your English sentence for grammar mistakes
from gingerit.gingerit import GingerIt
text = input("Enter a sentence >>: ")
corrected_text = GingerIt().parse(text)
print(corrected_text['result'])
