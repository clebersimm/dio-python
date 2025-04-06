from setuptools import setup, find_packages

setup(
    name="criarpacote",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "criarpacote=criarpacote.__main__:hello_world",
        ],
    },
    description="A simple package that prints Hello, World!",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/your-repo-url",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
