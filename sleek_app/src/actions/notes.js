import axios from 'axios'

export const notesFetch = () => {
    return async dispatch => {
        let resp = await axios.get('notes')
        return dispatch({type: 'FETCH_NOTES', payload: resp.data.results})
    }
}

export const paginateNotesFetch = (number) => {
    return async dispatch => {
        let resp = await axios.get('notes?page=' + number)
        return dispatch({type: 'FETCH_NOTES', payload: resp.data.results })
    }
}