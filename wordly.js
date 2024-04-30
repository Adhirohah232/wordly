const fs = require('fs');

const result = fs.readFileSync('./words.txt','utf-8')

// console.log(result);
const terms = {};
result.split('\n').forEach(line => {
  const [serial, definition] = line.split('. ');
  const [term, meaning] = definition.split(': ');
  terms[term.trim()] = meaning.trim();
});

function getRandomWord() {
    const keys = Object.keys(terms);
    const randomIndex = Math.floor(Math.random() * keys.length);
    return keys[randomIndex];
  }
  
  function getRandomChoices(correctWord) {
    const choices = [correctWord];
    while (choices.length < 4) {
      const randomWord = getRandomWord();
      if (!choices.includes(randomWord)) {
        choices.push(randomWord);
      }
    }
    return choices.sort(() => Math.random() - 0.5);
  }
  
  function createQuestion() {
    const correctWord = getRandomWord();
    const choices = getRandomChoices(correctWord);
    const answerIndex = choices.indexOf(correctWord);
  
    const question = `
      What is the meaning of "${correctWord}"?
      A) ${choices[0]}
      B) ${choices[1]}
      C) ${choices[2]}
      D) ${choices[3]}
      Enter the letter corresponding to your answer:
    `;
    const userAnswer = prompt(question);
  
    if (userAnswer && userAnswer.toLowerCase() === ['a', 'b', 'c', 'd'][answerIndex]) {
      alert('Correct!');
    } else {
      alert(`Incorrect. The correct answer was ${['A', 'B', 'C', 'D'][answerIndex]}.`);
    }
  }
  
  // Run the quiz
  createQuestion();