# from https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
# 23 Nov 17

import hashlib
import json
from time import time


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
