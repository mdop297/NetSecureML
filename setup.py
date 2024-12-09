from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    requirements = []
    try: 
        with open("requirements.txt", "r") as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()
                if requirement and requirement!="-e .":
                    requirements.append(requirement)
    except FileNotFoundError:
        raise Exception("requirements.txt not found")

    return requirements

setup(
    name="NetSecureML",
    version="0.0.1",
    author="MDOP297",
    author_email="lenhatminh297@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
