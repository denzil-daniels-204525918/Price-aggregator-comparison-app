from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="price-aggregator",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A price aggregator and comparison system for grocery stores",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[
        "fastapi>=0.104.0",
        "pydantic>=2.0.0",
        "redis>=5.0.0",
        "uvicorn>=0.24.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },
)