import bskyLogo from './assets/beacon.svg'
import Grid from '@mui/material/Grid';
import {BasicCard} from './components/BasicCard'
import './App.css'
import Typography from '@mui/material/Typography';
import { createClient } from "@supabase/supabase-js";
import { useEffect } from 'react';

const supabase = createClient(
  import.meta.env.VITE_PUBLIC_SUPABASE_URL,
  import.meta.env.VITE_PUBLIC_SUPABASE_ANON_KEY
);

function App() {
  useEffect(() => {
    getCountries();
  }, []);

  async function getCountries() {
    const { data, error } = await supabase.from("posts").select('*');
    console.log(data, error);
  }

  return (
    <>
      <div>
        <img src={bskyLogo} alt="BlueSky logo" />
        <Typography>
          Beacon
        </Typography>
      </div>
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
    </>
  )
}

export default App
