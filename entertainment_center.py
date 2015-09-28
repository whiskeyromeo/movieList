import media
import fresh_tomatoes

GoodBadAndUgly = media.Movie("The Good, the Bad, and the Ugly",
                       "Bounty hunters and outlaws collide in this search for hidden gold at the end of the civil war",
                       "http://www.gstatic.com/tv/thumb/movieposters/4161/p4161_p_v7_aa.jpg",
                       "https://www.youtube.com/watch?v=WCN5JJY_wiA",
                       "Sergio Leone",
                       "December 29, 1967")

FistfulOfDollars = media.Movie("A Fistful of Dollars",
                       "A mysterious stranger plays two rival factions in a small southwestern town against one another",
                       "http://ia.media-imdb.com/images/M/MV5BMTAzODAxMzg1MzZeQTJeQWpwZ15BbWU3MDgwMzE5ODk@._V1_SY317_CR0,0,214,317_AL_.jpg",
                       "https://www.youtube.com/watch?v=P9NKVLjTioY",
                       "Sergio Leone",
                       "January 18, 1967")

ForAFewDollarsMore = media.Movie("For a Few Dollars More",
                       "Two bounty hunters team up to hunt down a nefarious outlaw",
                       "http://t1.gstatic.com/images?q=tbn:ANd9GcR_LiSBN8YyfJYsSvzJ4zpx5Ha4EDYFtlz3-O8C9ki9jBCNW9tV",
                       "https://www.youtube.com/watch?v=DDRNEwFOttw",
                       "Sergio Leone",
                       "May 10, 1967")

OnceUponATime = media.Movie("Once Upon a Time in The West",
                       "Outlaws battle over a small tract of land in a old southwest boomtown",
                       "http://www.gstatic.com/tv/thumb/movieposters/2803/p2803_p_v7_af.jpg",
                       "https://www.youtube.com/watch?v=MNGQ1hUyx-k",
                       "Sergio Leone",
                       "May 28, 1969")


JoseyWales = media.Movie("The Outlaw Josey Wales",
                       "A man seeks revenge on a Union officer for the murder of his family",
                       "http://t1.gstatic.com/images?q=tbn:ANd9GcSTyddXepXHx0QAmZ1XAe8ylSs0oYVSX4CFcVMXRLUTtdx8ChVV",
                       "https://www.youtube.com/watch?v=en9rfsUGDkc",
                       "Clint Eastwood",
                       "June 26, 1976")

TheWildBunch = media.Movie("The Wild Bunch",
                       "A gang of outlaws go for one last robbery in a changed land",
                       "http://www.gstatic.com/tv/thumb/movieposters/2210/p2210_p_v7_aa.jpg",
                       "https://www.youtube.com/watch?v=aIwH96iZI7E",
                       "Sam Peckinpah",
                       "June 18, 1969")

ButchCassidyAndSundance = media.Movie("Butch Cassidy and the Sundance Kid",
                       "Two outlaws running from death go for riches in a new land",
                       "http://vignette1.wikia.nocookie.net/scratchpad/images/b/bf/Butch_cassidy_and_the_sundance_kid_xlg.jpg/revision/latest?cb=20130829032303",
                       "https://www.youtube.com/watch?v=X41Ylp02NRs",
                       "George Roy Hill",
                       "September 23, 1969")

JeremiahJohnson = media.Movie("Jeremiah Johnson",
                             "A man makes his way in the Rocky Mountains before the west was tame",
                             "http://www.gstatic.com/tv/thumb/movieposters/493/p493_p_v7_aa.jpg",
                             "https://www.youtube.com/watch?v=uzjN8YJt55g",
                             "Sydney Pollack",
                             "December 21, 1972")

DjangoUnchained = media.Movie("Django Unchained",
                              "A freed slave goes after his wife",
                              "http://t3.gstatic.com/images?q=tbn:ANd9GcSnm2FczCxSnt69XUZqqI5-sfy66SvjiV0du9mfUKRRCGqVAurt",
                              "https://www.youtube.com/watch?v=eUdM9vrCbow",
                              "Quentin Tarantino",
                              "December 25, 2012")

BlazingSaddles = media.Movie("Blazing Saddles",
                            "A sheriff and his friend become the only line of defense for a small town",
                            "http://i.jeded.com/i/blazing-saddles.16193.jpg",
                            "https://www.youtube.com/watch?v=VKayG1TrfuE",
                            "Mel Brooks",
                            "February 7, 1974")

TrueGrit = media.Movie("True Grit",
                      "A former lawman and a girl go after the outlaw that murdered her father",
                      "http://t1.gstatic.com/images?q=tbn:ANd9GcQCaz3MfE-t0TpPvW6KXYbk7XE1UWBRbBST46Xgvp9scz8eMHar",
                      "https://www.youtube.com/watch?v=qIJ4OJ1wH3o",
                      "Joel and Ethan Coen",
                      "December 22, 2010")

movie_list = [TrueGrit, BlazingSaddles, DjangoUnchained, ButchCassidyAndSundance, GoodBadAndUgly, OnceUponATime, TheWildBunch,  FistfulOfDollars, ForAFewDollarsMore, JoseyWales, JeremiahJohnson ]



fresh_tomatoes.open_movies_page(movie_list)