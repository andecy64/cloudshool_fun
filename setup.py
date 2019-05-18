from setuptools import setup, find_packages

setup(
    author="Barak Avrahami",
    author_email='barak1345@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Fun with devops tools",
    install_requires=[
        'mysql',
        'munch', 
        'pillow', 
        'PyGithub',
        'flask',
        ],
    include_package_data=True,
    keywords='cloudschool_fun',
    name='cloudschool_fun',
    packages=find_packages(exclude=['tests']),
    scripts=['scripts/get_image.py', 'scripts/flask_ep.py'],
    test_suite='tests',
    url='https://github.com/andecy64/cloudschool_fun',
    version='0.1.0',
    zip_safe=False,
)
