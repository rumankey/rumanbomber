# Encrypted By PyEncryptor
# A Product Of 
# https://github.com/rumankey

import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))