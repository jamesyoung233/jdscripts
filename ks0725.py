import lzma, base64
exec(lzma.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)
