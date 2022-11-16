import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='biggmodules',
    version='0.0.3',
    author='Michele Cantoni',
    author_email='mcantoni81@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/misterkilgore/test_repo',
    project_urls = {
        "Bug Tracker": "https://github.com/misterkilgore/test_repo/issues"
    },
    license='MIT',
    packages=['biggmodules'],
    install_requires=['numpy'],
)
