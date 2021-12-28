import React from 'react';
import c from "./QuestionForm.module.css";

class QuestionForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            creationDate: '',
            title: '',
            author: '',
            isAnswered: '',
            link: ''
        }
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value})
    }

    handleSubmit(event) {
        this.props.createNote(this.state.creationDate,
            this.state.title, this.state.author,
            this.state.isAnswered,
            this.state.link);
        this.setState({
            creationDate: '',
            title: '',
            author: '',
            isAnswered: '',
            link: ''
        })
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={event => this.handleSubmit(event)}>
                <div className={c.table}>
                    <div className={`${c.row} ${c.header}`}>
                        <div className={c.column}>Creation date</div>
                        <div className={c.column}>Title</div>
                        <div className={c.column}>Author</div>
                        <div className={c.column}>Answered?</div>
                        <div className={`${c.column} ${c.last}`}>Link</div>
                    </div>
                    <div className={c.row}>
                        <div className={c.column}>
                            <input type='date' name='creationDate' value={this.state.creationDate} onChange={event => this.handleChange(event)}/>
                        </div>
                        <div className={c.column}>
                            <input type='text' name='title' value={this.state.title} onChange={event => this.handleChange(event)}/>
                        </div>
                        <div className={c.column}>
                            <input type='text' name='author' value={this.state.author} onChange={event => this.handleChange(event)}/>
                        </div>
                        <div className={c.column}>
                            <input type='radio' name='isAnswered' value='Yes' onChange={event => this.handleChange(event)}/>Yes
                            <input type='radio' name='isAnswered' value='No' onChange={event => this.handleChange(event)}/>No
                        </div>
                        <div className={`${c.column} ${c.last}`}>
                            <input type='url' name='link' value={this.state.link} onChange={event => this.handleChange(event)}/>
                        </div>
                    </div>
                    <button type='submit'>Save</button>
                </div>

            </form>
    )
    }

}

export default QuestionForm;
