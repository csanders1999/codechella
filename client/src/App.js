import React, { Component  } from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import home from "./components/pages/home/home";
import login from "./components/pages/login/login";
import results from "./components/pages/results/results";

export default class App extends Component {
  render(){
    return (

      <Router>
          <Switch>
            <Route exact path="/" component={login} />
            <Route exact path="/home" component={home} />
            <Route exact path="/results" component={results} />
          </Switch>
        </Router>
   
    );
  }
}
