var my_data = d3.json('/json')

//console.log(my_data)

my_data.then(function(bb) {
  let width = 150, height = 150;
  let projection = d3.geoAzimuthalEqualArea()
  projection.fitSize([width, height], bb);
  let context = d3.select('#content canvas')
    //.node()
    //.getContext('2d');
  let geoGenerator = d3.geoPath()
    .projection(projection)
    //.context(context);
  let svg = d3.select("body").append('svg')
    .style("width", width).style("height", height);

  //console.log(bb.features);

  svg.append('g').selectAll('path')
    .data(bb.features)
    .join('path')
    .attr('d', geoGenerator)
    .attr('fill', '#088')
    .attr('stroke', '#000')
    .attr('viewbox', '0 0 1000 1000');
}); 
