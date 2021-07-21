from setuptools import setup, find_packages


setup(
    name='fizzbuzz',
    version='1.0.0',
    description='FizzBuzz Game',
    author='trevalkov',
    author_email='rodrigolf080@gmail.com',
    url='https://github.com/trevalkov/python_bdd,
    license='GPL',
    keywords='game',
    packages=find_packages(exclude=['specs*']),
    install_requires=[]
)
