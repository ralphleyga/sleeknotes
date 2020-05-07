import React, { Component } from 'react'
import { connect } from 'react-redux'
import CardColumns from 'react-bootstrap/CardColumns'

import NoteList from './NoteList'
import { paginateNotesFetch } from '../../actions/notes'

class Feeds extends Component {

    constructor(props) {
        super(props)
        this.handlePaginate = this.handlePaginate.bind(this)
    }

    handlePaginate(url) {
        this.props.paginate_notes(url)
    }

    render() {
        const { notes, next_notes_result } = this.props;
        let next = () => {
                if (next_notes_result) {
                    return (<button type="button" className='btn btn-info' onClick={() => this.handlePaginate(next_notes_result)}>More</button>)
                } else {
                    return null
                }
            }

        return (
            <div>
                <h1>Notes</h1>
                <p>You followed and created notes</p>
                
                <CardColumns>
                    <NoteList notes={notes} />
                </CardColumns>
                
                <div className='text-center mt-2 mb-4'>
                    { next() }
                </div>

            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        notes: state.noteReducer.notes,
        next_notes_result: state.noteReducer.next_notes_result
    }
}

const mapDispatchToProps = dispatch => ({
    paginate_notes: url => dispatch(paginateNotesFetch(url))
})

export default connect(mapStateToProps, mapDispatchToProps)(Feeds);