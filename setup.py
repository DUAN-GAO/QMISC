from setuptools import setup

setup(
    name='QMISC',
    version='1.0',
    packages=['QMISC'],
    install_requires=[
        "graphein==1.7.7",
        
    ],  
    author='DUAN GAO',
    author_email='gaoduan666@gmail.com',
    description='A tool for quantifying mutation-induced surface changes',
    long_description_content_type='text/x-rst',
    url='https://github.com/DUAN-GAO/QMISC', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)