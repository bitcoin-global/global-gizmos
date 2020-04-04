import hashlib

""" Consts """
class consts:
	CHAIN = {
		"main": {
			"size": 100,
			"prefix": "26", # base58 prefix - 38
			"secret_bytes": "80",
			"file": "secret.mainnet.csv"
		},
		"test": {
			"size": 50, 
			"prefix": "6f", # base58 prefix - 111
			"secret_bytes": "ef", 
			"file": "secret.testnet.csv"
		},
		"reg": {
			"size": 5, 
			"prefix": "6f", # base58 prefix - 111
			"secret_bytes": "ef", 
			"file": "secret.regtest.csv"
		}
	}
	CPPFILE = "param_consts.cpp"
	VECTOR_TEMPLATE = """// Chain: %s
vPreminePubkeys = {
%s
};
"""

""" Utils for list operations """
def reshape(lst, n):
	if len(lst) < n:
		return [lst]
	return [lst[i * n : (i + 1) * n] for i in range(len(lst) // n)]

""" Utils for WIF creation """
# base58 alphabet
alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def sha256(arg) :
	''' Return a sha256 hash of a hex string '''
	byte_array = bytearray.fromhex(arg)
	m = hashlib.sha256()
	m.update(byte_array)
	return m.hexdigest()

def b58encode(hex_string) :
	''' Return a base58 encoded string from hex string '''
	num = int(hex_string, 16)
	encode = ""
	base_count = len(alphabet)
	while (num > 0) :
		num, res = divmod(num,base_count)
		encode = alphabet[res] + encode
	return encode

def b58decode(v):
	''' Decode a Base58 encoded string as an integer and return a hex string '''
	if not isinstance(v, str):
		v = v.decode('ascii')
	decimal = 0
	for char in v:
		decimal = decimal * 58 + alphabet.index(char)
	return hex(decimal)[2:] # (remove "0x" prefix)

def privToWif(priv, secret_bytes) :
	''' Produce a WIF from a private key in the form of an hex string '''
	priv_add_secret_bit = secret_bytes + priv.lower()

	first_sha256 = sha256(priv_add_secret_bit)
	second_sha256 = sha256(first_sha256)
	first_4_bytes = second_sha256[0:8]

	resulting_hex = priv_add_secret_bit + first_4_bytes
	result_wif = b58encode(resulting_hex)

	return result_wif

def wifToPriv(wif, secret_bytes) :
	''' Produce the private ECDSA key in the form of a hex string from a WIF string '''
	if not wifChecksum(wif, secret_bytes) : raise Exception('The WIF is not correct (does not pass checksum)')

	byte_str = b58decode(wif)
	byte_str_drop_last_4bytes = byte_str[0:-8]
	byte_str_drop_first_byte = byte_str_drop_last_4bytes[2:]

	return byte_str_drop_first_byte

def wifChecksum(wif, secret_bytes) :
	''' Returns True if the WIF is positive to the checksum, False otherwise '''
	byte_str = b58decode(wif)
	byte_str_drop_last_4bytes = byte_str[0:-8]

	sha_256_1 = sha256(byte_str_drop_last_4bytes)
	sha_256_2 = sha256(sha_256_1)

	first_4_bytes = sha_256_2[0:8]
	last_4_bytes_WIF = byte_str[-8:]

	bytes_check = False
	if first_4_bytes == last_4_bytes_WIF: 
		bytes_check = True

	check_sum = False
	if bytes_check and byte_str[0:2] == secret_bytes: 
		check_sum = True

	return check_sum

""" Legacy Address handler """
import base58

def hash160(hex_str):
    sha = hashlib.sha256()
    rip = hashlib.new('ripemd160')
    sha.update(hex_str)
    rip.update( sha.digest() )
    return rip.hexdigest()  # .hexdigest() is hex ASCII

def btg_address(pubkey, prefix, compress_pubkey=True):
	if (compress_pubkey):
		if (ord(bytearray.fromhex(pubkey[-2:])) % 2 == 0):
			pubkey_compressed = '02'
		else:
			pubkey_compressed = '03'
		pubkey_compressed += pubkey[2:66]
		hex_str = bytearray.fromhex(pubkey_compressed)
	else:
		hex_str = bytearray.fromhex(pubkey)

	# Obtain key
	key_hash = prefix + hash160(hex_str)

	# Obtain signature
	sha = hashlib.sha256()
	sha.update( bytearray.fromhex(key_hash) )
	checksum = sha.digest()
	sha = hashlib.sha256()
	sha.update(checksum)
	checksum = sha.hexdigest()[0:8]

	return (base58.b58encode( bytes(bytearray.fromhex(key_hash + checksum)) )).decode('utf-8')
