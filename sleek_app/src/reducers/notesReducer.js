const initState = {
    notes: []
}

const noteReducer = (state = initState, action) => {
    switch (action.type) {
        case 'FETCH_NOTES':
            console.log(action.payload)
            return {
                ...state,
                notes: action.payload
            }
        default:
            return state
    }
}

export default noteReducer
