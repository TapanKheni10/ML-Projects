## This setup.py file is responsible for creating our machine learning application
## as package and this will allow us to use our application in our programs as noraml python package.

## Initial code
## setup.py file will automatically get trigered --> -e .
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements

## Meta data about our machine learning application
setup(
    name="MLProject",
    version="0.0.1",
    author="Tapan_Kheni",
    author_email="tapankheni10304@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)