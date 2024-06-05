import sys

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

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py /path/to/markdown [--out /path/to/output.html]", file=sys.stderr)
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = None
    if len(sys.argv) > 2 and sys.argv[2] == '--out':
        if len(sys.argv) > 3:
            output_file_path = sys.argv[3]
        else:
            print("Error: --out specified but no output file given", file=sys.stderr)
            sys.exit(1)

    try:
        with open(input_file_path, 'r') as file:
            markdown_text = file.read()
    except Exception as e:
        print(f"Error: cannot read file {input_file_path}. Details: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        html_text = convert_markdown_to_html(markdown_text)
    except Exception as e:
        print(f"Error: invalid markdown. Details: {e}", file=sys.stderr)
        sys.exit(1)

    if output_file_path:
        try:
            with open(output_file_path, 'w') as file:
                file.write(html_text)
        except Exception as e:
            print(f"Error: cannot write to file {output_file_path}. Details: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(html_text)

if __name__ == "__main__":
    main()
