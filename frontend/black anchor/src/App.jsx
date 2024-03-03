import { useState } from 'react'
import Navbar from './components/Navbar'
import Search_card from './components/Search_card'
import Results from './components/Results'
import styles from './styles/App.module.css'

function App() {
  const [result, setResult] = useState([])
  const [value,setValue] = useState("")
  const handleClick = (e) =>{
    e.preventDefault();
    
  }
  return (
    
    <>
    <div className={styles.nav}>
      <Navbar/>
    </div>
    <div className={styles.contain}>
      <Search_card handleClick={handleClick} value={value} setValue={setValue} />
      <Results />
    </div>
    </>
  )
}

export default App
