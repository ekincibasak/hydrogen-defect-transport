from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hydrogen-defect-transport",
    version="0.1.0",
    author="Başak Ekinci",
    author_email="baekinci@gmail.com",
    description="Defect-Induced Localization and Transport in 1D Tight-Binding Models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ekincibasak/hydrogen-defect-transport",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "pandas>=1.3.0",
        "scikit-learn>=1.0.0",
        "xgboost>=1.5.0",
        "optuna>=3.0.0",
        "matplotlib>=3.4.0",
        "qiskit>=0.43.0",
        "qiskit-aer>=0.12.0",
        "jax>=0.3.0",
    ],
)
