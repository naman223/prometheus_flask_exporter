from setuptools import setup

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='prometheus_flask_exporter',
    packages=['prometheus_flask_exporter'],
    version='0.20.3',
    description='Prometheus metrics exporter for Flask',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author='Viktor Adam',
    author_email='rycus86@gmail.com',
    url='https://github.com/rycus86/prometheus_flask_exporter',
    download_url='https://github.com/rycus86/prometheus_flask_exporter/archive/0.20.3.tar.gz',
    keywords=['prometheus', 'flask', 'monitoring', 'exporter'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Monitoring',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=['prometheus_client', 'flask'],
)
