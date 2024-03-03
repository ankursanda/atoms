import styles from "../styles/Search.module.css"

function Search_card({handleClick,setValue, value}){
    const handleChange = (e) =>{
        e.preventDefault();
        setValue(e.target.value)
    }

    return(
        <>
            <div className={styles.search_card}>
                <div><form action="submit">
                        <label htmlFor="search"></label>
                        <input type="text" name="search" id={styles.search} onChange={handleChange} value={value}/>
                        <button action="submit" onClick={handleClick} id={styles.btn}>search</button>
                    </form>
                </div>
            </div>
        </>
    )
}

export default Search_card;