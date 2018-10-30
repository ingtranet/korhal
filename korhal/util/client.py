import grpc
from korhal.util import korhal_pb2
from korhal.util import korhal_pb2_grpc
from concurrent.futures import Future

channel = grpc.insecure_channel('127.0.0.1:12248')
stub = korhal_pb2_grpc.TokenizerStub(channel)


def tokenize_rpc(text, tokenizer, is_async=False):
    request = korhal_pb2.TextRequest(text=text, tokenizer=tokenizer)
    
    if is_async:
        result_future = Future()
        
        def _callback(future):
            try:
                result = future.result()
                result_future.set_result([KorhalToken(token.text, token.pos, token.misc) for token in result.tokens])
            except Exception as e:
                result_future.set_exception(e)
            
        stub.Tokenize.future(request).add_done_callback(_callback)
        
        return result_future
    else:
        return [KorhalToken(token.text, token.pos, token.misc) for token in stub.Tokenize(request).tokens]


class KorhalToken(object):
    __slots__ = "text", "pos", "misc"

    def __init__(self, text, pos, misc):
        self.text = text
        self.pos = pos
        self.misc = misc
    
    def __repr__(self):
        return 'Token(text={},pos={})'.format(self.text, self.pos)

    