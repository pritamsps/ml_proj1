from setuptools import find_packages,setup
from typing import List
hype='-e .'
def get_requirements(file_path)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hype in requirements:
            requirements.remove(hype)
setup(
name='ml_proj1',
version='0.0.1',
author='sps',
author_email='pritam.montfort@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)