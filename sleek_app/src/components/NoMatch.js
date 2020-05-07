import React, { Component } from 'react'


class NoMatch extends Component {
    render() {
        console.log('nomatch page')
        return (
            <div className='row'>
                <h1>Page not found</h1>
            </div>)
    }
}

export default NoMatch;