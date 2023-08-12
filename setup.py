from setuptools import find_packages,setup
from typing import List

Hyphen_e_dot="-e ."

def get_requirments(file_path:str)->List[str]:
    '''
    this funtion return requirment
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]

        if Hyphen_e_dot in requirments:
            requirments.remove(Hyphen_e_dot)

    return  requirments


setup(
    name='mlproject',
    version='0.0.1',
    author='Himanshu',
    author_email='sharmahimanshu65018@gmail.com',
    pakages=find_packages(),
    install_requires=get_requirments("requirments.txt")
)