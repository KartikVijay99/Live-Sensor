from setuptools import find_packages , setup 
from typing import List 

def get_requirements () -> list [ str ] :
    
    requirements_list = list [ str ] = []
    
    return 

setup (
    name = 'Sensor' ,
    version= "0.0.1" ,
    author= "Kartik" ,
    author_email= "kartikvijay9680@gmail.com" ,
    packages = find_packages() , 
    install_requires= ["pymongo"] ,
    install_requires = get_requirements( ) , # ["pymongo"]
)