import logo from './logo.svg';
import './App.css';
import Table from "./components/Table";
import axios from "axios";
import React from "react";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.url = 'http://127.0.0.1:8000'
        this.state = {
            users: [],
            questions: [],
        }
    }

    loadData() {
        axios.get(`${this.url}/api/questions/`)
            .then(response => {
                this.setState({
                    questions: response.data,
                })
            }).catch(error => {
                console.log(error);
                this.setState({
                    questions: []
                })
        })
        axios.get(`${this.url}/api/users/`)
            .then(response => {
                this.setState({
                    users: response.data,
                })
            }).catch(error => {
                console.log(error);
                this.setState({
                    users: []
                })
        })
    }

    componentDidMount() {
        this.loadData();
    }
    render() {
        return (
            <div className="content">
                <Table questions={this.state.questions} users={this.state.users}/>
            </div>
        );
    }
}

export default App;
