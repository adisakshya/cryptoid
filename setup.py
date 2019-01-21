import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cryptoid",
    version="1.0.0",
    author="Adisakshya Chauhan",
    author_email="adisakshya98@gmail.com",
    description="A python cryptographer that facilitates encryption and decryption that is used to establish secure communication in presence of third parties.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adisakshya/cryptoid",
    packages=setuptools.find_packages(),
    scripts=['bin/cryptoid.py','bin/cryptoid.py','bin/lists.py','bin/helper_cryptoid.py','bin/asymmetric_ciphers.py','bin/helper_asymmetric_ciphers.py','bin/symmetric_ciphers.py','bin/helper_symmetric_ciphers.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
