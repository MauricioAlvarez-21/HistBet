# HistBet
As mentioned in the description, the following project is a web application that outputs games in which historical trends show a clear favorite winner for each match Day. The predictive algorithm to obtain these results was developed by myself and has been tested on the 2022-2023 season with an average success rate of roughly 80%. While developing HistBet (http://histbet.pythonanywhere.com/) I have:

- Extracted data from a public API (football-data.org), implementing automated timeFrames to overcome the limitations that the API imposed, and organized the data  in different Python data structures 
- Used several nested loops, hand in hand with time constraints to build an algorithm that analyzed the large amounts of data in search of historical trends and results deviation through time.
- Implemented the Flask web Framework to make a web application that retrieved user input through HTTP post requests, and inputted information received into a search engine that combined live API data with our previously extracted and analyzed records. 
- Developed a responsive HTML page that included some graphs made through the use of the chart.js library and JavaScript.
Explore the world of sports prediction with HistBet, where a rigorous data-driven approach, advanced algorithms, and elegant web design converge to offer a formal and reliable forecasting experience. Access HistBet at HistBet to experience the future of sports prediction.
