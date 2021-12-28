import c from './Table.module.css';
import RowItem from "./RowItem/RowItem";

const Table = (props) => {
    let questionsElem = props.questions.map(question => <RowItem question={question} key={question.id}/>)
    return (
        <div className={c.table}>
            <div className={`${c.row} ${c.header}`}>
                <div className={c.column}>Creation date</div>
                <div className={c.column}>Title</div>
                <div className={c.column}>Author</div>
                <div className={c.column}>Answered?</div>
                <div className={`${c.column} ${c.last}`}>Link</div>
            </div>
            {questionsElem}
            <button onClick={event => props.deleteAllNotes()}>Delete all</button>
        </div>
    )
}


export default Table;