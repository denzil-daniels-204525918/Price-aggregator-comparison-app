from setuptools import setup, find_packages

setup(
    name="price_aggregator",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi",
        "pydantic",
        "httpx"
    ],
    entry_points={
        "console_scripts": [
            "price-aggregator=main.app:main"
        ],
    },
)
