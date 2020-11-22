import React, { Component  } from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import home from "./components/pages/home/home";
import login from "./components/pages/login/login";
import results from "./components/pages/results/results";
import PrivateRoute from "./privateRoute";
import "./App.css";

export default class App extends Component {
  render(){
    return (
      <div className="App">
        <Router>
          <Switch>
            <Route exact path="/" component={home} />
            <Route exact path="/login" component={login} />
            <Route exact path="/results" component={results} />
          </Switch>
        </Router>
      </div>
    );
  }
}
