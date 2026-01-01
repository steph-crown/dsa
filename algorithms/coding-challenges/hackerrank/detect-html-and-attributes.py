import re

def process_html(lines):
    html_content = '\n'.join(lines)

    without_comments = re.sub(r'<!--[\s\S]*?-->', '', html_content)

    tag_regex = r'<(\w+)([^>]*)>'
    attribute_regex = r'(\w+)=["\'](.*?)["\']'

    results = []

    for match in re.finditer(tag_regex, without_comments):
        tag_name = match.group(1)
        attributes_str = match.group(2).strip()

        results.append(tag_name)

        if attributes_str:
            for attr_match in re.finditer(attribute_regex, attributes_str):
                attr_name = attr_match.group(1)
                attr_value = attr_match.group(2)
                results.append(f"-> {attr_name} > {attr_value}")

    print('\n'.join(results))

def detect_html_and_attributes(input_str):
    lines = input_str.strip().split('\n')
    num_lines = int(lines[0])

    if 0 < num_lines < 100:
        html_lines = lines[1:num_lines+1]
        return process_html(html_lines)

    return ''

# For testing with the sample input
sample_input = """9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash"
  data="your-file.swf"
  width="0" height="0">
<!-- <param name="movie" value="your-file.swf" /> -->
<param name="quality" value="high"/>
</object>"""

# def main():
#     # Read the number of lines
#     num_lines = int(input().strip())

#     if 0 < num_lines < 100:
#         # Read the HTML lines
#         html_lines = [input() for _ in range(num_lines)]
#         result = process_html(html_lines)
#         print(result)

# if __name__ == "__main__":
#     main()
