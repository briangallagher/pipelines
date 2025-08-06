import os
import re
from typing import List

import setuptools


def get_requirements(requirements_file: str) -> List[str]:
    """Read requirements from a requirements file."""
    file_path = os.path.join(os.path.dirname(__file__), requirements_file)
    with open(file_path, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if not line.startswith('#') and line]
    return lines


def find_version(*file_path_parts: str) -> str:
    """Get version from kubeflow.kfp.version.__version__."""
    file_path = os.path.join(os.path.dirname(__file__), *file_path_parts)
    with open(file_path, 'r') as f:
        version_file_text = f.read()
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file_text,
        re.M,
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError(f'Unable to find version string in file: {file_path}.')


def read_readme() -> str:
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    with open(readme_path) as f:
        return f.read()


docker = ['docker']
kubernetes = ['kfp-kubernetes<2']

setuptools.setup(
    name='kfp',  # Keep PyPI name the same for backward compatibility
    version=find_version('kubeflow', 'kfp', 'version.py'),
    description='Kubeflow Pipelines SDK (under the kubeflow namespace)',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    author='The Kubeflow Authors',
    url='https://github.com/kubeflow/pipelines',
    project_urls={
        'Documentation': 'https://kubeflow-pipelines.readthedocs.io/en/stable/',
        'Bug Tracker': 'https://github.com/kubeflow/pipelines/issues',
        'Source': 'https://github.com/kubeflow/pipelines/tree/master/sdk',
        'Changelog': 'https://github.com/kubeflow/pipelines/blob/master/sdk/RELEASE.md',
    },
    install_requires=get_requirements('requirements.in'),
    extras_require={
        'all': docker + kubernetes,
        'kubernetes': kubernetes,
    },
    packages=setuptools.find_packages(
        include=['kubeflow.kfp*'],
        exclude=['tests*', '*.tests*', '*_test*']
    ),
    namespace_packages=['kubeflow'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.9.0',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'kubeflow-pipelines=kubeflow.kfp.cli.__main__:main',
            'kf-pipelines=kubeflow.kfp.cli.__main__:main',
            'dsl-compile=kubeflow.kfp.cli.compile_:main',
            # Deprecated but retained for backward compatibility
            'kfp=kubeflow.kfp.cli.__main__:main',
        ]
    },
)
