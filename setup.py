from setuptools import find_packages, setup

# some RDKit versions are not recognized by setuptools
# -> check if RDKit is installed by attempting to import it
# -> if RDKit can be imported, do not add it to install_requires
rdkit_installed = False
try:
    import rdkit

    rdkit_installed = True
except ImportError:
    pass

# rdkit 2022.3.3 is the oldest (reasonable) version
rdkit_requirement = ["rdkit>=2022.3.3"] if not rdkit_installed else []

setup(
    name="np-scout",
    version="0.2.0",
    maintainer="Johannes Kirchmair",
    maintainer_email="johannes.kirchmair@univie.ac.at",
    packages=find_packages(),
    url="https://github.com/molinfo-vienna/np-scout",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="BSD 3-Clause License",
    include_package_data=True,
    install_requires=rdkit_requirement
    + [
        "scikit_learn==0.23.2",
        "numpy==1.19.2",
        "scipy==1.5.2",
        "matplotlib>=3",
        "nerdd-module>=0.3.3",
        # install importlib-resources and importlib-metadata for old Python versions
        "importlib-resources>=5; python_version<'3.9'",
        "importlib-metadata>=4.6; python_version<'3.10'",
    ],
    extras_require={
        "dev": [
            "mypy",
            "ruff",
        ],
        "test": [
            "pytest",
            "pytest-watch",
            "pytest-cov",
            "pytest-bdd",
            "hypothesis",
            "hypothesis-rdkit",
        ],
    },
    entry_points={
        "console_scripts": [
            "npscout=np_scout.__main__:main",
        ],
    },
)
