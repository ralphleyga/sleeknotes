import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import ReactMarkdown from 'react-markdown/with-html'

import Card from 'react-bootstrap/Card'

class Note extends Component {

    render() {
        const { note } = this.props;
        return (
            <Card bg='light' className='p-2'>
                <Card.Body onClick={() => this.props.open(note)} style={{'cursor': 'pointer'}}>
                    <ReactMarkdown
                        source={ note.text.substring(0,400) }
                        escapeHtml={false}
                        />

                    <Card.Text>
                        <small className="text-muted">Last updated 3 mins ago  &middot; <strong>{ note.channel.name }</strong></small>
                    </Card.Text>
                </Card.Body>
            </Card>
        )
    }
}

export default Note;
