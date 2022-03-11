"""
Maps a magic to its corresponding format class
"""

from bitnesslib.file_formats import (
    ELF, PE, Minidump
)
from bitnesslib.file_formats.const_bitness_format import (
    Const16BitFormat, Const32BitFormat, Const64BitFormat
)

IDB_EXTENSION_MAGIC = b'IDA1'
I64_EXTENSION_MAGIC = b'IDA2'
PE_MZ_MAGIC_REVERSED = PE.PE_MZ_MAGIC[::-1]
MACHO_MH_MAGIC = b'\xFE\xED\xFA\xCE'
MACHO_MH_CIGAM = MACHO_MH_MAGIC[::-1]
MACHO_MH_MAGIC_64 = b'\xFE\xED\xFA\xCF'
MACHO_MH_CIGAM_64 = MACHO_MH_MAGIC_64[::-1]


magic_map = {
    IDB_EXTENSION_MAGIC: Const32BitFormat,
    I64_EXTENSION_MAGIC: Const64BitFormat,
    ELF.ELF_MAGIC: ELF.ElfFormat,
    PE_MZ_MAGIC_REVERSED: Const16BitFormat,
    PE.PE_MZ_MAGIC: PE.PeFormat,
    MACHO_MH_MAGIC: Const32BitFormat,
    MACHO_MH_CIGAM: Const32BitFormat,
    MACHO_MH_MAGIC_64: Const64BitFormat,
    MACHO_MH_CIGAM_64: Const64BitFormat,
    Minidump.MINIDUMP_MAGIC: Minidump.MinidumpFormat
}
