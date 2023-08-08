from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

setup(
    name="minio_act",
    version='{{VERSION_PLACEHOLDER}}',
    author="John Doe",
    author_email="manhtct.dev@gmail.com",
    description="Python package for interact with Minio resource",
    url = "https://github.com/trancongtuanmanh/minio-act",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'minio>=7.1.15'
    ],
    keywords=['pypi', 'python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ],
    python_requires=">=3.7",
)