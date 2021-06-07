#!/bin/python3

import hashlib

#Define hashing function, declare encoding type.
def md5HashingFunction(string, encoding='utf-8'):
    md5_hasher = hashlib.md5()
    md5_hasher.update(string.encode(encoding))
    return md5_hasher.hexdigest()

#Opens wordlist source and destination hash-lookup file to write. Must specify appropriate file path.
with open("/usr/share/wordlists/rockyou.txt", 'r') as ry, open("/usr/share/wordlists/rockyou-md5-hash.txt", 'w') as nry:
	for line in ry:
		nry.write(md5HashingFunction(line) + ' - ' + line)
	ry.close()
	nry.close()