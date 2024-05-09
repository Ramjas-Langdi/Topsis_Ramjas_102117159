import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="topsis-Ramjas-102117159",
    version="1.0.2",
    description="It gives the ranking to models as per the TOPSIS score.Please view the instructions so as to run the package smoothly in your terminal.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Ramjas Langdi",
    author_email="rlangdi_be21@thapar.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "topsis=topsis.__main__:main",
        ]
    },
)