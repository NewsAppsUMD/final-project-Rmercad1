[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=10869979)
# final-project
Argentina 329: An Overview

NOTE: PLEASE GRADE THIS BASED ON ACCESSING THE PAGE THROUGH CODESPACES. GO TO CODE SPACES, OPEN A NEW CODESPACE, CD INTO APPLICATION > WEB_APP, AND THEN RUN “PYTHON APP.PY” OR “FLASK RUN” TO ACCESS PAGE.

Continued attempts at freezing and hosting the page on GitHub Pages did not work and resulted in a bad page you can see here: 

https://newsappsumd.github.io/final-project-Rmercad1/application/web_app/build/index.html

I apologize profusely for bothering you on a Friday night, that was my fault for not managing time correctly, but the app is good on codespaces. Why it won’t display properly on GH pages, I don’t know. Please understand I tried my best with lots of troubleshooting, including your suggestions or re-placing files in separate directories. I do want to get this live on GH pages, we could figure out how to do that later, but, as agreed upon, I need to get this assignment in to you today. Please grade me knowing eventually this will be live, it just needs to go through some troubleshooting.


Introduction: 

This final project’s inspiration was from two websites that I’ve used periodically over the years: 338canada.com, and Nate Silver’s 538. Both websites are very well-made and straightforward web applications giving users a good overview of election polls, predictions, statistics, and projections. It's a great resource for people who want to keep updated with elections and how public opinion is swaying. I wanted to make one for Argentina. The country is going through an important election this year, with the rise of the far-right and decline of traditional political parties. It is important to have a record of this rise to cite back to. The first update of this project was my proposal and how it differed from my bot, which was a full expansional use of the scraping code I made to contribute to a much larger website.

Development efforts:

-Data gathering/ scrapers:
In the data gathering portion of this project, I wanted to utilize the skills and codes I gained from my scraping bot project. Using this method to scrape data for my website was how I wanted to gather and continuously update the data on the eventual website. The second update to this project was my scrapers. As you saw in my blogpost and my updates, my problems with beautiful soup were resolved using pandas. In the end, 13 unique scrapers for 12 different wikipedia pages and 13 different tables were created, all of them still working today. With scrapers produced and CSV’s created with polling data, the next step was the website development.

-Website and HTML development:
The last update of this project was the beginning of HTML development on a flask app for this site. To create the website with the layout that I did, I used the actual homepage HTML of 338canada, pasted it into pastebin, and showed it to chatGPT. I asked Chat GPT if I could create a homepage similar to 338canada for my website, and it delivered. The homepage you see is the result of that. Over the next week I was able to basically teach myself rudimentary HTML, using tags, references, identifiers, links, images, static, etc to add in personalized elements. The last part of this project was the hardest one: embedding data in, and creating separate provincial pages for each province with data.

-Embedding data / provincial pages / realities of working with missing or incomplete data:
Surprisingly finding a way to present my data and create different pages for different regional elections proved to be the hardest part of this project. Finding a method to display my polling data that was easy to produce, visually appealing, and easy to update was hard. At first I tried to display my CSV’s as HTML tables on the pages of my website, but that proved to not only not work, but it looked terrible. I realized that in order to get nice HTML table displays on my website, it would take me weeks to learn more advanced HTML and then get that on my website. And Chat GPT would be no help here either. So, I decided to do a much easier and more reliable method: Datawrapper. DW’s presentable tables are not only easy to make and create, but they’re also easy to update to. If I want to add more data to my table, I can simply just upload a new CSV onto the existing file and replace one number in the existing code on codespaces, and it’s updated. Datawrapper also allows you to use an API in your code to have it manually update its tables on schedules, which I will get more into later. 
Making provincial pages, which may seem to be just cut and pasting of the same code, actually proved hard, partially because all provincial data is not created equally. Some provinces had data but maybe one poll. Others I had to re-work scrapers since the HTML of the page changed within the last two weeks. Others didn’t have any polls at all but I still wanted to present something. So I came up with a solution: Present polling tables for those provinces that have them, and present incumbents that are up for reelection for provinces that have no polling data. That way, all provincial pages have some data of sorts. Each provincial page also has a link to their respective province’s elections or governmental website to help guide the user.

Maintenance:
In keeping with the theme of our last class, what will happen to this election’s website? I imagine its life will end in October or November when the elections are over. Argentina does have midterm elections though, so votes happen every two years, but since this is my first ever election website, I imagine myself closing up the site once things are done to do a serious evaluation of it: what worked, what didn’t, etc, and plan whether I will continue on with other elections the country will hold.

