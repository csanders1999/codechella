import React, { Component } from 'react';
import Navbar from '../../navbar/navbar.jsx';
import Searchbox from "../../searchbox/searchbox";
import Results from "../results/results";

import * as API from "../../../util/api";

export class home extends Component {

    constructor(props) {
        super(props);
        this.state = {
            user: false,
            handle: null,
            results: null,
        };
    }

    handleChange = (input) => (e) => {
        this.setState({ [input]: e.target.value });
        console.log(input, e.target.value);
    };
    
    handleSubmit = (e) => {
        e.preventDefault();
        const { handle } = this.state;
        API.checkUser(handle).then((result) => {
            if (result.status === 200) {
                if (result.data.status === 0) {
                    alert("User not found");
                }
                else {
                    this.setState({ user: true });
                    API.results(handle).then((result) => {
                        if (result.status === 0) {
                            this.setState({
                                result: result.data
                            })
                        }
                    })
                }
            }
        })
        .catch((errors) => {
            console.log(errors);
            this.setState({
              errors
            })
        })
    };

    handleClickTitle = () => {
        this.setState({
            user: false
        })
    }

    render() {
        const { user, results } = this.state;

        if (!user) {
            return (
                <>
                    <Navbar click={this.handleClickTitle} />
                    <Searchbox click={this.handleSubmit} change={this.handleChange} />
                </>
            )
        }
        else {
            return (
                <>
                    <Navbar click={this.handleClickTitle} />
                    <Results result={results} />
                </>
            )
        }
    }
}

export default home
