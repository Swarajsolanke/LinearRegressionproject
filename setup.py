from setuptools import find_packages,setup
from typing  import List

Hypene_dot="-e ."
def get_requirement(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_object: # open the file requirements.txt
        requirements=file_object.readlines() # read this one by one 
        requirements=[req.replace("/n","") for req in requirements]

        if Hypene_dot in requirements:
            requirements.remove(Hypene_dot)
    return requirements
setup(
    name="Regressorproject",
    author="Swaraj",
    author_email="swarajsolanke02@gmail.com",
    version="0.0.1",
    install_requirements=get_requirement("requirements.txt"),
    packages=find_packages()
)


