import './App.css';
import Table from "./components/Table/Table";
import axios from "axios";
import React from "react";
import QuestionForm from "./components/QuestionForm/QuestionForm";
import Navbar from "./components/Navbar/Navbar";
import {BrowserRouter, Routes, Route} from "react-router-dom";

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

    createNote(creationDate, title, author, isAnswered, link) {
        const data = {
            creation_date: creationDate,
            title: title,
            author: author,
            is_answered: isAnswered,
            link: link
        }
        const headers = {
            'Content-Type': 'application/json'
        }
        axios.post(`${this.url}/api/questions/`, data, {headers: headers})
            .then(response => {
                this.loadData();
            })
    }

    deleteAllNotes() {
        axios.delete(`${this.url}/api/questions/1/`)
            .then(response => {
                console.log('Delete all notes');
                this.loadData();
            })

    }

    componentDidMount() {
        this.loadData();
    }
    render() {
        return (
            <BrowserRouter>
                <div className="content">
                    <Navbar/>
                    <Routes>
                        <Route path='/' element={<QuestionForm createNote={(creationDate, title, author, isAnswered, link) =>
                        this.createNote(creationDate, title, author, isAnswered, link)} />} />
                        <Route path='/table' element={<Table deleteAllNotes={() => this.deleteAllNotes()}
                                                             questions={this.state.questions}/>} />
                    </Routes>
                </div>
            </BrowserRouter>
        );
    }
}

export default App;
