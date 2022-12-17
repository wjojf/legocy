import axios from 'axios';
const API_URL = 'http://localhost:8000/api/v1';


export default class HomeService {

    constructor(){}

    
    getSets(){
        const url = `${API_URL}/sets/`;
        return axios.get(url).then(response => response.data);
    }


    getSet(pk){
        const url = `${API_URL}/sets/${pk}`;
        return axios.get(url).then(response => response.data);
    }

}