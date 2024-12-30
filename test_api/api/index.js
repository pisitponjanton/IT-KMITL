const multer = require("multer");
const { spawn } = require("child_process");
const path = require("path");
const fs = require("fs");

const storage = multer.diskStorage({
  destination: "/tmp/uploads/",
  filename: (req, file, cb) => {
    cb(null, `${file.fieldname}-${Date.now()}${path.extname(file.originalname)}`);
  },
});

const upload = multer({ storage }).single("file");

const testCases = {
  0: ["21\n", "11\n", "-1\n", "100\n", "101\n"],
  1: ["10\n", "20\n", "30\n"],
};

const expectedOutputs = {
  0: ["False", "False", "False", "True", "False"],
  1: [
    "10 9 8 7 6 5 4 \n3 2 1",
    "20 19 18 17 16 15 14 \n13 12 11 10 9 8 7 \n6 5 4 3 2 1",
    "30 29 28 27 26 25 24 \n23 22 21 20 19 18 17 \n16 15 14 13 12 11 10 \n9 8 7 6 5 4 3 \n2 1",
  ],
};

const deleteFile = (filePath) => {
  fs.unlink(filePath, (err) => {
    if (err) console.error(`Error deleting file: ${err}`);
  });
};

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  upload(req, res, async (err) => {
    if (err) return res.status(500).json({ error: "File upload failed" });

    const filePath = req.file.path;
    const caseIndex = +req.body.case - 1;

    if (!testCases[caseIndex]) {
      deleteFile(filePath);
      return res.status(400).json({ error: "ยังไม่มีข้อนี้เว้ย!!!" });
    }

    const inputs = testCases[caseIndex];
    const expected = expectedOutputs[caseIndex];
    const results = [];

    for (const input of inputs) {
      try {
        const output = await new Promise((resolve, reject) => {
          const pythonProcess = spawn("python3", [filePath]);
          let result = "";

          pythonProcess.stdin.write(input);
          pythonProcess.stdin.end();

          pythonProcess.stdout.on("data", (data) => {
            result += data.toString();
          });

          pythonProcess.stderr.on("data", (data) => {
            reject("Error");
          });

          pythonProcess.on("close", (code) => {
            if (code === 0) resolve(result.trim());
            else reject("Error");
          });
        });

        results.push(output);
      } catch {
        results.push("Error");
      }
    }

    deleteFile(filePath);

    let incorrectCount = 0;
    results.forEach((output, index) => {
      if (output !== expected[index]) incorrectCount += 1;
    });

    const message =
      incorrectCount === 0
        ? "ถูกหมดแล้วว"
        : `ไม่ถูก ${incorrectCount} เคส จาก ทั้งหมด ${expected.length}`;

    res.json({ message, results });
  });
}
