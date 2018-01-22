from setuptools import setup

main_ns = {}
exec(open('dash_dangerously_set_inner_html/version.py').read(), main_ns)

setup(
    name='dash_dangerously_set_inner_html',
    version=main_ns['__version__'],
    author='plotly',
    packages=['dash_dangerously_set_inner_html'],
    include_package_data=True,
    license='MIT',
    description='A dash component for specifying raw HTML',
    install_requires=[]
)
