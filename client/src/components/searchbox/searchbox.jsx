import React, { Component } from 'react';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import "./searchbox.css";

export class searchbox extends Component {
    render() {
        return (
            <Container className="custom-container">
                <div>How professional is your Twitter?</div>
                <Form inline>
                    <Form.Control type="email" placeholder="Your Twitter @" />
                    <Button className="ml-4 custom-button" variant="primary">Search</Button>
                </Form>
                <div>
                    Upon entering your Twitter account, this site will rate your Twitter's professionalism, show you your Tweets deemed "unprofessional", and offer suggestions on how to boost your rating. 
                </div>
            </Container>
        )
    }
}

export default searchbox