As you will see in the code, unfortunately, the periodic updating of datawrapper hasn’t been able to work. I have tried a lot of troubleshooting, but the problem goes down to the API key. If you look at my candidate_polls.py code (located in scrapers>wikitable), you will see the necessary code is in place, to scrape, save to CSV, access the datawrapper table / file using its API key, and then update the table:

# Update Datawrapper table using the Datawrapper API
    datawrapper_table_id = 'UkZzQ'
    api_key = os.environ['DATAWRAPPERAPI']
    update_url = f'https://api.datawrapper.de/v3/charts/UkZzQ/data'


    # Read the CSV file
    with open(csv_file, 'rb') as file:
        csv_data = file.read()


    # Prepare headers with API key
    headers = {
        'Authorization': api_key,
        'Content-Type': 'text/csv'
    }


    # Make the API request to update the Datawrapper table
    response = requests.put(update_url, headers=headers, data=csv_data)


    # Check the response status
    if response.status_code == 200:
        print('Datawrapper table updated successfully.')
    else:
        print(f'Error updating Datawrapper table. Status code: {response.status_code}')
        print(response.text)


# Schedule the task to run twice a week
schedule.every(3).days.do(scrape_and_update)  # Adjust the interval as needed


# Run the scheduled tasks indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)

The code is sound, but everytime I run it, it errors out saying there's a problem with the API key. The Key itself is legit, I put it as a secret in codespaces and it's listed on my datawrapper account as being able to update tables, but for some reason, it just doesn’t work. This is my biggest regret with this project. I apologize for not presenting you a workable updatable site, but I am out of time and need to turn this in. I will try to meddle with datawrapper’s API function over the coming week to see if this problem can be fixed. According to some, I need to contact Datawrapper to solve this issue as that has worked for some people.

Otherwise, updating the data itself without that is not hard. Like I explained, updating datawrapper and then re-publishing it is very easy, just replacing a “1” with a “2” in the code if I made a second version of a table. 

Example: 
Old: https://datawrapper.dwcdn.net/Ljl9K/embed.js?v=2
New: https://datawrapper.dwcdn.net/Ljl9K/embed.js?v=3


There are 10 tables on the site that need periodic updating. Only 2 (the home page tables) would require constant updating. Provincial polls are few and far between in Argentina. I would not be surprised if the polls up on the my site are the only ones until their province’s election dates in the coming months. Is manually updating datawrapper a lot of work? Somewhat yes, it's not terrible and I would still like my API method to work, but Philippe J. Fournier who runs 338Canada actually doesn't have automatic updates, he manually updates the site himself, leaving update dates, and he does it periodically, but he also dedicates most of his work to it, so it's not a hassle for him. I will manually update my site, twice a week, as I coded with the API update if it worked. When if I get the API to work, I will know updates are successful either from print statements from the code:

  # Check the response status
    if response.status_code == 200:
        print('Datawrapper table updated successfully.')
    else:
        print(f'Error updating Datawrapper table. Status code: {response.status_code}')
        print(response.text)


Conclusion/ final thoughts:

Does this election’s website come close to looking like 338Canada? Somewhat. It takes the template of that website and I’ve made it my own. I am proud of the work I have done, the scrapers I made, and the HTML I've created. This website is on its way to being a valuable resource for people looking to know more about the Argentine elections. If I could change things, I would first try to find another way to present the data. Datawrapper is good, but I think for my purposes I need an HTML table which would take many weeks to learn to code. I simply don’t have time for that for the time constraints for this project. Secondly, my map. A map of dates is nice, but I would have liked my map to be more interactive. I want users to click on their province and that would take them to their province’s page that I painstakingly made. Unfortunately, because its a datawrapper map, I cannot do that. That is another element that I would need to learn to code: an HTML map with interactive clickable links, but again, I don’t have time for that. The graph is also not very well done, I need a javascript graph and I just don’t have that knowledge yet. The graph produced does show trends in polling though, it is readable, just not pleasant to look at. Overall though, I am pleased with this work and I hope you recognize the hard work I put into it. The polling data itself will live on in perpetuity elsewhere I think. Wikipedia pages rarely get erased, and those polling numbers will live there.. This app served as a very good crash course lesson on taking the skills I learned in this class, plus HTML, and skills from 772 and I am very proud of my work. Thank you for teaching me these skills, for allowing me to do a project that aligns with my interests, and for giving me a project that I will honestly probably continue to use over the course of this year as I continue to cover this election. I apologize for the panic attacks and for coming up short in some places, and while I did come up short, I got pretty dang far if you ask me from where I was in September last year. With a few improvements here and there, this website can be fully live and operational soon. 
