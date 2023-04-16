HASH_MODES = ['header', 'nonce']
STREAM_MODES = ["MINT", "VALIDATE"]

BEACON_ADDRESS = ('localhost', 80085)

BEACON_SIGNALS = ["MINT", "VALIDATE", "CONNECT"]
RELAY_SIGNALS =  ["REGISTER", "ADD", "APPROVE", "DENY"]


'''
SIGNALS 

    FROM BEACON
        -> MINT         Start Minting a new Block
        -> VALIDATE     Validate a Minted Block
        -> CONNECT      Notify Relays of new Relay
    
    
    FROM RELAY
        -> REGISTER     Join the network
        -> ADD          Return new Block to Beacon
        -> APPROVE      Approve a Block
        -> DENY         Deny a Block        

'''