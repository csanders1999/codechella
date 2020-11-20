import React, { Component } from 'react';
import Navbar from 'react-bootstrap/Navbar';
import { Link } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.css';
import "./navbar.css";


export class navbar extends Component {
    render() {
        return (
            <Navbar collapseOnSelect expand="md"className="justify-content-between nav-bar">
                <Navbar.Brand>
                    <Link to="/Home">
                       
                        Project Name
                        
                    </Link>
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                <Navbar.Collapse >
                    
                </Navbar.Collapse>
            </Navbar>
        )
    }
}

export default navbar
