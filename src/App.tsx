import bskyLogo from './assets/bsky.svg'
import Grid from '@mui/material/Grid';
import {BasicCard} from './components/BasicCard'
import './App.css'

function App() {
  return (
    <>
      <div>
        <a href="https://react.dev" target="_blank">
          <img src={bskyLogo} className="logo bsky" alt="BlueSky logo" />
        </a>
      </div>
      <h1>Blue Sky Beacon</h1>
      <div className="card">
      <Grid container spacing={2}>
        <Grid item xs={6}>
          <BasicCard name='Post Authors' count={28889}/>
        </Grid>
        <Grid item xs={6}>
          <BasicCard name='Mean Post Count' count={32112}/>
        </Grid>
        <Grid item xs={6}>
          <BasicCard name='Users' count={28889}/>
        </Grid>
        <Grid item xs={6}>
          <BasicCard name='Views' count={348988}/>
        </Grid>
      </Grid>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
