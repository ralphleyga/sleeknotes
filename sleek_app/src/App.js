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
import NoMatch from './components/NoMatch'

// fetch datas
import { notesFetch, workspaceFetch } from './actions/notes'

function PrivateRoute({ children, ...rest }) {
  return (
    <Route
      {...rest}
      render={({ location }) =>
        localStorage.getItem('isLoggedIn') ? (
          children
        ) : (
          <Redirect
            to={{
              pathname: "/login",
              state: { from: location }
            }}
          />
        )
      }
    />
  );
}

class App extends Component {

  componentWillMount() {
    this.props.notesFetch()
    this.props.workspaceFetch()
  }

  render () {

    return (
        <Router history={history}>
            <Header />
            <div className="container">
              <Switch>
                <Route exact path='/' component={Home} />
                <Route exact path='/login/' component={Login} />

                  <PrivateRoute exact path='/notes/'>
                    <Notes />
                  </PrivateRoute>
                  <PrivateRoute exact path='/notes/:noteID'>
                    <Notes />
                  </PrivateRoute>
                  <PrivateRoute exact path='/explore/'>
                    <Explore />
                  </PrivateRoute>
                  <PrivateRoute exact path='/teams/'>
                    <Teams />
                  </PrivateRoute>
                  <PrivateRoute exact path="/logout/">
                      {this.props.auth.isLoggedIn ?<Home /> : <Redirect to="/login/" />}
                  </PrivateRoute>

                <Route component={NoMatch} />
              </Switch>
            </div>
        </Router>
    );
  }
}

const mapStateToProps = (state) => {
  return {
      auth: state.auth,
      notes: state.noteReducer.notes,
      workspaces: state.noteReducer.workspaces
  }
}

const mapDispatchToProps = dispatch => ({
    notesFetch: () => dispatch(notesFetch()),
    workspaceFetch: () => dispatch(workspaceFetch()),
})

export default connect(mapStateToProps, mapDispatchToProps)(App);
