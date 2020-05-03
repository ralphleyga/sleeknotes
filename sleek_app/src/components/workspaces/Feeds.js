import React, { Component } from 'react'

import NoteList from './NoteList'

class Feeds extends Component {
    render() {
        return (
            <div>
                <h1>Feeds</h1>
                <div className='row mt-4'>
                    <NoteList />
                </div>
            </div>
        )
    }
}

export default Feeds;