import axios from 'axios'


// const api = axios.create({
//     baseURL: 'http://localhost:8002',
// })

// export default api;

// Service for Columns
export const userApi = axios.create({
    baseURL: 'http://localhost:8001',
});

// Service for Boards
export const boardApi = axios.create({
    baseURL: 'http://localhost:8002',
});

// Service for Tasks
export const notiApi = axios.create({
    baseURL: 'http://localhost:8003',
});
