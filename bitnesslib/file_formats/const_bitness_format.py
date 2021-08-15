
from bitnesslib.file_formats import abstract_format


def get_const_bitness_format(bitness):
    class ConstBitnessFormat(abstract_format.AbstractFormat):
        def get_bitness(self):
            return bitness

    return ConstBitnessFormat


Const16BitFormat = get_const_bitness_format(16)
Const32BitFormat = get_const_bitness_format(32)
Const64BitFormat = get_const_bitness_format(64)
