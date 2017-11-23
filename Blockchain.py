# from https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
# 23 Nov 17

class Blockchain (object):
	"""docstring for Blockchain """
	def __init__(self):
		self.chain = []
		self.current_transactions = []

	def new_block(self):
		# creates new block and adds to chain
		pass

	def new_transaction(self):
		 # adds new transaction to the transaction llist
		 pass

	@staticmethod
	def hah(block):
		# hashes a block
		pass

	@property
	def last_block(self):
		# returns the last Block in the chain
		pass
	