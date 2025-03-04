from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    with open("requirements.txt") as file:
        requirements_list = file.read().splitlines()
        requirements_list = [req for req in requirements_list if req and not req.startswith("#")]  
    return requirements_list

setup(
    name="Sensor",
    version="0.0.1",
    author="Kartik",
    author_email="kartikvijay9680@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
