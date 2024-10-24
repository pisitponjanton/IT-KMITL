/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
      },
      backgroundImage:{
        p: "url('/img/p.png')",
        cl: "url('/img/cl.png')",
        set: "url('/img/set.png')",
        food: "url('/img/food.png')",
        l: "url('/img/l.png')",
        dod: "url('/img/dod.png')",
        c3: "url('/img/c3.png')",
        c3_2: "url('/img/c3-2.png')",
        c4: "url('/img/c4.png')",
        f4:"url('/img/img-1/f4.png')",
        bgr:"url('/img/bgr.png')",
        icon:"url('/img/icon.png')",
        img1:"url('/img/img-1/image1.png')",
        img2:"url('/img/img-1/image2.png')",
        img11:"url('/img/img-2/image1.png')",
        van:"url('/img/img-3/van.png')",
        bb: 'linear-gradient(135deg, #031420 73%, #07273D 100%)',
        bb1: 'linear-gradient(90deg, #102A46 0%, #1A4472 51%,#102A46 100%)',
        bb2: 'linear-gradient(180deg, #073575 0%,#ACACAC 100%)',
        bb3: 'linear-gradient(90deg, #2D5E93 3%,#102A46 72%)',
      },
      fontFamily: {
        'inter-r': ['inter-r', 'sans-serif'],
        'krona-r': ['krona-r', 'sans-serif'],
      },
      keyframes: {
        sp1: {
          '0%': { transform: 'rotate(0deg)' },
          '100%': { transform: 'rotate(360deg)' },
        },
        scale: {
          '0%': { transform: 'translateX(-100vw)' },
          '100%': { transform: 'translateX(0vw)' },
        },
        scale1: {
          '0%': { transform: 'translateX(100vw)' },
          '100%': { transform: 'translateX(0vw)' },
        },
      },
      animation:{
        sp1: 'sp1 1s ease-in-out',
        scale:'scale 0.8s ease-in-out',
        scale1:'scale1 0.6s ease-in-out',
      }
    },
  },
  plugins: [],
};
