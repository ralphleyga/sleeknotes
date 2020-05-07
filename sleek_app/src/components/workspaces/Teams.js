import React, { Component } from 'react'
import Accordion from 'react-bootstrap/Accordion'
import { connect } from 'react-redux'

import Team from './Team'

class Teams extends Component {
    render() {
        const workspaces = this.props.workspaces ? (
            this.props.workspaces.map(workspace => {
                return (
                    <Team key={workspace.id} workspace={workspace} />
                )
            })
        ) : []
        

        return (
            <div className='mt-4'>
                <h1>Teams</h1>

                <Accordion defaultActiveKey="0">
                    { workspaces }
                </Accordion>
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        workspaces: state.noteReducer.workspaces,
    }
}

export default connect(mapStateToProps)(Teams);
