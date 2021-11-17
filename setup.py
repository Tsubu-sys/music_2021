from setuptools import find_packages, setup

setup(
    name='hpss',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/Tsubu-sys/music_2021',
    install_requires=[
        'tensorflow',
        'numpy',
        'librosa',
        'tqdm',
        'pandas',
        'matplotlib',
        'soundfile'
    ],
    entry_points={
        "console_scripts": [
            "hpss = anomaly.hpss:main",
        ]
    },
    license='GPLv3',
    author='',
    author_email='',
    description=''
)
