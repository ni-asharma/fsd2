import Checkbox from '@mui/material/Checkbox';
import FormControlLabel from '@mui/material/FormControlLabel';

export default function MyCheckbox() {
  return (
    <FormControlLabel
      control={<Checkbox />}
      label="Accept Terms"
    />
  );
}
