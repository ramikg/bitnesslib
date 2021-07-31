from bitnesslib.file_formats import abstract_format

IDB_SIZE_OF_MAGIC = 4
IDB_IDB_EXTENSION_MAGIC = b'IDA1'
IDB_I64_EXTENSION_MAGIC = b'IDA2'


class IdbFormat(abstract_format.AbstractFormat):
    def get_bitness(self):
        with open(self._path, 'rb') as file:
            magic = file.read(IDB_SIZE_OF_MAGIC)

        if magic == IDB_IDB_EXTENSION_MAGIC:
            return 32
        if magic == IDB_I64_EXTENSION_MAGIC:
            return 64

        raise abstract_format.BitnessLibFormatError()


FileFormatParser = IdbFormat
