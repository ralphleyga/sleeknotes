import React, { Component } from 'react'
import { connect } from 'react-redux'
import CardColumns from 'react-bootstrap/CardColumns'

import NoteList from './NoteList'

class Feeds extends Component {
    render() {
        return (
            <div>
                <h1>Notes</h1>
                <p>You followed and created notes</p>
                
                <CardColumns>
                    <NoteList notes={this.props.notes} />
                </CardColumns>
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        notes: state.noteReducer.notes
    }
}

export default connect(mapStateToProps)(Feeds);