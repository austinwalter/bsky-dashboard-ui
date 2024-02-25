import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

type BasicCardProps = {
  count: number;
  name: string;
}

export function BasicCard(props: BasicCardProps) {
  return (
    <Card sx={{ minWidth: 60 }}>
    <CardContent>
      <Typography variant="h4" component="div">
        {props.count}
      </Typography>
      <Typography sx={{ mb: 1.5 }} color="text.secondary">
        {props.name}
      </Typography>
    </CardContent>
  </Card>
  );
}
