from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="YoutubeVideoDownloader",
    version="0.1",
    author="Orosunlegan O. Stephen",
    author_email="oluwabusayomidafrabzinator@gmail.com",
    description="A simple YouTube video downloader application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/YoutubeVideoDownloader",
    packages=find_packages(),
    install_requires=[
        "pytube",
        "tkinter"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
