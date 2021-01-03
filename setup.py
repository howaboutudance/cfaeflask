import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
package_list = setuptools.find_packages()
print(f"found: {package_list}")

setuptools.setup(
    name="cfaeflask",
    version="0.0.1",
    author="Michael Penhallegon",
    author_email="mike@hematite.tech",
    description="a docker webapp demoonstrating",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=package_list,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "flask"
    ]
)