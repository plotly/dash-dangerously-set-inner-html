import os as _os
import dash as _dash
import sys as _sys
import json
from .version import __version__

_current_path = _os.path.dirname(_os.path.abspath(__file__))

_components = _dash.development.component_loader.load_components(
    _os.path.join(_current_path, 'metadata.json'),
    'dash_dangerously_set_inner_html'
)

_this_module = _sys.modules[__name__]

_basepath = _os.path.dirname(__file__)
_filepath = _os.path.abspath(_os.path.join(_basepath, 'package.json'))
with open(_filepath) as f:
    package = json.load(f)

js_package_name = package['name']
py_package_name = __name__
js_version = package['version']

_js_dist = [
    {
        'relative_package_path': 'bundle.js',
        'external_url': (
            'https://unpkg.com/{}@{}/{}/bundle.js'
        ).format(js_package_name, js_version, py_package_name),
        'namespace': py_package_name
    }
]

_css_dist = []


for _component in _components:
    setattr(_this_module, _component.__name__, _component)
    setattr(_component, '_js_dist', _js_dist)
    setattr(_component, '_css_dist', _css_dist)
