import axios from "axios";

const checkUser = (handle) => {
    return axios.get(`http://localhost:5000/view/?q=${handle}`)
}

export {
    checkUser
}