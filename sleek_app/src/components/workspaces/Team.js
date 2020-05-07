import React, { Component } from 'react'
import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button'
import Accordion from 'react-bootstrap/Accordion'
import ListGroup from 'react-bootstrap/ListGroup'

class Team extends Component {
    render() {
        const { workspace } = this.props
        const users = workspace.users.map(user => {
            return (
                <ListGroup.Item key={user.id}>{ user.username }</ListGroup.Item>
            )
        })
        return (
            <Card>
                <Card.Header>
                <Accordion.Toggle as={Button} variant="link" eventKey={workspace.id}>
                    { workspace.name }
                </Accordion.Toggle>
                </Card.Header>
                <Accordion.Collapse eventKey={workspace.id}>
                <Card.Body>
                    <ListGroup variant="flush">
                        { users }
                    </ListGroup>
                </Card.Body>
                </Accordion.Collapse>
            </Card>
        )
    }
}

export default Team