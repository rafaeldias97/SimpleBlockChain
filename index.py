from hashlib import sha256
import json
import time

chain = [
	{
		"remetente": "Rafael Dias",
       		"destinatario": "Teste",
       		"mensagem": "600 Reais"
	},
	{
		"remetente": "TESTE",
	       	"destinatario": "Fulano de Tal",
       		"mensagem": "700 Reais"
	}
]

block_chain = []


def get_time():
	return time.time()

def isValidHashDifficulty(hash, difficulty):
	count = 0
	for i in hash:
		count += 1
		if(i <> '0'):
			break
	return count > difficulty

def generate_hash(block):
	nonce = 0
	block["nonce"] = nonce
	hash = sha256(json.dumps(block)).hexdigest()
	while(not isValidHashDifficulty(hash, 4)):
		nonce = nonce + 1
		block["nonce"] = nonce
		hash = sha256(json.dumps(block)).hexdigest()
	return hash


def add_block(block):
	if(len(block_chain) == 0):
		block["timestamp"] = get_time()
		block["hash"] = generate_hash(block)
	else:
		block["timestamp"] = get_time()
		last_block = block_chain[-1]
		block["last_hash"] = last_block["hash"]
		block["hash"] = generate_hash(block)
	block_chain.append(block)

for c in chain:
	add_block(c)

print(block_chain)
