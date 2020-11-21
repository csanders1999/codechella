import React, { Component } from 'react';
import Navbar from "../../navbar/navbar";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Button from "react-bootstrap/Button";
import "./results.css"

import Tweets from "../../tweets/tweets";
import Graph from "../../graph/graph";

export class results extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            auth: false,
            total: 100,
            flagged: 10,
            rating: 80,
            emotion: "sad",
            tweets: [],
            errors: []
        }
    }

    componentDidMount() {
        const test = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Error, rem quae! Temporibus nisi blanditiis est, itaque iusto eum quo praesentium aliquam voluptatum. Mollitia, a autem dolorum quo ipsam amet illo!";
        let tweetsSetUp = [];
        for (let i=0; i < 3; i++) {
            tweetsSetUp.push(<Tweets body={test} key={i} />)
        }
        this.setState({
            tweets: tweetsSetUp
        })
    }


    render() {
        const { auth, total, flagged, rating, tweets, emotion } = this.state;

        return (
            
            <>
                <Navbar />
                <Col className="summary-text">
                    <h1 className="display-1">Summary</h1>
                </Col>
                <Row className="info-con">
                    <Col className="ml-5">
                        <Row>
                            <h1 className="display1 rating-text">
                                {rating}%
                            </h1>
                        </Row>
                        <p className="emotion-text"> 
                            Based on your recent 
                            <br />tweets you appear as
                            <div className="emotion-var-text">{emotion}</div>
                        </p>
                        <Graph />
                    </Col>
                    <Col>
                        <h3 className="flagged-text display-5">
                            {flagged} out of {total} tweets deemed "unprofessional"
                        </h3>
                        {tweets}
                        
                    </Col>
                    <Col className="">
                        <Button className="custom-button mb-5" variant="primary">Delete All</Button>
                        <Row>
                            <h4 className="suggestion-text display-4">
                                Suggestions
                            </h4>
                        </Row>
                    </Col>
                </Row>
                
            </>
        )
    }
}

export default results
