import React, { Component } from 'react'
import ReactMarkdown from 'react-markdown/with-html'

import Card from 'react-bootstrap/Card'

class Note extends Component {

    render() {
        const { note } = this.props;
        return (
            <Card bg='light' className='p-2'>
                <Card.Body onClick={(e) => this.props.open(e, note)} style={{'cursor': 'pointer'}} >
                    <div>
                        <ReactMarkdown
                            source={ note.text.substring(0,400) }
                            escapeHtml={false}
                            />
                    </div>

                    <Card.Text>
                        <small className="text-muted">
                        { note.created } ago  &middot; 
                        <strong>{ note.workspace.name }</strong></small>
                    </Card.Text>
                </Card.Body>
            </Card>
        )
    }
}

export default Note;
