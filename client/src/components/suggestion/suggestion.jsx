import React, { Component } from 'react';
import Card from "react-bootstrap/Card";

import "./suggestion.css";

export class suggestion extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            data: this.props.data,
            list: null
        };
    }

    componentDidMount () {
        const { data } = this.state;
        let ul = [];

        for (let index=0; index < data.length; index++) {
            ul.push(<Card className="suggestion mt-4">{ data[index] }</Card>)
        }

        this.setState({
            list: ul
        })
    }

    render() {
        const { list } = this.state;

        return (
            <div className="mt-4">
                { list }
            </div>
        )
    }
}

export default suggestion
