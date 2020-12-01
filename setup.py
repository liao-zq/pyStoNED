from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='pystoned',
    version='0.4.0',
    description='A Package for Stochastic Nonparametric Envelopment of Data (StoNED) in Python',
    long_description_content_type="text/markdown",
    long_description=README,
    license='GPLv3',
    packages=find_packages(),
    author='Sheng Dai, Timo Kuosmanen, Chia-Yen Lee, Yu-Hsueh Fang',
    author_email='sheng.dai@aalto.fi',
    keywords=['StoNED', 'CNLS', 'CER', 'CQR', 'Z-variables'],
    url='https://github.com/ds2010/StoNED-Python',
    download_url='https://pypi.org/project/pystoned/',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    package_data={'pystoned': ['data/*.csv']},
)

install_requires = [
    'pyomo>=5.6.9',
    'pandas',
    'numpy',
    'scipy',
    'matplotlib'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
