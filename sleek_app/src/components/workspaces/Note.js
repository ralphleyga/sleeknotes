import React, { Component } from 'react'
import { Link } from 'react-router-dom'

import Card from 'react-bootstrap/Card'

class Note extends Component {
    render() {
        const { note } = this.props;
        return (
            <Card bg='light' className='p-2'>
                <Card.Body>
                <Link to='/'>{ note.text.substring(0,200) }</Link>

                    <Card.Text>
                        <small className="text-muted">Last updated 3 mins ago</small>
                    </Card.Text>
                </Card.Body>
            </Card>
        )
    }
}

export default Note;
