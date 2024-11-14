import hashlib

class Block:
    def __init__(self, index, previous_hash, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.hash = hash

    def calculate_hash(index, previous_hash, data):
        value = str(index) + str(previous_hash) + str(data)
        return hashlib.sha256(value.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(data="Genesis Block", previous_hash='0')

    def create_block(self, data, previous_hash=None):
        index = len(self.chain) + 1
        if previous_hash is None:
            previous_hash = self.chain[-1].hash if self.chain else '0'
        hash = Block.calculate_hash(index, previous_hash, data)
        new_block = Block(index, previous_hash, data, hash)
        self.chain.append(new_block)
        return new_block

    def get_chain(self):
        return self.chain

    def __str__(self):
        return "\n".join([
            f"Block {block.index}: [Hash: {block.hash}, Previous Hash: {block.previous_hash}, Data: {block.data}]"
            for block in self.chain
        ])

blockchain = Blockchain()
blockchain.create_block(data="Первый блок")
blockchain.create_block(data="Второй блок")
blockchain.create_block(data="Третий блок")

print(blockchain)
