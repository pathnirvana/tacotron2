# coding=utf-8
from unidecode import unidecode

print(unidecode('කෝකටත් මං වෙනදා තරම් කාලෙ ගන්නැතිව ඇඳ ගත්තා'))

_pad        = '_'
_punctuation = '!\'(),.:;? '
_special = '-'
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzජනක'

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
#_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Export all symbols:
symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters) 

print(symbols)
_symbol_to_id = {s: i for i, s in enumerate(symbols)}
print(_symbol_to_id)