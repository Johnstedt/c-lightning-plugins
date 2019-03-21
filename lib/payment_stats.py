from amount import Amount


# Incomplete payments
def incomplete_payments(rpc):
    return [p['msatoshi_sent']
            for p in rpc.listpayments()['payments']
            if p['status'] != 'complete']


# All complete payments
def complete_payments(rpc):
    return [p['msatoshi_sent']
            for p in rpc.listpayments()['payments']
            if p['status'] == 'complete']


# Total routing fees paid thus far on node
def routing_fees_paid(rpc):
    return Amount(sum((p['msatoshi_sent'] - p['msatoshi']
                       for p in complete_payments(rpc))), 'msat')


# Total in sent payments
def total_sent_payments(rpc):
    return Amount(sum((p['msatoshi_sent']
                       for p in complete_payments(rpc))), 'msat')
