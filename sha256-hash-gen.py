#!/bin/python3

import hashlib

#Define hashing function, declare encoding type.
def sha256HashingFunction(string, encoding='utf-8'):
    sha256_hasher = hashlib.sha256()
    sha256_hasher.update(string.encode(encoding))
    return sha256_hasher.hexdigest()

#Opens wordlist source and destination hash-lookup file to write. Must specify appropriate file path.
with open("/usr/share/wordlists/rockyou.txt", 'r') as ry, open("/usr/share/wordlists/rockyou-sha256-hash.txt", 'w') as nry:
	for line in ry:
		nry.write(sha256HashingFunction(line) + ' - ' + line)
	ry.close()
	nry.close()