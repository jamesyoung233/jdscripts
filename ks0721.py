import lzma, base64
exec(lzma.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)
