import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { IconButton } from "@mui/material";


const user_pw = [{ "email": 'jason.wen@tum.de', "password": 'pw' }, { "email": 'jasonwendavidson@gmail.com', "password": 'pw2' }]
const listItems = user_pw.map((item) =>
    <li>
        {item["email"]}
        {item["password"]}
    </li>
)
const rows = [
    ('Frozen yoghurt', 159, 6.0, 24, 4.0),
    ('Ice cream sandwich', 237, 9.0, 37, 4.3),
    ('Eclair', 262, 16.0, 24, 6.0),
    ('Cupcake', 305, 3.7, 67, 4.3),
    ('Gingerbread', 356, 16.0, 49, 3.9),
];

export default function BasicTable({userData}) {
    return (
        <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
                <TableHead>
                    <TableRow>
                        <TableCell align="left">Email Address</TableCell>
                        <TableCell align="left">Password</TableCell>
                    </TableRow> 
                </TableHead>
                <TableBody>
                    {userData.map((item, index) => (
                        <TableRow
                            key={index}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                        >
                            <TableCell component="th" scope="row">
                                {item["login"]}
                            </TableCell>
                            <TableCell align="left">{item["password"]}</TableCell>
                            <TableCell align="left"><IconButton>Edit</IconButton></TableCell>
                            <TableCell align="left"><IconButton>Delete</IconButton></TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}