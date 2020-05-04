import React, { Component } from 'react'
import { connect } from 'react-redux'
import CardColumns from 'react-bootstrap/CardColumns'

import NoteList from './NoteList'
import { paginateNotesFetch } from '../../actions/notes'

class Feeds extends Component {

    constructor(props) {
        super(props)
        this.handlePaginate = this.handlePaginate.bind(this)
        this.counter = 1;
    }

    handlePaginate() {
        this.counter += 1
        this.props.paginate_notes(this.counter)
    }

    render() {
        const { notes } = this.props;
        let next = () => {
                return (<a href='#' onClick={this.handlePaginate}>Next</a>)
            }

        return (
            <div>
                <h1>Notes</h1>
                <p>You followed and created notes</p>
                
                <CardColumns>
                    <NoteList notes={this.props.notes} />
                </CardColumns>
                
                { next() }

            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        notes: state.noteReducer.notes
    }
}

const mapDispatchToProps = dispatch => ({
    paginate_notes: url => dispatch(paginateNotesFetch(url))
})

export default connect(mapStateToProps, mapDispatchToProps)(Feeds);