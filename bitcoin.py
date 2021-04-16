#bitcoin mining algorithm
from hashlib import sha256
MAX_NONCE = 1000000
def  SHA256(text):

    return print(sha256(text.encode("ascii")).hexdigest())

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
            return new_hash
    raise BaseException(f"Couldn't find correct after tring {MAX_NONCE} times")
    

if __name__=='__main__':
    transactions='''
    Dhaval->Bhavin->20,
    Mando->Cara->45
     '''
    difficulty = 4
    import time
    start = time.time()
    print("start mining")
    new_hash = mine(5,transactions, 'hash', difficulty)
    total_time = str((time.time() - start))
    print(f"end mining. Mining took: {total_time} seconds ")

    print(new_hash)