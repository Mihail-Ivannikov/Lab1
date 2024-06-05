# markdown_to_html.py
def convert_markdown_to_html(markdown_text):
    html_text = ""
    lines = markdown_text.split('\n')
    in_preformatted = False
    
    for line in lines:
        if line.strip() == "```":
            if in_preformatted:
                html_text += "</pre>\n"
                in_preformatted = False
            else:
                html_text += "<pre>\n"
                in_preformatted = True
            continue
        
        if in_preformatted:
            html_text += line + '\n'
            continue

        line = line.replace('**', '<b>', 1).replace('**', '</b>', 1)
        line = line.replace('_', '<i>', 1).replace('_', '</i>', 1)
        line = line.replace('`', '<tt>', 1).replace('`', '</tt>', 1)
        
        if line.strip():
            if not html_text.endswith('</p>\n') and not html_text.endswith('<pre>\n'):
                html_text += "<p>"
            html_text += line + ' '
        else:
            if html_text.endswith(' '):
                html_text = html_text.rstrip() + "</p>\n"

    if html_text.endswith(' '):
        html_text = html_text.rstrip() + "</p>\n"
    
    return html_text.strip()
