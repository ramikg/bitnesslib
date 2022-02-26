import os
import struct
from abc import ABCMeta, abstractmethod

# Compatible with Python 2 & 3
ABC = ABCMeta('ABC', (object,), {'__slots__': ()})


class BitnessLibFormatError(Exception):
    pass


class BitnessLibFileDoesNotExistError(Exception):
    pass


class AbstractFormat(ABC):
    def __init__(self, path):
        if not os.path.exists(path):
            raise BitnessLibFileDoesNotExistError('File {} doesn\'t exist'.format(path))

        self._path = path

    @abstractmethod
    def get_bitness(self):
        pass

    @staticmethod
    def file_read_uint8(file):
        return ord(file.read(1))

    @staticmethod
    def file_read_little_endian_uint16(file):
        bytes = file.read(2)
        return struct.unpack('<H', bytes)[0]

    @staticmethod
    def file_read_little_endian_uint32(file):
        bytes = file.read(4)
        return struct.unpack('<L', bytes)[0]

    @staticmethod
    def file_read_big_endian_uint16(file):
        bytes = file.read(2)
        return struct.unpack('>H', bytes)[0]
