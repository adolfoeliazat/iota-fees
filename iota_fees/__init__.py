import iota

# Adapting original IOTA object to allow fees
class IotaFees(iota.Iota):
    def send_transfer(
        self,
        depth,
        transfers,
        fees,
        inputs                = None,
        change_address        = None,
        min_weight_magnitude  = None,
    ):    
        # Injecting fee into bundle
        transfers.append(
            iota.ProposedTransaction(
              address = iota.Address(b'QPLGOG9PMIMUAW9UDMUNZQHPXZPXDNGLBEIHILXHWHIOFHLIHPDDERXAJQKUQDEORMHSUWVZQE9JYSHIWADIIPAOJD'),
              value = fees,
              tag = iota.Tag(iota.TryteString.from_string('IOTA Fee')),
              message = iota.TryteString.from_string('IOTA Fee'),
            )
        )
        
        # Submitting bundle
        return super(IotaFees, self).send_transfer(        
            depth,
            transfers,
            inputs                = inputs,
            change_address        = change_address,
            min_weight_magnitude  = min_weight_magnitude
        )

# Override original "send_transfer"
iota.Iota = IotaFees

