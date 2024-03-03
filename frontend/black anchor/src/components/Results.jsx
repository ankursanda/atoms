import styles from "../styles/Result.module.css"

function Results(){
    return(
        <>
            <div className={styles.results_card}>
                <div className={styles.title}>Alarm</div>
                <div className="categories"></div>
                <div className="results-urls"></div>
            </div>
        </>
    )
}

export default Results;