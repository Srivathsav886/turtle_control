from setuptools import setup

package_name = 'turtle_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=[
        'turtle_control.random_velocity_publisher',
        'turtle_control.boundary_monitor'
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='srivathsav',
    maintainer_email='yainchasrivathsav@gmail.com',
    description='Turtle control package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'random_velocity_publisher = turtle_control.random_velocity_publisher:main',
            'boundary_monitor = turtle_control.boundary_monitor:main',
        ],
    },
)
