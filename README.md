# bitnesslib

A Python library with one simple purpose: given a binary, determine its bitness.  

## Installation

`pip install bitnesslib`

## Usage example

```python
>>> import bitnesslib
>>> bitnesslib.get_bitness('C:/Windows/System32/calc.exe')
64
>>> bitnesslib.get_bitness('C:/Windows/SysWOW64/calc.exe')
32
```

## Supported file formats

- MZ & PE
- ELF
- Mach-O
- IDA databases (_.idb_ & _.i64_)
- Minidump
