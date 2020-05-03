import React, { Component } from 'react';
import { Router, Route, Switch, Redirect } from 'react-router-dom'
import history from './history'
import { connect } from 'react-redux'

import Home from './components/layout/Home'
import Header from './components/layout/Header'
import Login from './components/Login'
import Notes from './components/workspaces/Notes'
import Explore from './components/workspaces/Explore'
import Teams from './components/workspaces/Teams'

// fetch datas
import { notesFetch } from './actions/notes'


const PrivateRoutes = ({ children, ...rest }) => {
  // redirect to login
  return (
      localStorage.getItem('isLoggedIn') ? (
              children
        ) : ("")
  )
}


class App extends Component {

  componentWillMount() {
    this.props.notesFetch()
  }

  render () {
    return (
      
        <Router history={history}>
            <Header />
            <div className="container">
              <Switch>
                <Route exact path='/' component={Home} />
                <Route exact path='/login/' component={Login} />

                <PrivateRoutes>
                  <Route exact path='/notes/' component={Notes} />
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
      notes: state.noteReducer.notes
  }
}

const mapDispatchToProps = dispatch => ({
  notesFetch: () => dispatch(notesFetch()),
})

export default connect(mapStateToProps, mapDispatchToProps)(App);
