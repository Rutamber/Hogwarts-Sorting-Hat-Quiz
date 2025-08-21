# Hogwarts Sorting Hat Quiz 🎩🪄
## Harvard CS50P Final Project
#### Video Demo: https://youtu.be/-CJcHYvI6zQ
---
***Hey there! My name is Rutamber and this is my Final Project for Harvard CS50P!***
This is the recreation of the sorting hat that is a part of the *wizarding world* franchise.
In the wizarding world, espescially in **Harry Potter** All the first year students at *Hogwarts School of Witchcraft and Wizardry* would wear this hat on their first day and then the hat will sort them into one of the four hogwarts houses:
1. ***Gryffindor*** 🔴🦁 - *The brave and chivalrous*
2. ***Ravenclaw*** 🔵🦅 - *The Wise and witty*
3. ***Hufflepuff*** 🟡🦡 - *The loyal and kind*
4. ***Slytherin***   🟢🐍 - *The cunning and ambitious*

#### Each of these house are unique and a student can get into only one of these houses.
---
## My Project v. Official Test
My project takes direct inspiration from the sorting process that is available in the *Harry Potter* website, previously called *Pottermore*. In the website, there is not a hat that sorts you but rather the computer does algorithmically by asking you different questions and determine your hogwarts house, my program is CLI version of the same test. However, there are few differences:
1. The official test is graphic intensive whereas my project is only text based. 💻
2. The official test only asks 8 questions per sorting whereas my test asks 15 questions with a tiebreaker question, if needed as well. 1️⃣5️⃣
3. The official test has no whatsoever mention of sorting hat, as of Aug 2025. My project not only has an [ASCII Art](<image copy 2.png>) of the hat, but the hat in its own style would give its own monologues throughout the quiz from time to time. ⏰
4. My project allows for replayability of the quiz, on the other hand there is no such option existing in the official quiz. 🔁
5. Sorting is only available for Hogwarts school in the official test whereas my Quiz also allows you to select your Wizarding school based on your location. 🗺️
---
## Functioning of the Quiz
My Quiz when started, will show an ASCII representation of the sorting hat, which will then print a song line by line with a delay of 1 second. (In the novels, the hat used to sing before sorting)

After singing, It will greet the player and then asks the player for the continent from which they belong, There are 5 options the player can choose, These options are different continents of the world and they would determine the wizarding school the player will go to depending on their loaction provided (Hogwarts only take students from the British Isles).

After this we get another, bigger ASCII representation of the sorting hat and the sorting officially begins.

Players have to enter options provided on the screen at the CLI, if wrong input is entered, Sorting hat will make a comment and replay the question, this will continue as long as the player does not enter a valid response only single letter from A-E (depending on the options). If a valid response is entered, the hat will proceed to the next question.

The question list is randomized and at every run, the player will see the same questions at different serial number than before.

After every 2-3 questions, sorting hat will make a comment similar to the ones the hat made in the original novels.

At the end of the 15th question, if there are 2 (or more) houses at the number 1 position based on the points accumulated (explained better below), The sorting hat will make one comment saying that it is unsure and will present the 16th **Tiebreaker** question, however if there is a clear winner and one house is at the top, we will get the results of the sorting.

The results include an [ASCII Art](<image copy 5.png>) of the house_mascot (Lion, Eagle, Badger, Snake) of the house the player is sorted into, then a congratulations message, with hat telling the player that they are sorted into a different house than hogwarts based on the location they provided. If the player have chosen a continent other than Europe. Otherwise there will only be a congratulations message. Below this is a funfact about the school you have been sorted into.

At last, the hat will ask the player to play again if they want to, if the player enter yes, the quiz will be rerun once again. However if prompted no, the hat will make a concluding comment and the quiz will exit via *sys.exit(0)*

---
## How the quiz determines your house? 🤔

Each option in every question will have **points** for each house as shown in this image:
![points per house](<image copy.png>)

As shown in the image, Each option gives different points to each house, These points, depend on the options chosen and are then stored in a **Global Dictionary** called *Houses*, This dictionary then stores points accumulated by each house after every question and in the end the *result* function calls this dictionary to declare which house the player has been sorted in, if there are 2 winners, then there will be a tiebreaker question to determine the clear winner.

---
## Extra details ✨

1. Throughout the sorting, an interactive [loading screen](<image copy 3.png>) will be displayed after user input to give an interactive user experience and to break walls of texts into different chunks.

2. In some particular questions, the sorting hat will make a [unique remark](<image copy 4.png>), based on the option submitted.

3. If the player enters Ctrl+D the sorting hat will make a peculiar statement before, exiting via *sys.exit(0)*.

---
## Credits 📄

The data of all the points of the houses have been colected directly from this [Reddit analysis of the Pottermore sorting hat quiz](https://www.reddit.com/r/Pottermore/comments/44os14/pottermore_sorting_hat_quiz_analysis/)

1.All the questions are adapted from the official Harry Potter website (formerly Pottermore). These questions, as well as the Harry Potter universe itself, are the copyright of J.K. Rowling and Warner Bros.

2.This project is a fan-made educational project for CS50P and is not affiliated with or endorsed by the official franchise.

---
