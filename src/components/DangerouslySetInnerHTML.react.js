import React, {PropTypes} from 'react';

/**
 * Render a string of raw, unescaped HTML.
 * This uses React.js's `dangerouslySetInnerHTML` method.
 * From React.js's documentation, note that:
 * > Setting HTML from code is risky because it's easy to
 * > inadvertently expose your users to a cross-site scripting (XSS)
 * > (https://en.wikipedia.org/wiki/Cross-site_scripting)
 * > attack.
 * So, you can set HTML directly in Dash through React.js, but you have
 * to type out dangerouslySetInnerHTML to remind yourself that it's dangerous.
 *
 * In most cases, you are safer using the Dash HTML component classes,
 * dash-html-components (https://github.com/plotly/dash-html-components).
 * You can also provide HTML in a sandboxed iframe using the
 * `dash_html_components.IFrame(srcDoc='raw html here')` component,
 * see , see https://community.plot.ly/t/rendering-html-similar-to-markdown/6232/2?u=chriddyp
 *
 * Note that the elements in the HTML block that is generated will can not
 * be targeted with Dash callbacks.
 */
function DangerouslySetInnerHtml(props) {
    const htmlObject = {__html: props.children};
    return (
        <div dangerouslySetInnerHTML={htmlObject}/>
    )
}

DangerouslySetInnerHtml.propTypes = {
    /**
     * An string of raw, unescaped HTML that will be rendered directly
     */
    children: PropTypes.string
};

export default DangerouslySetInnerHtml;
