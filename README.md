[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=10869979)
# final-project
A template for final projects

Final Project update 4/21/2023

In this week's update I wanted to give you an idea about SCRAPERS I am doing. Originally when I submitted my proposal, I told you I was originally going to do just national polls for political parties and candidates. Well, two major updates happened in the past day:

1: Alberto Fernandez, the incumbent president of Argentina decided NOT to run for re-election which is going to cause seismic shifts in polling averages for both political parties and canddiates themselves. Fernandez was NOT LIKED among Argentines, and him leaving the scene means his party actually has a chance now to win re-election with a new candidate. I am interested to see how this announcement impacts polling averages over the next months before the primaries in August. 

2: I found a wikipedia page: https://es.wikipedia.org/wiki/Elecciones_provinciales_de_Argentina_de_2023 which gives me all the dates, and links to ALL the provincial elections in Argentina that are happening this year. While provincial elections in Argentina aren't required to happen on the same day as the presidential election, they're still a pretty good indicator of people's voting intentions for a national aspect and I think I can now include these things in a map!
After a careful reading of each province's pages, I can get polling numbers for a map for PROVINCIAL elections for these provinces:

1) Buenos Aires Province
2) Autonomous City of Buenos Aires
3) Cordoba
4) Jujuy
5) La Pampa
6) Mendoza 
7) Salta
8) San Juan
9) San Luis
10) Santa Fe
11) Tucumán

11/23 provinces and the city of Buenos Aires I can get on a map. Two of the provinces: Neuquen, and Rio Negro, already had their provincial elections on April 16, so I guess I could also display the results of that on a map... if I can figure it out.

So where doeos that leave me? For the next several days and possible week(s) I will need to basically make 11 different scrapers for all those provinces + the city to get those polling numbers on a CSV, which I can then get into a datasette... which I can then make into graphs, maps, etc and display on a website.

Along with that, I need to go back in and make sure my original scraper and modified to scrape from the Spanish wikipedia page and not the english page since that page is more accurate and updated regularly. I also need to make a scraper for the candidates section of the page too to get actual candidates instead of just party numbers.

A lot of scrapers basically. 

That is where I stand now. I don't have much code to present you aside from the scrape.py file I made, and a test_scrape.py file I'm using to test scraping codes for candidates. I will have much more for you next week. 

Any guidance here is always appreciated. I do feel I'm going a little over my head, but now that I know what my data is and I have provincial date, which I thought I'd never get, I think I can really make a good website..... Its just going to take a long time to make as I don't know half of what I'm doing. 

Chat GPT will help me, so far, I've just been asking it to adjust scraping codes for the time being. 
