import sys

items = [
    ("Power", "dTxpGf8xLEc", "Experiencing the supernatural movement and transformative power of God."),
    ("Presence", "-aHVOiNT_rw", "Cultivating an atmosphere where the Holy Spirit dwells and moves freely."),
    ("People", "5jJnWivD_g8", "Building an authentic community rooted in deep connection and grace."),
    ("Praise", "TccnbhZfUAI", "Lifting up unrestricted, passionate worship that honors our Creator."),
    ("Purpose", "4ADU7BfvpUo", "Equipping every individual to discover and walk in their divine calling.")
]

mobile_html = """   <!-- Mobile Stack Layout (Hidden on Desktop) -->
   <div class="lg:hidden flex flex-wrap justify-center gap-6 px-6 relative z-10 w-full max-w-[1400px] mx-auto">"""

for title, vid, desc in items:
    mobile_html += f"""
     <!-- Card: {title} -->
     <div class="gsap-card-up relative rounded-[2.5rem] overflow-hidden aspect-square w-full sm:w-[calc(50%-0.75rem)] group shadow-xl">
       <div class="absolute inset-0 z-0 overflow-hidden pointer-events-none bg-black">
         <iframe class="absolute top-1/2 left-1/2 w-[185%] max-w-none h-auto aspect-video -translate-x-1/2 -translate-y-1/2" src="https://www.youtube.com/embed/{vid}?autoplay=1&mute=1&controls=0&rel=0&showinfo=0&loop=1&playlist={vid}&end=45&playsinline=1" frameborder="0" allow="autoplay; encrypted-media" tabindex="-1"></iframe>
       </div>
       <div class="absolute inset-0 bg-gradient-to-b from-black/80 via-black/10 to-black/90 pointer-events-none z-10 transition-opacity duration-1000 group-hover:opacity-80"></div>
       <div class="absolute inset-x-8 top-8 z-20 pointer-events-none">
         <h3 class="text-white text-[2.5rem] font-serif tracking-tight leading-none mb-1">{title}</h3>
       </div>
       <div class="absolute inset-x-8 bottom-8 z-20 text-white/90 text-[1.05rem] font-serif italic leading-snug tracking-wide pointer-events-none">
         {desc}
       </div>
     </div>"""

mobile_html += "\n   </div>\n"

desktop_html = """
   <!-- Desktop Infinite Scroll Marquee (Hidden on Mobile) -->
   <!-- Uses inline CSS animation to keep scrolling infinitely -->
   <div class="hidden lg:flex w-full relative z-10 gs-marquee-container opacity-0">
     <style>
       @keyframes infinite-marquee {
         0% { transform: translateX(0%); }
         100% { transform: translateX(-50%); }
       }
       .animate-marquee {
         animation: infinite-marquee 40s linear infinite;
       }
       .animate-marquee:hover {
         animation-play-state: paused;
       }
     </style>
     <!-- Marquee track containing 2 sets of the 5 cards to allow perfect 50% snap -->
     <div class="animate-marquee flex gap-8 whitespace-nowrap min-w-max px-4">
"""

for set_num in [1, 2]:
    desktop_html += f"\n       <!-- Set {set_num} -->\n"
    for title, vid, desc in items:
        desktop_html += f"""       <div class="relative rounded-[2.5rem] overflow-hidden aspect-[4/5] w-[26rem] group shadow-xl shrink-0">
         <div class="absolute inset-0 z-0 overflow-hidden pointer-events-none bg-black">
           <iframe class="absolute top-1/2 left-1/2 w-[235%] max-w-none h-auto aspect-video -translate-x-1/2 -translate-y-1/2" src="https://www.youtube.com/embed/{vid}?autoplay=1&mute=1&controls=0&rel=0&showinfo=0&loop=1&playlist={vid}&end=45&playsinline=1" frameborder="0" allow="autoplay; encrypted-media" tabindex="-1"></iframe>
         </div>
         <div class="absolute inset-0 bg-gradient-to-b from-black/80 via-black/10 to-black/90 pointer-events-none z-10 transition-opacity duration-1000 group-hover:opacity-80"></div>
         <div class="absolute inset-x-10 top-10 whitespace-normal z-20 pointer-events-none">
           <h3 class="text-white text-[3.2rem] font-serif tracking-tight leading-none mb-1">{title}</h3>
         </div>
         <div class="absolute inset-x-10 bottom-10 text-white/90 text-[1.125rem] font-serif italic leading-snug tracking-wide whitespace-normal z-20 pointer-events-none">
           {desc}
         </div>
       </div>\n"""

desktop_html += "     </div>\n   </div>\n  </section>\n\n"

with open("/Users/etosegun/Documents/websites /tent church /index.html", "r") as f:
    text = f.read()

start_marker = "<!-- Mobile Stack Layout (Hidden on Desktop) -->"
end_marker = "<!-- Footer -->"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_text = text[:start_idx] + mobile_html + desktop_html + text[end_idx:]
    with open("/Users/etosegun/Documents/websites /tent church /index.html", "w") as f:
        f.write(new_text)
    print("Success")
else:
    print("Markers not found")
