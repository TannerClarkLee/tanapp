import axios from 'axios';

const API_URL = 'http://localhost:8080/api/auth/';

export function login(username, password) {

}

export function logout() {
    window.$cookies.remove('token')
}
