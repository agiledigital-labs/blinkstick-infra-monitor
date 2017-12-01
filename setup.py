from setuptools import setup

setup(name='blinkstick_infra_monitor',
      version='0.0.1',
      description='An attempt at showing infrastucture health on a light strip',
      url='https://github.com/agiledigital/blinkstick-infra-monitor',
      author='Sean Dawson',
      author_email='spdawson@agiledigital.com.au',
      license='MIT',
      packages=['blinkstick_infra_monitor'],
      scripts=["bin/blinkstick_infra_monitor"],
      install_requires=[
   		'BlinkStick',
   		'pyusb',
   		'schedule'
	  ])
