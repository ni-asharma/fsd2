import { MenuItem, Select, InputLabel, FormControl } from '@mui/material';

export default function MySelect() {
  return (
    <FormControl fullWidth margin="normal">
      <InputLabel>Course</InputLabel>
      <Select>
        <MenuItem value="cse">CSE</MenuItem>
        <MenuItem value="ai">AI</MenuItem>
        <MenuItem value="ds">Data Science</MenuItem>
      </Select>
    </FormControl>
  );
}
