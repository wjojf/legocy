import React, {Component} from "react"
import HomeService from './HomeService'


const homeService = new HomeService();


class HomeList extends Component {

    constructor(props) {
        super(props);
        this.state = {
            sets: [],
            nextPageURL: ''
        };
        this.nextPage = this.nextPage.bind(this);
        this.handleDelete = this.handleDelete.bind(this)
    }

}

export default HomeList;