import React, { useContext } from "react";
import { Redirect, Route } from "react-router-dom";

function PrivateRoute({ component: Component, ...rest }) {
 
  return (
    <Route
      {...rest}
      render={() =>
        <Redirect to="/" />
      }
    />
  );
}

export default PrivateRoute;
