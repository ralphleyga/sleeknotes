import React, { Component } from 'react'

import Note from './Note'

class NoteList extends Component {
    render() {
        const notesList = this.props.notes.results ? (
            this.props.notes.results.map(note => {
                return (<Note note={note} key={note.id} />)
            })
        ) : (null)
        return (
            <>
                { notesList }
            </>
        )
    }
}

export default NoteList;