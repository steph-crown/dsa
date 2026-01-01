// given N lines of HTML, find the tag names and print them in the order they appear as a string separated by semicolons

function detectHTML(html) {
  const matches = html.match(/<(\w+)/g)?.map((tag) => tag.substring(1)) || [];
  const uniqueSortedTags = [...new Set(matches)].sort();

  console.log(uniqueSortedTags.join(";"));
}

detectHTML(`<p><a href="http://www.quackit.com/html/tutorial/html_links.
cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/
html_links_examples.cfm">More Link Examples...</a></div>`);
