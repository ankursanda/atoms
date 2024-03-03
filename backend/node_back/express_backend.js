const express = require("express");
const bodyParser = require('body-parser');
const axios = require('axios');


const app = express()
const PORT = process.env.PORT || 3000;

app.get("/",(req,res,next)=>{
    res.send("The server is Running")
})

app.get("/api/crawl/:id",async(req,res,next)=>{
    try {
        const instr = req.params.id;
        const response = await axios.get(`http://localhost:8000/api/process/${instr}`);
        res.json(response.data);
    } catch (error) {
        console.error('Error processing data:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
})

app.listen(PORT, ()=>{
    console.log(`The server is listening to port ${PORT}`);
})

