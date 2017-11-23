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

	def new_transaction(self,sender,recipient,amount):
		 # adds new transaction to the transaction 
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


	@staticmethod
	def hah(block):
		# hashes a block
		pass

	@property
	def last_block(self):
		# returns the last Block in the chain
		pass
