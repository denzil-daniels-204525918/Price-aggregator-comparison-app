from setuptools import setup, find_packages

setup(
    name="price_aggregator",
    version="0.1",
    package_dir={"": "src"},  # Tell setuptools to look in src/
    packages=find_packages(where="src"),  # Find all packages in src/
    install_requires=[
        "fastapi",
        "pydantic",
        "redis",
        "pytest",
    ],
    python_requires=">=3.9",
)