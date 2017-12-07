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
