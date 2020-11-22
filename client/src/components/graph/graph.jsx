import React, { Component } from 'react';
import * as d3 from "d3";

import "./graph.css";

export class graph extends Component {
    
    constructor(props) {
        super(props)
    
        this.state = {
            width: 500,
            height: 450,
            margin: { top: 50, bottom: 50, left: 50, right: 50 },
            data: this.props.data
        };
    }

    componentDidMount() {
        const { width, height, margin, data } = this.state;

        const svg = d3.select('#d3-container')
            .append('svg')
            .attr('width', width - margin.left - margin.right)
            .attr('height', height - margin.top - margin.bottom)
            .attr("viewBox", [0, 0, width, height]);
        
        // this allows chart to be dynamic and allow any data
        const x = d3.scaleBand()
            .domain(d3.range(data.length))
            .range([margin.left, width - margin.right])
            .padding(0.1)
        
        const y = d3.scaleLinear()
            .domain([0, 100])
            .range([height - margin.bottom, margin.top])
        
        svg
            .append("g")
            .attr("fill", '#1DA1F2')
            .selectAll("rect")
            .data(data.sort((a, b) => d3.descending(a.score, b.score)))
            .join("rect")
            .attr("x", (d, i) => x(i))
            .attr("y", d => y(d.score))
            .attr('title', (d) => d.score)
            .attr("class", "rect")
            .attr("height", d => y(0) - y(d.score))
            .attr("width", x.bandwidth());
        
        function yAxis(g) {
            g.attr("transform", `translate(${margin.left}, 0)`)
            .call(d3.axisLeft(y).ticks(null, data.format))
            .attr("font-size", '20px')
        }
        
        function xAxis(g) {
            g.attr("transform", `translate(0,${height - margin.bottom})`)
            .call(d3.axisBottom(x).tickFormat(i => data[i].name))
            .attr("font-size", '20px')
            .selectAll("text")
                .attr("x", 9)
                .attr("transform", "rotate(90)")
                .style("text-anchor", "start");
        }
        
        svg.append("g").call(xAxis);
        svg.append("g").call(yAxis);
        svg.node();
    }

    render() {
        return (
            <div id="d3-container" className="graph-width" />
        )
    }
}

export default graph
