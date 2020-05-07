import React, { Component } from 'react'

import Note from './Note'
import NoteDetail from './NoteDetail'

class NoteList extends Component {
    constructor(props) {
        super(props)
        this.handleModalClose = this.handleModalClose.bind(this)
        this.handleModalOpen = this.handleModalOpen.bind(this)

        this.state = {
            modalState: false,
            note: null
        }
    }

    handleModalOpen(e, note) {
        e.preventDefault()
        this.setState({
            ...this.state,
            modalState: true,
            note: note,
        })
    }

    handleModalClose() {
        this.setState({
            ...this.state,
            modalState: false,
        })
    }

    render() {
        const notesList = this.props.notes ? (
            this.props.notes.map(note => {
                return (<Note note={note} key={note.id} open={this.handleModalOpen} close={this.handleModalClose} />)
            })
        ) : (null)
        return (
            <>
                { notesList }
                <NoteDetail show={this.state.modalState} note={this.state.note} onClose={this.handleModalClose} />
            </>
        )
    }
}

export default NoteList;