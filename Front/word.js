// ************** Generate the tree diagram	 *****************
var margin = {top: 20, right: 120, bottom: 20, left: 20},
	width = 1887 - margin.right - margin.left,
	height = 3000 - margin.top - margin.bottom;

var i = 0;

var tree = d3.layout.tree()
	.size([height, width]);

var diagonal = d3.svg.diagonal()
	.projection(function(d) { return [d.y, d.x]; });

var svg = d3.select("body").append("svg")
	.attr("width", width + margin.right + margin.left)
	.attr("height", height + margin.top + margin.bottom)
  .append("g")
	.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

let url = new URL(window.location.href);
console.log(url.pathname.replace(/[^/]*$/, ''));
let data_name = url.searchParams.get("data");
if(!data_name){
	data_name = 'whole';
}
let word = url.searchParams.get("word");
let path = "../Data/trees/"+data_name+"/tree_with_languages.json";
// load the external data
d3.json(path, function(error, treeData) {
  root = treeData[0];
  update(root);
});

function update(source) {

  // Compute the new tree layout.
  var nodes = tree.nodes(root).reverse(),
	  links = tree.links(nodes);

  // Normalize for fixed-depth.
  // nodes.forEach(function(d) { d.y = d.distance ? (d.parent.y + d.distance*25) : d.depth*150; });

  // Declare the nodes…
  var node = svg.selectAll("g.node")
	  .data(nodes, function(d) { return d.id || (d.id = ++i); });

  // Enter the nodes.
  var nodeEnter = node.enter().append("g")
	  .attr("class", "node")
	  .attr("transform", function(d) {
		  return "translate(" + d.y + "," + d.x + ")"; });

  var nodeA = nodeEnter.append("a")
		.attr("xlink:href", function(d) { return url.pathname.replace(/[^/]*$/, '') + "language.html?langs="+d.name+"&dir="+data_name; })
		.attr("target", "_blank");

	nodeA.append("ellipse")
	  .attr("rx", function(d) { return d.lang[word] ? (d.children || d._children ? d.lang[word].length*5 : (d.lang[word].length + d.name.length + 3)*5) : 0 })
    .attr("ry", function(d) { return 10 })
	  .style("fill", function(d) {
      return "#fff1cc"});

  nodeA.append("text")
	  .attr("x", function(d) {
		  return d.lang[word].length*3; })
	  .attr("dy", ".3em")
	  .attr("text-anchor", function(d) {
		  return "end"; })
	  .text(function(d) { return d.lang[word] ? (d.children || d._children ? d.lang[word] : d.lang[word] + ' (' + d.name + ')') : ''; })
	  .style("fill-opacity", 1)
    .style("display", function(d) { return 'block'; });

  // nodeEnter.append("text")
	//   .attr("x", -45)
  //   .attr("dy", "-0.5em")
	//   .text(function(d) { return d.distance ? Math.round(d.distance * 100) / 100 : ''; })
	//   .style("fill-opacity", 1);

  // Declare the links…
  var link = svg.selectAll("path.link")
	  .data(links, function(d) { return d.target.id; });

  // Enter the links.
  var linkEnter = link.enter().insert("path", "g")
	  .attr("class", "link")
	  .attr("d", diagonal);

	linkEnter.append("text").text(function(d) { return 'aaaaa'; });
}
