import os

from bitnesslib.file_formats import abstract_format

MINIDUMP_SIZE_OF_MAGIC = 4
MINIDUMP_MAGIC = b'MDMP'
MINIDUMP_OFFSET_OF_NUMBER_OF_STREAMS = 0x8
MINIDUMP_MAX_NUMBER_OF_STREAMS = 0xFF  # Avoid stalling on malformed files.
MINIDUMP_SIZE_OF_LOCATION_DESCRIPTOR = 8
MINIDUMP_SIZE_OF_STREAM_SIZE_FIELD = 4
MINIDUMP_SYSTEM_INFO_STREAM_TYPE = 7
MINIDUMP_64_BIT_PROCESSOR_ARCHITECTURES = [
    6,  # IA64
    9,  # AMD64
    12  # ARM64
]


class MinidumpFormat(abstract_format.AbstractFormat):
    def get_bitness(self):
        with open(self._path, 'rb') as file:
            magic = file.read(MINIDUMP_SIZE_OF_MAGIC)
            assert magic == MINIDUMP_MAGIC

            try:
                file.seek(MINIDUMP_OFFSET_OF_NUMBER_OF_STREAMS)
                number_of_streams = self.file_read_little_endian_uint32(file)

                offset_of_stream_directory = self.file_read_little_endian_uint32(file)
                file.seek(offset_of_stream_directory)

                for stream_number in range(min(number_of_streams, MINIDUMP_MAX_NUMBER_OF_STREAMS)):
                    stream_type = self.file_read_little_endian_uint32(file)
                    if stream_type != MINIDUMP_SYSTEM_INFO_STREAM_TYPE:
                        file.seek(MINIDUMP_SIZE_OF_LOCATION_DESCRIPTOR, os.SEEK_CUR)
                    else:
                        file.seek(MINIDUMP_SIZE_OF_STREAM_SIZE_FIELD, os.SEEK_CUR)
                        offset_of_system_info = self.file_read_little_endian_uint32(file)

                        file.seek(offset_of_system_info)
                        processor_architecture = self.file_read_little_endian_uint16(file)
                        return self._get_bitness_by_processor_architecture(processor_architecture)

            except Exception:
                pass

            raise abstract_format.BitnessLibFormatError()

    @staticmethod
    def _get_bitness_by_processor_architecture(processor_architecture):
        if processor_architecture in MINIDUMP_64_BIT_PROCESSOR_ARCHITECTURES:
            return 64
        else:
            return 32
