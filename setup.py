from setuptools import setup

exec (open('dash_dangerously_set_inner_html/version.py').read())

setup(
    name='dash_dangerously_set_inner_html',
    version=__version__,
    author='plotly',
    packages=['dash_dangerously_set_inner_html'],
    include_package_data=True,
    license='MIT',
    description='A dash component for specifying raw HTML',
    install_requires=[]
)
