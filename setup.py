import io
from setuptools import setup, find_packages

VERSION = "0.1.0"
PACKAGE_NAME = "hp3par-exporter"
SOURCE_DIR_NAME = "src"


def readme():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        return f.read()


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description="Prometheus exporter for HP 3PAR metrics",
    author="Nicolas Marcq",
    long_description=readme(),
    url="https://github.com/sispheor/hp3par-exporter",
    package_dir={'': SOURCE_DIR_NAME},
    packages=find_packages(SOURCE_DIR_NAME, exclude=('*.tests',)),
    include_package_data=True,
    zip_safe=False,
    package_data={},
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        "cffi",
        "prometheus-client",
        "pyyaml",
        "python-3parclient"
    ],
    entry_points={
        'console_scripts': [
            'hp3par-exporter = hp3par_exporter.main:main',
        ],
    }
)
