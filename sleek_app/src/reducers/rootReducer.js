import { combineReducers } from 'redux'

import authReducer from './authReducer'
import noteReducer from './notesReducer'

const rootReducer = combineReducers({
    auth: authReducer,
    noteReducer: noteReducer
})

export default rootReducer