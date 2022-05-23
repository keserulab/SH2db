function barchart(url_mask, width, height){
    
    // append the svg object to the body of the page
    d3.select("svg").remove();
    const svg = d3.select("#grouped_bars")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform",`translate(${margin.left},${margin.top})`);
        
    // Parse the Data 
    d3.csv( url_mask ).then( function(data) {
    
    // List of subgroups = header of the csv files = soil condition here
    const subgroups = data.columns.slice(1)

    // List of groups = species here = value of the first column called group -> I show them on the X axis
    const groups = data.map(d => d.group)

    const max_y = d3.max(data.map(d => d.count).values())

    console.log(groups)

    // Add X axis
    const x = d3.scaleBand()
        .domain(groups)
        .range([0, width])
        .padding([0.4])
    svg.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(d3.axisBottom(x).tickSize(0));
    

    // Add Y axis
    const y = d3.scaleLinear()
    .domain([0, 1.1 * max_y])
    .range([ height, 0 ]);
    svg.append("g")
    .call(d3.axisLeft(y));

    // Another scale for subgroup position?
    const xSubgroup = d3.scaleBand()
    .domain(subgroups)
    .range([0, x.bandwidth()])
    .padding([0.05])

    // color palette = one color per subgroup
    const color = d3.scaleOrdinal()
    .domain(subgroups)
    .range(['#e41a1c','#377eb8','#4daf4a'])

    // Show the bars
    const rects = svg.append("g")
    .selectAll("g")
    // Enter in data = loop group per group
    .data(data)
    .join("g")
        .attr("transform", d => `translate(${x(d.group)}, 0)`)
    .selectAll("rect")
    .data(function(d) { return subgroups.map(function(key) { return {key: key, value: d[key]}; }); })
    .join("rect")
        .attr("x", d => xSubgroup(d.key))
        .attr("y", d => y(d.value))
        .attr("width", xSubgroup.bandwidth())
        .attr("height", d => height - y(d.value))
        .attr("fill", d => color(d.key));

    rects
        .transition()
        .duration(1000) // duration of the animation
        .delay(200) // delay animation start
        .attr("cx", (d, i) => d * 50)
        .attr("cy", (d, i) => 40 + i * 100)
        .transition() // start another transition after the first one ended
        .attr("r", 20);
        
    });

}