# dash-dangerously-set-inner-html

<div align="center">
  <a href="https://dash.plotly.com/project-maintenance">
    <img src="https://dash.plotly.com/assets/images/maintained-by-plotly.png" width="400px" alt="Maintained by Plotly">
  </a>
</div>


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
`dash_html_components.IFrame(srcDoc='raw html here')` component, see [https://community.plotly.com/t/rendering-html-similar-to-markdown/6232/2?u=chriddyp](https://community.plotly.com/t/rendering-html-similar-to-markdown/6232/2?u=chriddyp)

Note that the elements in the HTML block that is generated can not
be targeted with Dash callbacks.

The package can be installed with:

```sh
pip install dash-dangerously-set-inner-html
```

## Usage

```py
import dash_dangerously_set_inner_html
import dash
import dash_html_components as html

app = dash.Dash('')

app.scripts.config.serve_locally = True

app.layout = html.Div([
    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
        <h1>Header</h1>
    '''),
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

To set the inner HTML with a Dash callback, do the following:

```py
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML
from dash import Dash, html, Input, Output

app = Dash('')

app.layout = html.Div([
    html.Div(id='target')
    html.Button('Click me!', id='trigger')
])

@app.callback(
    Output('target', 'children')
    Input('trigger', 'n_clicks')
    prevent_initial_call=True
)
def populateFunc(n):
    return DangerouslySetInnerHTML('''
        <h1>You clicked the button!</h1>
    ''')
```

## Dash

Go to this link to learn about [Dash][].

## Getting started

```sh
# Install dependencies
$ npm install

# Watch source for changes and build to `lib/`
$ npm start
```

## Development

### Demo server

You can start up a demo development server to see a demo of the rendered
components:

```sh
$ builder run demo
$ open http://localhost:9000
```

You have to maintain the list of components in `demo/Demo.react.js`.

### Code quality and tests

#### To run lint and unit tests:

```sh
$ npm test
```

#### To run unit tests and watch for changes:

```sh
$ npm run test-watch
```

#### To debug unit tests in a browser (Chrome):

```sh
$ npm run test-debug
```

1. Wait until Chrome launches.
2. Click the "DEBUG" button in the top right corner.
3. Open up Chrome Devtools (`Cmd+opt+i`).
4. Click the "Sources" tab.
5. Find source files
  - Navigate to `webpack:// -> . -> spec/components` to find your test source files.
  - Navigate to `webpack:// -> [your/repo/path]] -> dash-dangerously-set-inner-html -> src` to find your component source files.
6. Now you can set breakpoints and reload the page to hit them.
7. The test output is available in the "Console" tab, or in any tab by pressing "Esc".

#### To run a specific test

In your test, append `.only` to a `describe` or `it` statement:

```js
describe.only('Foo component', () => {
    // ...
});
```

### Testing your components in Dash

1. Build development bundle to `lib/` and watch for changes

        # Once this is started, you can just leave it running.
        $ npm start

2. Install module locally (after every change)

        # Generate metadata, and build the JavaScript bundle
        $ npm run install-local

        # Now you're done. For subsequent changes, if you've got `npm start`
        # running in a separate process, it's enough to just do:
        $ python setup.py install

3. Run the dash layout you want to test

        # Import dash-dangerously-set-inner-html to your layout, then run it:
        $ python my_dash_layout.py


**TODO:** There is a workflow that links your module into `site-packages` which would
make it unnecessary to re-run `2.` on every change: `python setup.py develop`.
Unfortunately, this doesn't seem to work with resources defined in
`package_data`.

See https://github.com/plotly/dash-components-archetype/issues/20


## Installing python package locally

Before publishing to PyPi, you can test installing the module locally:

```sh
# Install in `site-packages` on your machine
$ npm run install-local
```

## Uninstalling python package locally

```sh
$ npm run uninstall-local
```

## Publishing

For now, multiple steps are necessary for publishing to NPM and PyPi,
respectively. **TODO:**
[#5](https://github.com/plotly/dash-components-archetype/issues/5) will roll up
publishing steps into one workflow.

Ask @chriddyp to get NPM / PyPi package publishing accesss.

1. Preparing to publish to NPM

        # Bump the package version
        $ npm version major|minor|patch

        # Push branch and tags to repo
        $ git push --follow-tags

2. Preparing to publish to PyPi

        # Bump the PyPi package to the same version
        $ vi setup.py

        # Commit to github
        $ git add setup.py
        $ git commit -m "Bump pypi package version to vx.x.x"

3. Publish to npm and PyPi

        $ npm run publish-all

## Builder / Archetype

We use [Builder][] to centrally manage build configuration, dependencies, and
scripts.

To see all `builder` scripts available:

```sh
$ builder help
```

See the [dash-components-archetype][] repo for more information.


[Builder]: https://github.com/FormidableLabs/builder
[Dash]: https://github.com/plotly/dash2
[dash-components-archetype]: https://github.com/plotly/dash-components-archetype
