from setuptools import setup, find_packages
import os

github_run_number = os.getenv("GITHUB_RUN_NUMBER")
current_version = "1.0.{github_run_number}".format(github_run_number=github_run_number) if github_run_number else "1.0.0"

setup(
    name="image-resize-python-script",
    version=current_version,
    packages=find_packages(),

    # Metadata
    author="Mayjo Antony",
    author_email="mayjoantony123@gmail.com",
    description="A small python script to resize images in a folder",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mayjoantony/image-resize-python-script",
    download_url="https://github.com/mayjoantony/image-resize-python-script/archive/refs/tags/v{}.zip".format(current_version),
    keywords=["image", "resize", "python", "script", "png", "opencv", "numpy"],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],

    install_requires=[
        "numpy",
        "opencv-python",
    ],

)