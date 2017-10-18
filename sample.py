import iota  # Original IOTA python library
import iota_fees  # Just import this module and you are ready to set fees on transactions

#
# This sample shows how the iota-fees module allows for setting transaction fees,
# in order to make IOTA a fully accepted crypto currency and to increase acceptance
# of your business towards customers.
#

# Connect to IOTA node
api = iota.Iota('http://localhost:14265/')

# Create sample transfer
transfer = [
    iota.ProposedTransaction(
      address = iota.Address(b'QPLGOG9PMIMUAW9UDMUNZQHPXZPXDNGLBEIHILXHWHIOFHLIHPDDERXAJQKUQDEORMHSUWVZQE9JYSHIWADIIPAOJD'),
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
