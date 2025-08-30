from setuptools import setup, find_packages

setup(
    name='clean-code-analyzer',
    version='0.1',
    packages=find_packages(),
    install_requires=['requests', 'pylint'],  # Added necessary dependencies
    entry_points={
        'console_scripts': [
            'clean-code-analyzer=analyzer:main',
        ],
    },
    description='A tool to analyze Python code for clean code practices',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/clean-code-analyzer',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)