# from https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
# 23 Nov 17

import hashlib
import json

from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask,jasonify, request



class Blockchain (object):

	def __init__(self):
		self.chain = []
		self.current_transactions = []

		# create genesis block
		self.new_block(previous_hash = 1,proof = 100)

	def new_block(self,proof,previous_hash = None):
		"""
		Creates new block and adds to chain

		:param proof: <int> the proof given by Proof of Work algorithm
		:param previous_hash: (Optional) <str> hash of previous block
		:return: <dict> New Block

		"""

		block = {
			'index':len(self.chain) + 1,
			'timestamp':time(),
			'transaction':self.current_transactions,
			'proof':proof,
			'previous_hash':previous_hash or self.hash(self.chain[-1]),
		}
		# Reset current list of transactions
		self.current_transactions = []

		self.chain.append(block)

		return block

	def proof_of_work(self,last_proof):
		"""
		Simple Proof of Work algorithm
		- find 'p' such that hash(pp') contains four leading zeros
		and where p is the previous p'
		- p is the previous proof
		- p' is the new proof

		:param last_proof: <int>
		:return: <int>
		"""

		proof = 0
		while self.valid_proof(last_proof,proof) is False:
			proof += 1

		return proof

	@staticmethod
	def valid_proof(last_proof,proof):
		"""
		Validates the Proof: does hash(last_proof,proof) contain four leading zeros?

		:param last_proof: <int> previous proof
		:param proof: <int> current proof
		:return: <bool> True if correct, False if incorrect
		"""

		guess = f'{last_proof}[proof}'.encode()
		guess_hash = hashlib.sha256(guess).hexdigest()
		return guess_hash[:4] == "0000"

	def new_transaction(self,sender,recipient,amount):
		 """

		 Creates a new transaction to go into 
		 the next mined Block 

		 :param sender: <str> Address of sender
		 :param recipient: <str> Address of recipient
		 :param amount: <int> Amount
		 :return: <int> index of the block that will hold this transaction 
		 
		 """

		 self.current_transactions.append({
		 	'sender':sender,
		 	'recipient':recipient,
		 	'amount':amount,
		 	})

		 return self.last_block['index'] + 1

	@property 
	def last_block(self):
		return self.chain[-1]


	@staticmethod
	def hash(block):
		"""
		Creates a SHA-256 hash of a block

		:param block: <dict> Block
		:return: <str>

		"""
		# Make sure Dictionary is ordered or there will be inconsistent hashes


		block_string = json.dumps(block,sort_keys = True).encode()
		return hashlib.sha256(block_string).hexdigest()


	@property
	def last_block(self):
		# returns the last Block in the chain
		pass

	# instantiate our Node
	app = flask(__name__)

	# Generate a globally unique address for this node
	node_identifier = str(uuid4()).replace('-','')

	# instantiate the Blockchain
	blockchain = Blockchain()

	@app.route('/mine',methods=['GET'])
	def mine():
		#We run the proof of work algorithm to get the next proof
		last_block = blockchain.last_block
		last_proof = last_block['proof']
		proof = blockchain.proof_of_work(last_proof)

		# we must receive a reward for finding a proof
		# the sender is "0" to signify that this node has mined a new coin
		blockchain.new_transaction(
			sender = "0",
			recipient = node_identifier,
			amount = 1,
		)

		# forge the new Block by adding it to the chain
		previous_hash = blockchain.hash(last_block)
		block = blockchain.new_block(proof,previous_hash)

		response = {
			'message':"New Block Forged",
			'index':block['index'],
			'transactions':block['transactions'],
			'proof':block['proof'],
			'previous_hash':block[previous_hash],
		}
		return jasonify(response), 200



	@app.route('/transactions/new',methods=['POST'])
	def new_transaction():
		values = request.get_jason()

		# check that required fields are in the POSTed data
		required = ['sender','recipient','amount']
		if not all(k in values for k in required):
			return 'Missing values', 400

		#create a new Transaction
		index = blockchain.new_transaction(values['sender'],values['recipient']),values['amount'])

		response = {'message': f'Transaction will be added to Blockchain {index}'}
		return jasonify(response), 201


	@app.route('/chain',methods = ['GET'])
	def full_chain():
		response = {
			'chain':blockchain.chain,
			'length':len(blockchain.chain),
		}
		return jsonify(respone),200

	if __name__ == '__main__':
		app.run(host='0.0.0.0',port=5000)


