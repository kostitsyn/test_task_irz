import c from "../Table.module.css";

const RowItem = (props) => {
    return (
        <div className={c.row}>
            <div className={c.column}>{props.question.creation_date}</div>
            <div className={c.column}>{props.question.title}</div>
            <div className={c.column}>{props.question.author}</div>
            <div className={c.column}>{props.question.is_answered ? "Yes" : 'No'}</div>
            <div className={`${c.column} ${c.last}`}>{props.question.link}</div>
        </div>
    )
}

export default RowItem;