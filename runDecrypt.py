def decryptTextData(encrypted, nShift):

  text = ''

  for c in encrypted:
    if ord(c) >= 97 and ord(c) <=122:
      s = chr((ord(c) - nShift - 97) % 26 + 97)
      text = text[0:] + s
    else:
      text = text[0:] + c

  return text

