import React, { Component } from 'react';
import { Router, Route, Switch, Redirect } from 'react-router-dom'
import history from './history'
import { connect } from 'react-redux'

import Home from './components/layout/Home'
import Header from './components/layout/Header'
import Login from './components/Login'
import Feeds from './components/workspaces/Feeds'
import Explore from './components/workspaces/Explore'
import Teams from './components/workspaces/Teams'


const PrivateRoutes = ({ children, ...rest }) => {
  // redirect to login
  return (
      localStorage.getItem('isLoggedIn') ? (
              children
        ) : ("")
  )
}


class App extends Component {

  render () {
    return (
      
        <Router history={history}>
            <Header />
            <div className="container">
              <Switch>
                <Route exact path='/' component={Home} />
                <Route exact path='/login/' component={Login} />

                <PrivateRoutes>
                  <Route exact path='/feeds/' component={Feeds} />
                  <Route exact path='/explore/' component={Explore} />
                  <Route exact path='/teams/' component={Teams} />
                  <Route exact path="/logout/">
                      {this.props.auth.isLoggedIn ?<Home /> : <Redirect to="/login/" />}
                  </Route>
                </PrivateRoutes>
              </Switch>
            </div>
        </Router>
    );
  }
}

const mapStateToProps = (state) => {
  return {
      auth: state.auth,
  }
}

const mapDispatchToProps = dispatch => ({

})

export default connect(mapStateToProps, mapDispatchToProps)(App);
