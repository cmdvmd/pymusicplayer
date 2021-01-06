import setuptools

with open('README.md', 'r') as file:
    readme = file.read()

setuptools.setup(
    name='pymp',
    version='0.0.1',
    author='cmdvmd',
    description='An MP3 music player interface',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/cmdvmd/py-music-player',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
        'Topic :: Software Development :: Libraries :: pygame'
    ]
)
