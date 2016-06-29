from setuptools import setup

setup(name='flower-platform-raspberry-pi-runtime',
    version = '1.0',
    description = 'Flower Platform Runtime for Raspberry Pi',
    author = 'Crispico',
    author_email = 'flower@flower-platform.org',
    url='http://www.flower-platform.org/',
    include_package_data = True,
    package_dir = {'FlowerPlatformRuntime': 'lib-src'},
    packages = ['FlowerPlatformRuntime'],
)