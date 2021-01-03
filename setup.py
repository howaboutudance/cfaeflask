# Copyright 2020-2021 Michael Penhallegon 
# 
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
# 
#        http://www.apache.org/licenses/LICENSE-2.0

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
    include_package_data=True,
    zip_safe=False,
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