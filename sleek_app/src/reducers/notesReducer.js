const initState = {
    notes: [],
    next_result: null,
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
                next_result: action.payload.next
            }
        default:
            return state
    }
}

export default noteReducer
