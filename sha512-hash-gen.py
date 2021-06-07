#!/bin/python3

import hashlib

#Define hashing function, declare encoding type.
def sha512HashingFunction(string, encoding='utf-8'):
    sha512_hasher = hashlib.sha512()
    sha512_hasher.update(string.encode(encoding))
    return sha512_hasher.hexdigest()

#Opens wordlist source and destination hash-lookup file to write. Must specify appropriate file path.
with open("/usr/share/wordlists/rockyou.txt", 'r') as ry, open("/usr/share/wordlists/rockyou-sha512-hash.txt", 'w') as nry:
	for line in ry:
		nry.write(sha512HashingFunction(line) + ' - ' + line)
	ry.close()
	nry.close()