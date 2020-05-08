import React, { Component } from 'react'

import { Navbar, Nav, Form, FormControl, Button, NavDropdown } from 'react-bootstrap'


class NoteFilterNav extends Component {
    render() {
        return (
            <Navbar>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto"></Nav>
                    <Form inline>
                        <Form.Control as="select" custom>
                            <option>All Team</option>
                            <option>Following</option>
                            <option>Teams Note</option>
                            <option>4</option>
                            <option>5</option>
                        </Form.Control>

                        <FormControl type="text" placeholder="Keywords..." className="mr-sm-2 ml-1" />
                        <Button variant="outline-success">Search</Button>
                    </Form>
                </Navbar.Collapse>
            </Navbar>
        )
    }
}

export default NoteFilterNav