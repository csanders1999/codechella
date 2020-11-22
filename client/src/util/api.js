import axios from "axios";

const checkUser = (handle) => {
    return axios.get(`http://localhost:5000/view/?q=${handle}`)
}

const results = (handle) => {
    return axios.get(`http://localhost:5000/results/?q=${handle}`)
}


export {
    checkUser,
    results
}