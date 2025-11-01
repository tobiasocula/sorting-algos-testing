from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "algorithms",
        ["algorithms.cpp"],
        include_dirs=[pybind11.get_include()],
        language='c++'
    ),
]

setup(
    name="algorithms",
    ext_modules=ext_modules,
)
