
# IOTA Fees (Extension Module)
This extension library for IOTA allows for setting transaction fees, in order to make IOTA 
a fully acceptable crypto currency and to increase acceptance of your business towards customers.

Fees are sent to me and I might take care of wasting some electricity to back the network, in exchange.

## Usage
All you need to do to enable this extension is to import it in your project.

        import iota_fees

After importing, the functionality of the default IOTA library will be extended and accept a "fee" parameter as an
input for sending transactions. **Sending little fees might influence your karma, while increasing will make your 
wallet you quick(ly poor).**

```
    # Connect to IOTA node
    api = iota.Iota('http://localhost:14265/')
    
    # Create sample transfer
    transfer = [
        iota.ProposedTransaction(
          address = iota.Address(
              b'QPLGOG9PMIMUAW9UDMUNZQHPXZPXDNGLBEIHILXHWHIOF
              b'HLIHPDDERXAJQKUQDEORMHSUWVZQE9JYSHIWADIIPAOJD'
          ),
          value = 100,
          tag = iota.Tag(b'EXAMPLE'),
          message = iota.TryteString.from_string('Hello!'),
        ),
    ]
    
    # Send transfer
    api.send_transfer(
        depth = 100,
        transfers = transfer,
        fees  = 1000000  # The fee to send along with the transfer can be set
    )
```

See sample.py for a working sample.
  
## Installation
1) Install Python3
2) Install required Python 3 modules
    > pip3 install pyota
    
    > pip3 install pyopenssl
    
## Prerequisites (coming with the installation steps above)
- Python3
- PyOpenSSL
- Pyota + dependencies

