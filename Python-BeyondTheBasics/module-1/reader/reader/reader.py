import os

from reader2.reader.compressed import bzipped
from reader2.reader.compressed import gzipped

extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener,
}

class Reader:
    def __init__(self, filename):
        # self.filename = filename
        extension = os.path.splitext(filename)[1]
        opener = extension_map.get(extension, open)
        self.f = opener(filename, 'rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()

# import reader.reader
# reader.reader.__file__
# r = reader.reader.Reader.('reader.reader.py')
# r.read()
# r.close()

# import reader
# reader.reader.__file__
# r = reader.Reader.('reader.__init__.py')
# r.read()
# r.close()

# import reader
# import reader.compressed
# import reader.compressed.gzipped
# import reader.compressed.bzipped

# python -m reader.compressed.bzipped test.bz2 data compressed with bz2
# python -m reader.compressed.gzipped test.gz data compressed with gzip

# import reader
# r = reader.Reader('test.bz2')
# r.read()
# r.close()
# r = reader.Reader('test.gz')
# r.read()
# r.close()
# r = reader.Reader('reader/__init__.py')
# r.read()
# r.close()


