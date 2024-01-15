import pandas as pd

users = pd.read_csv('users.dat', header=None, delimiter='::', engine='python',
                    names='UserID::Gender::Age::Occupation::Zip-code'.split('::'))


ratings = pd.read_csv('ratings.dat', header=None, delimiter='::', engine='python',
                      names='UserID::MovieID::Rating::Time'.split('::'))

movies = pd.read_csv('movies.dat', header=None, delimiter='::', engine='python',
                      encoding='ISO-8859-1', names='MovieID::Title::Genres'.split('::'))


movies = pd.merge(movies, pd.merge(users, ratings))
print(movies)

