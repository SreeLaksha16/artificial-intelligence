# Remove Punctuation
import string

text = "Hello!!!, Python... is great???"
no_punct = "".join(ch for ch in text if ch not in string.punctuation)

print("Original:", text)
print("Without Punctuation:", no_punct)
