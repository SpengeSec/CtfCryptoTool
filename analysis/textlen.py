

#write ciphertext length and ciphertext length without whitespaces to the result dictionary

name = "Ciphertext Length"

fail="[\033[91m+\033[0m]"
success="[\033[92m+\033[0m]"

success = f"{success} Found cipher length"
fail = f"{fail}"


def analyse(result, text, **kwargs):
    result["cipherLength"]=len(text)
    result["cipherLengthNOWS"]=len(text.replace(' ',''))
    return True