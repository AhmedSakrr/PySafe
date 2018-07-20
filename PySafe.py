import io
import zlib
import random
import string
import sys
def o(data,secretkey,mode=0):
	ret = []
	for n in range(len(data)):
		byte = ord(secretkey[n % len(secretkey)])
		random.seed(byte)
		gw = random.randint(0,999999999)
		if mode == 0:
			ret.append((data[n] ^ byte) + gw ) 
		else:
			ret.append(((data[n] - gw) ^ byte))
	return ret


HEADER = """
'''
[PROTECTOR] PySafe
[VERSION] 	0.3
[GITHUB]  	https://github.com/BitTheByte
'''
import sys
import zlib
import random
def {f_name}({d_name},{key_name}):
	{r_name} = []
	for {n_name} in range(len({d_name})):
		{byte_name} = ord({key_name}[{n_name} % len({key_name})])
		random.seed({byte_name})
		{r_name}.append((({d_name}[{n_name}] - random.randint(0,999999999)) ^ {byte_name}))
	return {r_name}
try:
	{key_name} = ""
	if sys.version[0] == '3':
		print('[WARNING] This program is protected!')
		{key_name} = input('[#] Please Enter your key: ')
	else:
		print '[WARNING] This program is protected!'
		{key_name} = raw_input('[#] Please Enter your key: ')	
	{dec_name} = {dec_value}
	exec(zlib.decompress(str(bytearray({f_name}({dec_name},{key_name})))))
except:
	print('[ERROR] Wrong Password!')
"""

if len(sys.argv) < 4:
	print("[Usage] python {} in.py out.py key").format(sys.argv[0])
else:
	try:
		file = io.open(sys.argv[1],'r').read()
		print("[INFO] Compressing data")
		CompressedData = zlib.compress(file,9)
		print "[INFO] Fetching Bytes"
		ZipFileArray   = map(ord,CompressedData)
		print "[INFO] Encrypting Data"
		EncryptedData  = o(ZipFileArray ,str(sys.argv[3]),0) #Mode 0 Encrypt / Mode 1 Decrypt
		print("[INFO] Saveing Data")
		open(sys.argv[2],'w').write(HEADER.format(
			r_name=''.join(random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase   + string.digits) for _ in xrange(random.randint(random.randint(10,50),99))),
			f_name=''.join(random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase   + string.digits) for _ in xrange(random.randint(random.randint(10,50),99))),
			d_name=''.join(random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase   + string.digits) for _ in xrange(random.randint(random.randint(10,50),99))),
			n_name=''.join(random.choice(string.ascii_uppercase) +random.choice(string.ascii_uppercase   + string.digits) for _ in xrange(random.randint(random.randint(10,50),99))),
			key_name=''.join(random.choice(string.ascii_uppercase) +random.choice(string.ascii_uppercase + string.digits) for _ in xrange(random.randint(random.randint(10,50),99))),
			byte_name=''.join(random.choice(string.ascii_uppercase) +random.choice(string.ascii_uppercase+ string.digits) for _ in xrange(random.randint(random.randint(10,50),99))),
			dec_name=''.join(random.choice(string.ascii_uppercase) +random.choice(string.ascii_uppercase + string.digits) for _ in xrange(random.randint(random.randint(10,50),99))),
			dec_value=EncryptedData
		))
	except:
		print("[ERROR] Invaild file name")
