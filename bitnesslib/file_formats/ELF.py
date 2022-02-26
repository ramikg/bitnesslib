from bitnesslib.file_formats import abstract_format

ELF_SIZE_OF_MAGIC = 4
ELF_MAGIC = b'\x7FELF'
ELFCLASS32 = 1
ELFCLASS64 = 2
ELF_LITTLE_ENDIAN = 1
ELF_BIG_ENDIAN = 2
ELF_OFFSET_OF_MACHINE = 0x12
ELF_SIZE_OF_MACHINE = 2
ELF_64_BIT_ARCHITECTURES_WITH_ILP32 = [
    0x3E,  # AMD x86-64 supports x32
    0xB7  # AArch64 supports AArch64-ILP32
]


class ElfFormat(abstract_format.AbstractFormat):
    def get_bitness(self):
        with open(self._path, 'rb') as file:
            magic = file.read(ELF_SIZE_OF_MAGIC)
            assert magic == ELF_MAGIC

            elf_class = self.file_read_uint8(file)
            elf_endianness = self.file_read_uint8(file)

            file.seek(ELF_OFFSET_OF_MACHINE)
            if elf_endianness == ELF_LITTLE_ENDIAN:
                elf_machine = self.file_read_little_endian_uint16(file)
            elif elf_endianness == ELF_BIG_ENDIAN:
                elf_machine = self.file_read_big_endian_uint16(file)
            else:
                raise abstract_format.BitnessLibFormatError()

        if elf_class == ELFCLASS64 or elf_machine in ELF_64_BIT_ARCHITECTURES_WITH_ILP32:
            return 64

        elif elf_class == ELFCLASS32:
            return 32

        raise abstract_format.BitnessLibFormatError()
