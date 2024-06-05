# main.py
import sys
from markdown_to_html import convert_markdown_to_html

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py /path/to/markdown [--out /path/to/output.html]", file=sys.stderr)
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
