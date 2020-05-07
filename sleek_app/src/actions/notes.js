import axios from 'axios'

export const notesFetch = () => {
    return async dispatch => {
        let resp = await axios.get('notes')
        return dispatch({type: 'FETCH_NOTES', payload: resp.data})
    }
}

export const paginateNotesFetch = (nextUrl) => {
    return async dispatch => {
        let resp = await axios.get(nextUrl)
        return dispatch({type: 'FETCH_NOTES', payload: resp.data })
    }
}

export const workspaceFetch = () => {
    return async dispatch => {
        let resp = await axios.get('workspaces')
        return dispatch({type: 'FETCH_WORKSPACE', payload: resp.data})
    }
}