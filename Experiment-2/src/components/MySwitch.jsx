import Switch from '@mui/material/Switch';
import FormControlLabel from '@mui/material/FormControlLabel';

export default function MySwitch() {
  return (
    <FormControlLabel
      control={<Switch />}
      label="Enable Notifications"
    />
  );
}
