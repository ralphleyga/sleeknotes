import React, { Component } from 'react'
import { connect } from 'react-redux'

import NoteList from './NoteList'

class Feeds extends Component {
    render() {
        return (
            <div>
                <h1>Notes</h1>
                <p>You followed and created notes</p>
                
                <div className="card-columns">
                    <NoteList notes={this.props.notes} />
                </div>
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