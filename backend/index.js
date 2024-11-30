// index.js
const express = require('express');
const mysql = require('mysql2/promise');
const dotenv = require('dotenv');
const path = require('path');

dotenv.config();

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, '../frontend')));

async function connect() { return await mysql.createConnection({
    host: process.env.DB_HOST,
    port: process.env.DB_PORT,
    user: process.env.DB_USERNAME,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_DATABASE,
    ssl: {
        ca: [process.env.DB_CA_PATH]  // If required, otherwise you can remove this line
    }
});}

const port = process.env.PORT || 4000;

app.post('/update', async (req, res) => {
    const { name } = req.body;

    // CHANGES
    const { user_id } = req.params.user_id; 
    runPythonScript('runnable.py', [user_id], (err, result) => {
        if (err) {
            res.status(500).send(err);
        }
        else {
            res.send("Script ran successfully");
        }
    })

    try {
        const connection = await connect();

        const [result] = await connection.execute(
            'UPDATE `assignments` SET `pinned` = 0 WHERE `assignments`.`name` = ?',
            [name]
        );

        res.json({ success: true, result });
        await connection.end();
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

app.post('/login', async (req, res) => {
    const { name } = req.params.userPass.name;
    const { password } = req.params.userPass.password;
    try {
        const connection = await connect();

        const [result] = await connection.execute(
            'SELECT `user_id` FROM `users` WHERE `name` = ? AND `password` = ?',
            [password, name]
        );
        res.json({ succes: true, result});
        await connection.end();
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
})

app.get('/fetch', async (req, res) => {
    try {
        const connection = await connect();

        const [rows] = await connection.execute(
            'SELECT * FROM `assignments` WHERE `user_id` = 3'
        );

        res.json(rows);
        await connection.end();
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
