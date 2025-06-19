from setuptools import setup
from setuptools_rust import RustExtension

setup(
    name="quorum_core",
    version="0.1.0",
    rust_extensions=[RustExtension("quorum_core", debug=False)],
    zip_safe=False,
)
