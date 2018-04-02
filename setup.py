from setuptools import setup

setup(
    name='LilUFO',
    version='1.0',
    py_modules=['lilufo'],
    include_package_data=True,
    install_requires=[
        'click',
        'pillow',
    ],
    entry_points='''
        [console_scripts]
        lilufo=lilufo:cli
    ''',
)
