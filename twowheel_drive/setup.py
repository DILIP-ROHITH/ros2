from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'twowheel_drive'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # Install the launch files in the shared directory
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        # Install the URDF files in the shared directory
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rohith',
    maintainer_email='rohithkarella@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
