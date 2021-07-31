from bitnesslib.file_formats import abstract_format

MACHO_SIZE_OF_MAGIC = 4
MH_MAGIC = b'\xFE\xED\xFA\xCE'
MH_CIGAM = MH_MAGIC[::-1]
MH_MAGIC_64 = b'\xFE\xED\xFA\xCF'
MH_CIGAM_64 = MH_MAGIC_64[::-1]


class MachoFormat(abstract_format.AbstractFormat):
    def get_bitness(self):
        with open(self._path, 'rb') as file:
            magic = file.read(MACHO_SIZE_OF_MAGIC)

        if magic in (MH_MAGIC, MH_CIGAM):
            return 32
        if magic in (MH_MAGIC_64, MH_CIGAM_64):
            return 64

        raise abstract_format.BitnessLibFormatError()


FileFormatParser = MachoFormat
