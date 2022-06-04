import sys

import pytest

import bitnesslib


PE_32_BIT_PATH = 'C:\\Windows\\SysWOW64\\cmd.exe'
PE_64_BIT_PATH = 'C:\\Windows\\System32\\cmd.exe'
ELF_32_BIT_PATH = '/lib32/libc.so.6'
ELF_64_BIT_PATH = '/lib/x86_64-linux-gnu/libc.so.6'


@pytest.mark.skipif(not sys.platform.startswith('win'), reason="Windows test")
def test_pe_32_bit():
    assert bitnesslib.get_bitness(PE_32_BIT_PATH) == 32


@pytest.mark.skipif(not sys.platform.startswith('win'), reason="Windows test")
def test_pe_64_bit():
    assert bitnesslib.get_bitness(PE_64_BIT_PATH) == 64


@pytest.mark.skipif(not sys.platform.startswith('linux'), reason="Linux test")
def test_elf_32_bit():
    assert bitnesslib.get_bitness(ELF_32_BIT_PATH) == 32


@pytest.mark.skipif(not sys.platform.startswith('linux'), reason="Linux test")
def test_elf_64_bit():
    assert bitnesslib.get_bitness(ELF_64_BIT_PATH) == 64
