const initState = {
    notes: [],
    workspaces: [],
    next_notes_result: null,
}

const noteReducer = (state = initState, action) => {
    switch (action.type) {
        case 'FETCH_NOTES':
            return {
                ...state,
                notes: [
                    ...state.notes,
                    ...action.payload.results
                ],
                next_notes_result: action.payload.next
            }
        case 'FETCH_WORKSPACE':
            return {
                ...state,
                workspaces: action.payload.results
            }
        default:
            return state
    }
}

export default noteReducer
