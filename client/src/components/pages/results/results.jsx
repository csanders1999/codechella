import React, { Component } from 'react';
import Navbar from "../../navbar/navbar";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import "./results.css"

import Tweets from "../../tweets/tweets";

export class results extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            auth: false,
            total: 100,
            flagged: 10,
            errors: []
        }
    }


    render() {
        const test = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Error, rem quae! Temporibus nisi blanditiis est, itaque iusto eum quo praesentium aliquam voluptatum. Mollitia, a autem dolorum quo ipsam amet illo!"
        return (
            
            <>
                <Navbar />
                <Col className="summary-text">
                    <h1 className="display-1">Summary</h1>
                </Col>
                <Row className="info-con">
                    <Col>
                        80%
                    </Col>
                    <Col>
                        < Tweets body={test} id={1}/>
                        < Tweets body={test}/>
                        < Tweets body={test}/>
                        
                    </Col>
                    <Col>
                        Suggestions
                    </Col>
                </Row>
                
            </>
        )
    }
}

export default results
