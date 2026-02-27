const puppeteer = require("puppeteer");
require("dotenv").config();

async function loginITKMITL(username, password) {
  const browser = await puppeteer.launch({
    headless: false,
    defaultViewport: null,
  });

  const page = await browser.newPage();

  try {
    await page.goto("https://login.it.kmitl.ac.th", {
      waitUntil: "networkidle2",
    });

    // 🔥 เช็คว่าโดน redirect ไป /status ไหม
    if (page.url().includes("/status")) {
      console.log("⚠️ Redirected to /status → clicking submit first");

      await page.waitForSelector('button[type="submit"]', {
        timeout: 5000,
      });

      await Promise.all([
        page.click('button[type="submit"]'),
        page.waitForNavigation({ waitUntil: "networkidle2" }),
      ]);
    }

    // รอ input โหลด
    await page.waitForSelector('input[name="username"]');

    // กรอกข้อมูล
    await page.type('input[name="username"]', username, { delay: 50 });
    await page.type('input[name="password"]', password, { delay: 50 });

    // กด Enter login
    await Promise.all([
      page.keyboard.press("Enter"),
      page.waitForNavigation({ waitUntil: "networkidle2" }),
    ]);

    console.log("✅ Login attempted");

    return {
      success: true,
      url: page.url(),
      cookies: await page.cookies(),
    };
  } catch (error) {
    console.error("❌ Login error:", error);
    return { success: false, error };
  } finally {
    // ✅ ปิด browser เสมอ
    await browser.close();
  }
}

async function main() {
  const data = await loginITKMITL(process.env.USERNAME, process.env.PASSWORD);
  console.log(data);
}

main();
