from .file_formats.magic_map import magic_map

FORMATS_FOLDER_NAME = 'file_formats'
ABSTRACT_FORMAT_MODULE_NAME = 'abstract_format.py'
NUMBER_OF_MAGIC_BYTES_TO_READ = 4


class BitnessLibUnknownFormatError(Exception):
    pass


def _get_dict_value_based_on_longer_key(d, longer_key):
    keys_with_prefix = [key for key in d.keys() if longer_key.startswith(key)]
    # Assumption: No key is a prefix of another key
    assert len(keys_with_prefix) <= 1

    if not keys_with_prefix:
        raise BitnessLibUnknownFormatError()

    key_with_prefix = keys_with_prefix[0]
    return d[key_with_prefix]


def get_bitness(path):
    with open(path, 'rb') as file:
        magic_bytes = file.read(NUMBER_OF_MAGIC_BYTES_TO_READ)

    file_format_parser_class = _get_dict_value_based_on_longer_key(magic_map, magic_bytes)
    file_format_parser = file_format_parser_class(path)

    return file_format_parser.get_bitness()
