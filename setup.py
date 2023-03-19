from setuptools import find_packages, setup
from typing import List

unreq = '-e .'
def get_requirements(file_path:str)-> List[str]:

    requirements = []
    with open(file_path) as file_obj:

        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]

        if unreq in requirements:

            requirements.remove(unreq)
    
    return requirements

setup(
    name = 'Performance Prediction',
    version = '0.0.1',
    author = 'Kalyan',
    author_email = 'kalyanmurapaka274@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)