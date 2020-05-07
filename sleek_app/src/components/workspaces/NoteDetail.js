import React from 'react'
import Modal from 'react-bootstrap/Modal'
import ReactMarkdown from 'react-markdown/with-html'

const NoteDetail = (props) => {
    const handleClose = props.onClose
    const { note } = props

    const noteDetail = note ? (
      <ReactMarkdown
            source={ note.text }
            escapeHtml={false}
            />
    ) : null

    const noteChannel = note ? (
      <small className="text-muted">Last updated 3 mins ago  &middot; <strong>{ note.channel.name }</strong></small>
    ) : null

    return (
        <Modal show={props.show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Note Detail</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          { noteDetail }
        </Modal.Body>
        <Modal.Footer>
          { noteChannel }
        </Modal.Footer>
      </Modal>
    )
}

export default NoteDetail