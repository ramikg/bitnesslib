from bitnesslib.file_formats import abstract_format

ELF_SIZE_OF_MAGIC = 4
ELF_MAGIC = b'\x7FELF'
ELFCLASS32 = 1
ELFCLASS64 = 2


class ElfFormat(abstract_format.AbstractFormat):
    def get_bitness(self):
        with open(self._path, 'rb') as file:
            magic = file.read(ELF_SIZE_OF_MAGIC)

            if magic != ELF_MAGIC:
                raise abstract_format.BitnessLibFormatError()

            elf_class = self.file_read_uint8(file)

        if elf_class == ELFCLASS32:
            return 32
        if elf_class == ELFCLASS64:
            return 64

        raise abstract_format.BitnessLibFormatError()


FileFormatParser = ElfFormat
