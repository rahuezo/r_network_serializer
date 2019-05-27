from setuptools import setup


setup(
    name='r_network_serializer', 
    version='0.1',
    description='A tool to read csv adjacency matrices into serialized R network objects.',
    url='https://github.com/rahuezo/r_network_serializer',
    author='Rudy Huezo',
    author_email='rahuezo@ucdavis.edu',
    license='MIT',
    packages=['r_network_serializer', 'r_network_serializer.rnetwork', 'r_network_serializer.serialize'],
    zip_safe=False
)