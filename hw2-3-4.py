# Author: JD 09/23/2021

population = 332774945

sec = 24 * 60 * 60

birth = sec // 8

death = sec // 12

migra = sec // 645

tomorrow = population + birth - death + migra

print(tomorrow)

