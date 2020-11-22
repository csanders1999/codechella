import React, { Component } from 'react';
import Navbar from "../../navbar/navbar";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Button from "react-bootstrap/Button";
import "./results.css"

import Tweets from "../../tweets/tweets";
import Graph from "../../graph/graph";
import Suggestion from "../../suggestion/suggestion";

export class results extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            results: this.props.result,
            emotion: this.props.result.first_impression,
            totalTweets: this.props.result.total_number_of_tweets,
            amountUnprofessionalTweets: this.props.result.number_of_unprofessional_tweets,
            unprofessionalTweets: this.props.result.unprofessional_tweets,
            pictureTweets: this.props.result.unprofessional_photos,
            rating: this.props.result.percentage,
            graphData: this.props.result.graph_data,
            suggestions: this.props.result.suggestions,
            tweets: null
        }
        
        /*this.state = {
            results: {},
            emotion: [],
            totalTweets: 0,
            amountUnprofessionalTweets: 1,
            unprofessionalTweets: [{id: 123, reason:"idk", tweet:"hello world!"}],
            pictureTweets: [],
            rating: 0,
            graphData: [
                { name: 'Professional', score: 80 },
                { name: 'Nonprofessional', score: 76 },
                { name: 'Other', score: 20}
            
            ],
            suggestions: ["Try making a bio that aligns with your professional interests!", "Test", "Another Test"],
            tweets: null
        }*/
    }

    componentDidMount() {
        const { unprofessionalTweets, pictureTweets } = this.state;
        let tweetsSetUp = [];
        
        for (let index=0; index < unprofessionalTweets.length; index++) {
            tweetsSetUp.push(<Tweets body={unprofessionalTweets[index].tweet} reason={unprofessionalTweets[index].reason} key={unprofessionalTweets[index].id} />)
        }

        for (let index=0; index < pictureTweets.length; index++) {
            tweetsSetUp.push(<Tweets body={pictureTweets[index].tweet} reason={pictureTweets[index].reason} key={pictureTweets[index].id} />)
        }

        this.setState({
            tweets: tweetsSetUp
        })
    }


    render() {
        const { emotion, totalTweets, amountUnprofessionalTweets, rating, tweets, graphData, suggestions } = this.state;

        return (
            
            <>
                
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
                            <br />tweets you appear as <b>{emotion}</b>
                        </p>
                        <Graph data={graphData} />
                    </Col>
                    <Col>
                        <h3 className="flagged-text display-5">
                            {amountUnprofessionalTweets} out of {totalTweets} tweets deemed "unprofessional"
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
                        <Suggestion data={suggestions} />
                    </Col>
                </Row>
                
            </>
        )
    }
}

export default results
