import axios from 'axios'

export const notesFetch = () => {
    return async dispatch => {
        let resp = await axios.get('notes')
        return dispatch({type: 'FETCH_NOTES', payload: resp.data})
    }
}