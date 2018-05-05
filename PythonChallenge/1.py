import string
cyphertext = dict(zip(string.ascii_lowercase,string.ascii_lowercase[2:]+string.ascii_lowercase[:2]))
codedmessage="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print("".join(cyphertext.get(c,c) for c in codedmessage))
