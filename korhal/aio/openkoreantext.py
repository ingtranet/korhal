from korhal.util.client import tokenize_rpc


def tokenize(text):
    return tokenize_rpc(text, 'okt', True)
    
def split_sentence(text):
    raise NotImplementedError()
