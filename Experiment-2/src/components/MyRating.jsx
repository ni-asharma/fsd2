import Rating from '@mui/material/Rating';
import Typography from '@mui/material/Typography';

export default function MyRating() {
  return (
    <>
      <Typography>Rate Us</Typography>
      <Rating value={4} />
    </>
  );
}
