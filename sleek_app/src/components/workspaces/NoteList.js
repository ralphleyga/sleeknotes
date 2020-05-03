import React, { Component } from 'react'

import Note from './Note'

class NoteList extends Component {
    render() {
        return (
            <>
                <Note />
                <Note />
                <Note />
                <Note />
                <Note />
            </>
        )
    }
}

export default NoteList;