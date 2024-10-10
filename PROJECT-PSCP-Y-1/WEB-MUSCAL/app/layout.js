
import "./globals.css";


export const metadata = {
  title: "NPC",
  description: "Generated by create next app",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body
        className={``}>
        {children}
      </body>
    </html>
  );
}
