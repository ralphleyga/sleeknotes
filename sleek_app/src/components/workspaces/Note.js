import React, { Component } from 'react'

import Card from 'react-bootstrap/Card'

class Note extends Component {
    render() {
        return (
            <div class="col-md-4 mb-3">
                <Card className='shadown-sm' bg='light'>
                    <Card.Body>
                        <p className='card-text'>This is some text within a card body.</p>
                        <div className="d-flex align-items-center">
                            <small className="text-muted">Sleek Team</small>
                            &nbsp;&middot;&nbsp;
                            <small className="text-muted">9 mins</small>
                        </div>
                    </Card.Body>
                </Card>
            </div>
        )
    }
}

export default Note;