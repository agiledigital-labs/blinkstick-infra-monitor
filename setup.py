from setuptools import setup, find_packages

setup(name='blinkstick_infra_monitor',
      version='0.0.1',
      description='An attempt at showing infrastucture health on a light strip',
      url='https://github.com/agiledigital/blinkstick-infra-monitor',
      author='Sean Dawson',
      author_email='spdawson@agiledigital.com.au',
      license='MIT',
      packages=find_packages(),
      scripts=["bin/blinkstick_infra_monitor"],
      install_requires=[
        'astroid==1.5.3',
        'BlinkStick==1.1.8',
        'certifi==2017.11.5',
        'chardet==3.0.4',
        'idna==2.6',
        'isort==4.2.15',
        'lazy-object-proxy==1.3.1',
        'mccabe==0.6.1',
        'pylint==1.7.4',
        'pyusb==1.0.0b1',
        'requests==2.18.4',
        'schedule==0.5.0',
        'six==1.11.0',
        'urllib3==1.26.5',
        'wrapt==1.10.11'
      ])
