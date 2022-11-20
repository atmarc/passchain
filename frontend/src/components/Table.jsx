import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { IconButton } from "@mui/material";
import Button from "./Button";
import { useRef } from 'react';


export default function BasicTable({ userData, setUserData, user, refreshTable }) {

    const newUser = useRef();
    const newPassword = useRef();

    function refreshTable() {
        fetch("http://localhost:5000/getData", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                "login": user.login,
                "password": user.password
            }),
            redirect: "follow"
        })
            .then(res => res.json()).then(res => {
                setUserData(res["data"])
                console.log(res["data"])
            })
    }

    function addPassHandler() {
        var body_data = {
            "login": user.login,
            "master_password": user.password,
            "username": newUser.current.value,
            "user_password": newPassword.current.value,
        }

        console.log(body_data)

        fetch("http://localhost:5000/createData", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(body_data),
            redirect: "follow"
        })

            .then(res => {
                console.log(res);
                refreshTable();
            })

        newUser.current.value = ""
        newPassword.current.value = ""
    }

    return (
        <div>
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
            <Button styles={`mt-10`} text={"Add data"} onClick={addPassHandler} />
            <br />
            <input type="username" ref={newUser} />
            <br />
            <br />
            <input type="password" ref={newPassword} />

        </div>
    );
}