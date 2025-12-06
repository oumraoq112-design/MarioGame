const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = 3000;

// Create uploads directory if it doesn't exist
const uploadsDir = path.join(__dirname, 'uploads');
if (!fs.existsSync(uploadsDir)) {
    fs.mkdirSync(uploadsDir);
}

// Configure multer for file uploads
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, uploadsDir);
    },
    filename: (req, file, cb) => {
        // Save with timestamp to keep all screenshots
        const timestamp = Date.now();
        cb(null, `screenshot_${timestamp}.png`);
    }
});

const upload = multer({ storage: storage });

// Serve static files (HTML, CSS, uploaded screenshots)
app.use('/uploads', express.static(uploadsDir));
app.use(express.static(__dirname));

// Endpoint to receive screenshots
app.post('/upload', upload.single('screenshot'), (req, res) => {
    if (!req.file) {
        return res.status(400).send('No file uploaded');
    }
    
    console.log(`[SERVER] Screenshot received: ${req.file.filename}`);
    res.status(200).send('Screenshot received');
});

// Endpoint to get list of all screenshots
app.get('/screenshots', (req, res) => {
    fs.readdir(uploadsDir, (err, files) => {
        if (err) {
            return res.status(500).send('Error reading screenshots');
        }
        
        // Filter only PNG files and sort by timestamp (newest first)
        const screenshots = files
            .filter(file => file.endsWith('.png'))
            .sort((a, b) => {
                const timeA = parseInt(a.match(/\d+/)[0]);
                const timeB = parseInt(b.match(/\d+/)[0]);
                return timeB - timeA;
            })
            .map(file => ({
                filename: file,
                url: `/uploads/${file}`,
                timestamp: new Date(parseInt(file.match(/\d+/)[0]))
            }));
        
        res.json(screenshots);
    });
});

// Serve the main page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
    console.log(`\n========================================`);
    console.log(`Screenshot Server Running`);
    console.log(`========================================`);
    console.log(`Local: http://localhost:${PORT}`);
    console.log(`\nWaiting for screenshots...`);
    console.log(`========================================\n`);
});
