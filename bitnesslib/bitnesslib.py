import importlib
import os

from bitnesslib.file_formats.abstract_format import BitnessLibFormatError

FORMATS_FOLDER_NAME = 'file_formats'
ABSTRACT_FORMAT_MODULE_NAME = 'abstract_format.py'


class BitnessLibUnknownFormatError(Exception):
    pass


def get_bitness(path):
    formats_folder_path = os.path.join(os.path.dirname(__file__), FORMATS_FOLDER_NAME)
    for module_name in os.listdir(formats_folder_path):
        if (module_name in ('__init__.py', ABSTRACT_FORMAT_MODULE_NAME)
                or not module_name.endswith('.py')):
            continue

        module_name_without_ext = os.path.splitext(module_name)[0]
        file_format_module = importlib.import_module(
            'bitnesslib.{}.{}'.format(FORMATS_FOLDER_NAME, module_name_without_ext))
        file_format_parser = file_format_module.FileFormatParser(path)

        try:
            return file_format_parser.get_bitness()
        except BitnessLibFormatError:
            continue

    raise BitnessLibUnknownFormatError()
