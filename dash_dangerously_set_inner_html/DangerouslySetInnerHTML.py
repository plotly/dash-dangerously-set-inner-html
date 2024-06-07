# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DangerouslySetInnerHTML(Component):
    """A DangerouslySetInnerHTML component.
Render a string of raw, unescaped HTML.
This uses React.js's `dangerouslySetInnerHTML` method.
From React.js's documentation, note that:
> Setting HTML from code is risky because it's easy to
> inadvertently expose your users to a cross-site scripting (XSS)
> (https://en.wikipedia.org/wiki/Cross-site_scripting)
> attack.
So, you can set HTML directly in Dash through React.js, but you have
to type out dangerouslySetInnerHTML to remind yourself that it's dangerous.

In most cases, you are safer using the Dash HTML component classes,
dash-html-components (https://github.com/plotly/dash-html-components).
You can also provide HTML in a sandboxed iframe using the
`dash_html_components.IFrame(srcDoc='raw html here')` component,
see , see https://community.plotly.com/t/rendering-html-similar-to-markdown/6232/2?u=chriddyp

Note that the elements in the HTML block that is generated will can not
be targeted with Dash callbacks.

Keyword arguments:
- children (string; optional): An string of raw, unescaped HTML that will be rendered directly"""
    @_explicitize_args
    def __init__(self, children=None, **kwargs):
        self._prop_names = ['children']
        self._type = 'DangerouslySetInnerHTML'
        self._namespace = 'dash_dangerously_set_inner_html'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DangerouslySetInnerHTML, self).__init__(children=children, **args)
