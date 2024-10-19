#dictionary of the top 50 instagram account in the world
# Creating the list of dictionaries for the first 50 Instagram accounts
ig_dict = [
    {"name": "Cristiano Ronaldo",
     "country": "Portugal",
     "description": "Footballer sharing personal life and sponsorship posts",
     "follower count": 600},

    {"name": "Lionel Messi",
     "country": "Argentina",
     "description": "Footballer sharing sports highlights and personal life",
     "follower count": 490},

    {"name": "Selena Gomez",
     "country": "United States",
     "description": "Singer, actress, and mental health advocate",
     "follower count": 430},

    {"name": "Kylie Jenner",
     "country": "United States",
     "description": "Entrepreneur and reality TV star with lifestyle and fashion content",
     "follower count": 400},

    {"name": "Dwayne Johnson",
     "country": "United States",
     "description": "Actor and former wrestler, focusing on fitness and motivational content",
     "follower count": 396},

    {"name": "Kim Kardashian",
     "country": "United States",
     "description": "Reality TV star, entrepreneur, and influencer",
     "follower count": 380},

    {"name": "Ariana Grande",
     "country": "United States",
     "description": "Singer and actress",
     "follower count": 370},

    {"name": "Beyoncé",
     "country": "United States",
     "description": "Musician, producer, and actress",
     "follower count": 300},

    {"name": "Khloé Kardashian",
     "country": "United States",
     "description": "Reality TV star and entrepreneur",
     "follower count": 315},

    {"name": "Justin Bieber",
     "country": "Canada",
     "description": "Singer and musician",
     "follower count": 290},

    {"name": "Kendall Jenner",
     "country": "United States",
     "description": "Model and reality TV star",
     "follower count": 292},

    {"name": "Taylor Swift",
     "country": "United States",
     "description": "Singer and songwriter",
     "follower count": 280},

    {"name": "Nike",
     "country": "United States",
     "description": "Sportswear brand sharing fitness, athletes, and products",
     "follower count": 320},

    {"name": "National Geographic",
     "country": "United States",
     "description": "Media organization focusing on nature, science, and culture",
     "follower count": 280},

    {"name": "Virat Kohli",
     "country": "India",
     "description": "Cricketer sharing sports updates and personal life",
     "follower count": 260},

    {"name": "Jennifer Lopez",
     "country": "United States",
     "description": "Singer, actress, and dancer",
     "follower count": 250},

    {"name": "Kourtney Kardashian",
     "country": "United States",
     "description": "Reality TV star and entrepreneur",
     "follower count": 220},

    {"name": "Real Madrid",
     "country": "Spain",
     "description": "Football club sharing team updates and match highlights",
     "follower count": 162},

    {"name": "Rihanna",
     "country": "Barbados",
     "description": "Singer and entrepreneur focusing on beauty, fashion, and music",
     "follower count": 150},

    {"name": "Billie Eilish",
     "country": "United States",
     "description": "Singer and songwriter with personal and mental health-focused content",
     "follower count": 110},

    {"name": "Shakira",
     "country": "Colombia",
     "description": "Musician and philanthropist",
     "follower count": 90},

    {"name": "Priyanka Chopra",
     "country": "India",
     "description": "Actress and producer sharing Bollywood, Hollywood, and personal life",
     "follower count": 91},

    {"name": "Dua Lipa",
     "country": "United Kingdom",
     "description": "Singer-songwriter with posts on her music, fashion, and lifestyle",
     "follower count": 88},

    {"name": "David Beckham",
     "country": "United Kingdom",
     "description": "Former footballer, sharing family life and sports-related content",
     "follower count": 88},

    {"name": "Chris Brown",
     "country": "United States",
     "description": "Singer and dancer with content on music, dance, and art",
     "follower count": 145},

    {"name": "Drake",
     "country": "Canada",
     "description": "Rapper and entrepreneur sharing insights into his career and personal life",
     "follower count": 146},

    {"name": "FC Barcelona",
     "country": "Spain",
     "description": "Football club with updates on matches and players",
     "follower count": 130},

    {"name": "UEFA Champions League",
     "country": "Europe",
     "description": "Football competition posting match highlights and behind-the-scenes content",
     "follower count": 115},

    {"name": "Gal Gadot",
     "country": "Israel",
     "description": "Actress known for her role as Wonder Woman, sharing film and advocacy content",
     "follower count": 108},

    {"name": "Vin Diesel",
     "country": "United States",
     "description": "Actor famous for the Fast & Furious series, sharing personal and motivational posts",
     "follower count": 102},

    {"name": "NASA",
     "country": "United States",
     "description": "Space agency sharing scientific and space exploration content",
     "follower count": 97},

    {"name": "Kylian Mbappé",
     "country": "France",
     "description": "Footballer with sports highlights and personal life posts",
     "follower count": 122},

    {"name": "Ellen DeGeneres",
     "country": "United States",
     "description": "Comedian and talk show host sharing personal life and celebrity interviews",
     "follower count": 140},

    {"name": "Kevin Hart",
     "country": "United States",
     "description": "Comedian and actor sharing funny moments and personal life",
     "follower count": 179},

    {"name": "Katy Perry",
     "country": "United States",
     "description": "Pop singer known for vibrant content, music, and philanthropy",
     "follower count": 200},

    {"name": "Zendaya",
     "country": "United States",
     "description": "Actress and fashion icon sharing film projects and personal moments",
     "follower count": 180},

    {"name": "LeBron James",
     "country": "United States",
     "description": "Basketball player sharing sports and personal life content",
     "follower count": 170},

    {"name": "Snoop Dogg",
     "country": "United States",
     "description": "Rapper and entrepreneur sharing music, humor, and personal life",
     "follower count": 90},

    {"name": "Alia Bhatt",
     "country": "India",
     "description": "Actress sharing Bollywood updates and personal moments",
     "follower count": 85},

    {"name": "Shraddha Kapoor",
     "country": "India",
     "description": "Bollywood actress with posts on film projects and personal life",
     "follower count": 93},

    {"name": "Neymar Jr.",
     "country": "Brazil",
     "description": "Footballer posting highlights of his career and personal life",
     "follower count": 210},

    {"name": "Adele",
     "country": "United Kingdom",
     "description": "Singer-songwriter sharing personal insights and music updates",
     "follower count": 60},

    {"name": "Lady Gaga",
     "country": "United States",
     "description": "Singer and actress advocating for mental health and unique fashion",
     "follower count": 56},

    {"name": "Tom Holland",
     "country": "United Kingdom",
     "description": "Actor best known for Spider-Man, sharing movie promotions and personal adventures",
     "follower count": 65},

    {"name": "Kylie Cosmetics",
     "country": "United States",
     "description": "Beauty brand by Kylie Jenner with vibrant product displays",
     "follower count": 70},

    {"name": "Emma Watson",
     "country": "United Kingdom",
     "description": "Actress and UN Women ambassador advocating for gender equality",
     "follower count": 74},

    {"name": "Leonardo DiCaprio",
     "country": "United States",
     "description": "Actor and environmental activist raising awareness about climate change",
     "follower count": 61},

    {"name": "Gigi Hadid",
     "country": "United States",
     "description": "Model sharing runway moments, fashion shoots, and personal life",
     "follower count": 78},

    {"name": "Jennifer Aniston",
     "country": "United States",
     "description": "Actress sharing nostalgic throwbacks and updates on her current projects",
     "follower count": 45},

    {"name": "Ayr",
     "country": "United States",
     "description": "Unique fashion brand known for its artistic photo styles and creativity",
     "follower count": 100},
]


# # used to check and see how many items are within our above list.
# apperances = 0 

# for x in ig_dict:
#     apperances += 1
# print(apperances)

# # checks to see if we have any duplicate entries
# for x in ig_dict:
#     if ig_dict.count(x) > 1:
#         print(x)