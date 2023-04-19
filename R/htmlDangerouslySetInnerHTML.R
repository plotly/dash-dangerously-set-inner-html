# AUTO GENERATED FILE - DO NOT EDIT

htmlDangerouslySetInnerHTML <- function(children=NULL) {
    
    props <- list(children=children)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DangerouslySetInnerHTML',
        namespace = 'dash_dangerously_set_inner_html',
        propNames = c('children'),
        package = 'dashDangerouslySetInnerHtml'
        )

    structure(component, class = c('dash_component', 'list'))
}
