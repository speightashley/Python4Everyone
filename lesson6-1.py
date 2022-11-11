text = "X-DSPAM-Confidence:    0.8475"

slicedpos = text.find(' ')

slicedstring = text[slicedpos:]

clean = slicedstring.strip()

finished = float(clean)

print(finished)
