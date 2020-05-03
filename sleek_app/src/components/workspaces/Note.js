import React, { Component } from 'react'

import Card from 'react-bootstrap/Card'

class Note extends Component {
    render() {
        const { note } = this.props;
        return (
            <Card bg='light'>
              <Card.Body>{ note.text.substring(0,200) }</Card.Body>
            </Card>
        )
    }
}

export default Note;
