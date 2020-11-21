import React, { Component } from 'react';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Container from 'react-bootstrap/Container';
import "./searchbox.css";

export class searchbox extends Component {
    render() {
        return (
            <Container className="custom-container">
                <div className="mb-5 title-text">How professional is your Twitter?</div>
                <Form inline>
                    <Col>
                        <Form.Control className="cutom-searchbox" type="email" placeholder="Your Twitter @" />
                    </Col>
                    <Col>
                        <Button className="custom-button" variant="primary">Search</Button>
                    </Col>
                </Form>
                <Container className="slogan-container mt-5">
                    <Row className="ml-1">
                        Upon entering your Twitter account, this site will rate your Twitter's
                    </Row>
                    <Row>
                        professionalism, show you your Tweets deemed "unprofessional", and
                    </Row>
                    <Row className="text-shift">
                        offer suggestions on how to boost your rating. 
                    </Row>
                </Container>
            </Container>
        )
    }
}

export default searchbox
