function processHTML(lines) {
  // Combine lines to handle multiline tags
  const htmlContent = lines.join("\n");

  // Remove HTML comments
  const withoutComments = htmlContent.replace(/<!--[\s\S]*?-->/g, "");

  // Regex to match HTML tags with attributes
  const tagRegex = /<(\w+)([^>]*)>/g;
  const attributeRegex = /(\w+)=["']([^"']*)["']/g;

  let match;
  const results = [];

  while ((match = tagRegex.exec(withoutComments)) !== null) {
    const tagName = match[1];
    const attributesStr = match[2].trim();

    results.push(tagName);

    if (attributesStr) {
      let attrMatch;
      while ((attrMatch = attributeRegex.exec(attributesStr)) !== null) {
        const attrName = attrMatch[1];
        const attrValue = attrMatch[2];
        results.push(`-> ${attrName} > ${attrValue}`);
      }
    }
  }

  console.log(results.join("\n"));
}

function detectHTMLAndAttributes(input) {
  const lines = input.trim().split("\n");
  const numLines = parseInt(lines[0], 10);

  if (numLines >= 1 && numLines < 100) {
    const htmlLines = lines.slice(1, numLines + 1);
    return processHTML(htmlLines);
  }

  return "";
}

// For testing with the sample input
const sampleInput = `9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash"
  data="your-file.swf"
  width="0" height="0">
<!-- <param name="movie" value="your-file.swf" /> -->
<param name="quality" value="high"/>
</object>`;

detectHTMLAndAttributes(sampleInput);
