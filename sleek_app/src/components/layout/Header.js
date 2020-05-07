import React, { Component } from 'react'
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import { Link } from 'react-router-dom'
import { connect } from 'react-redux'

import { userLogout } from '../../actions/auth'


const PrivateLink = ({ children, ...rest}) => {
    const nav = rest.isLogin ? (
        children
    ) : (
        null
    )
    return nav
}

class Header extends Component {

    constructor(props) {
        super(props)
        this.handleLogout = this.handleLogout.bind(this)
    }

    handleLogout(e) {
        e.preventDefault()
        this.props.userLogout()
    }

    render() {
        const { isLoggedIn } = this.props;

        const externalNav = isLoggedIn ? ( null ): (
            <Nav.Link as={ Link } to="/login/">Login</Nav.Link>
        )

        return (
            <Navbar collapseOnSelect expand="lg" bg="light">
                <div className='container d-flex flex-column flex-md-row justify-content-between'>
                    <Navbar.Brand as={ Link } to="/">sleeknotes</Navbar.Brand>
                    <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                    <Navbar.Collapse id="responsive-navbar-nav">
                        <Nav className="mr-auto">
                            <PrivateLink isLogin={isLoggedIn}>
                                    <Nav.Link as={Link} to="/notes/">Notes</Nav.Link>
                                    <Nav.Link as={Link} to="/explore/">Explore</Nav.Link>
                                    <Nav.Link as={Link} to='/teams/'>Teams</Nav.Link>
                            </PrivateLink>
                            </Nav>
                        <Nav>
                            <PrivateLink isLogin={isLoggedIn}>
                                <Nav.Link as={Link} to="/logout/" onClick={ this.handleLogout }>Log out</Nav.Link>
                            </PrivateLink>
                            {externalNav}
                        </Nav>
                    </Navbar.Collapse>
                </div>
            </Navbar>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        isLoggedIn: state.auth.isLoggedIn
    }
}

const mapDispatchToProps = dispatch => ({
    userLogout: () => dispatch(userLogout())
})

export default connect(mapStateToProps, mapDispatchToProps)(Header)