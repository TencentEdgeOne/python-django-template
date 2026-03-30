import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Django + EdgeOne Pages",
  description: "Deploy Django applications as serverless functions on EdgeOne Pages. The web framework for perfectionists with deadlines.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en-US">
      <head>
        <link rel="icon" href="/django-favicon.svg" />
      </head>
      <body
        className="antialiased"
      >
        {children}
      </body>
    </html>
  );
}
