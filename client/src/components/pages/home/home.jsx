import React, { Component } from 'react';
import Navbar from '../../navbar/navbar.jsx';
import Searchbox from "../../searchbox/searchbox";

export class home extends Component {
    render() {
        return (
            <div>
                <Navbar />
                <Searchbox />
            </div>
        )
    }
}

export default home
