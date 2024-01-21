from setuptools import setup, find_packages

setup(
    name="image-resize-python-script",
    version="1.0.5",
    packages=find_packages(),

    # Metadata
    author="Mayjo Antony",
    author_email="mayjoantony123@gmail.com",
    description="A small python script to resize images in a folder",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mayjoantony/image-resize-python-script",
    download_url="https://github.com/mayjoantony/image-resize-python-script/archive/refs/tags/v1.0.5.zip",
    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
    ],

    install_requires=[
        "numpy",
        "opencv-python",
    ],
    
)