"use strict";
/*
ЗАДАЧИ:

Создайте функцию calcAverageHumanAge которая будет принимать в себя массив с годами собак и будет делать с этими данными следующее:

1. Пересчитайте собачий возраст, в возраст человека по формуле: 
если возраст собаки меньше или равен 2 годам, то человеческий возраст = 2 * возраст собаки. Если собаке больше 2-х лет то человеческий возраст = 16 + собачий возраст * 4

2.Вычислите всех собак которым меньше 18 человеческих лет.

3. Вычислите среднее значение возраста всех взрослых собак в пересчете на человеческие года.

4.Запустите функцию для двух массивов данных:
*/

const dogs1 = [5, 2, 4, 1, 15, 8, 3];
const dogs2 = [16, 6, 10, 5, 6, 1, 4];

function calcAverageHumanAge(dogs) {
  const humanAge = dogs.map(function (val) {
    if (val <= 2) {
      return 2 * val;
    } else if (val > 2) {
      return 16 + val * 4;
    }
  });
  const calcLowerThen18 = humanAge.filter(function (val) {
    return val < 18;
  });
  const calcAverage = humanAge.reduce(function (acc, val) {
    return acc + val
  }, 0) / humanAge.length
  console.log(humanAge);
  console.log(calcLowerThen18);
  console.log(calcAverage)
}

console.log(calcAverageHumanAge([...dogs1, ...dogs1]));
