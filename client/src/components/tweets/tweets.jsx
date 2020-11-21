import React, { Component } from 'react';
import Card from "react-bootstrap/Card";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Image from "react-bootstrap/Image";
import "./tweets.css";

import trash from "../../images/trashcan.svg";

export class tweets extends Component {
    constructor(props) {
        super(props);
        this.state = {
            body: this.props.body,
            reason: this.props.reason,
        }
    }

    delete = (id) => {
        console.log("clicked");
    }

    render() {
        const { body, reason } = this.state;

        return (
            <>
                <Row> 
                    <Card className="tweet-card mt-4">
                        <Card.Body>
                            {body}
                        </Card.Body>
                    </Card>
                    <Image src={trash} className="ml-3" onClick={() => this.delete(this.props.id)} />
                </Row>
                

                <Col className="mt-3 reason">
                    This Tweet is unprofessional because {body}
                </Col>
            </>
        )
    }
}

export default tweets
