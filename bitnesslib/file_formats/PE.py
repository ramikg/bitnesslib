from bitnesslib.file_formats import abstract_format

PE_SIZE_OF_MZ_MAGIC = 2
PE_MZ_MAGIC = b'MZ'
PE_MZ_MAGIC_REVERSED = b'ZM'
PE_OFFSET_OF_PE_HEADER = 0x3C
PE_SIZE_OF_PE_HEADER_MAGIC = 4
PE_HEADER_MAGIC = b'PE\0\0'
PE_OFFSET_OF_OPTIONAL_HEADER = 0x18  # Relative to PE header start
IMAGE_NT_OPTIONAL_HDR32_MAGIC = 0x10B
IMAGE_NT_OPTIONAL_HDR64_MAGIC = 0x20B


class PeFormat(abstract_format.AbstractFormat):
    def get_bitness(self):
        with open(self._path, 'rb') as file:
            magic = file.read(PE_SIZE_OF_MZ_MAGIC)

            if magic == PE_MZ_MAGIC_REVERSED:
                return 16

            if magic != PE_MZ_MAGIC:
                raise abstract_format.BitnessLibFormatError()

            try:
                file.seek(PE_OFFSET_OF_PE_HEADER)
                offset_of_pe_header = self.file_read_little_endian_uint32(file)

                file.seek(offset_of_pe_header)
                pe_header_magic = file.read(PE_SIZE_OF_PE_HEADER_MAGIC)
                if pe_header_magic != PE_HEADER_MAGIC:
                    # Not a proper PE, but may still be a valid MZ executable
                    return 16

                file.seek(offset_of_pe_header + PE_OFFSET_OF_OPTIONAL_HEADER)
                optional_header_magic = self.file_read_little_endian_uint16(file)

                if optional_header_magic == IMAGE_NT_OPTIONAL_HDR32_MAGIC:
                    return 32
                if optional_header_magic == IMAGE_NT_OPTIONAL_HDR64_MAGIC:
                    return 64

            except Exception:
                pass

            raise abstract_format.BitnessLibFormatError()


FileFormatParser = PeFormat
