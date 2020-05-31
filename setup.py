from pathlib import Path
from setuptools import setup

setup(
    name="pydmtx-export-svg",
    description="ExportSVGPlugin is plugin for pydmtx",
    long_description=Path("README.md").read_text(),
    version="0.1.0",
    author="Mariusz Gumienny",
    author_email="mkgumienny@gmail.com",
    license="MIT",
    url="https://github.com/pydmtx/pydmtx-export-svg",
    download_url="https://github.com/pydmtx/pydmtx-export-svg",
    py_modules=["export"],
    zip_safe=False,
    entry_points={
        "pydmtx.plugins.export": [
            "export_svg=export:ExportSVGPlugin",
        ]
    },
    install_requires=[
        "pydmtx2>=0.1.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Environment :: Plugins",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
    ],
    keywords="pydmtx plugin",
)