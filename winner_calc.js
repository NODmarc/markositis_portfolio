/*
ОПИСАНИЕ ЗАДАНИЯ:

Вам нужно вычислить победителя среди двух команд.
Представим 2 комманды по плаванию - "crazyKats" и "funnyDucks"

Каждая из комманд показала 3 итоговых результата, в трех заплывах. Например crazyKats показали три резултата (30, 60, 43).

Одна из комманд побеждает только в том случае, если среднее количесто очков по итогам трех результатов, минимум в 2 раза больше чем у соперника. Иначе ничья

ЗАДАЧА:

    1. Создайте стрелочную функцию которая будет считать среднее значение, 3-х результатов комманды. Расчитывается по формуле:
    "(res1 + res2 + res3) / 3"

    2. Используйте созданную функцию чтобы получить средний результат 2-х комманд.
    
    3. Создайте функцию с двумя параметрами - которые будут принимать аргументы из результата среднего значения очков комманд. В этой функции создайте вариацию условий, которые помогут определить победителя с помощью if/ else if и вывести сообщение с результатом в консоль.

ДАННЫЕ ДЛЯ ЗАДАЧИ:

    Первый вариант: "crazyKats"- 44, 23, 71  "funnyDucks" 65, 54, 49
    Второй вариант: "crazyKats"- 85, 54, 41  "funnyDucks" 23, 34, 27


*/


const teamAverageResult = (result1, result2, result3) => (result1 + result2 + result3) / 3

const crazyKats_avg = teamAverageResult(85, 54, 41)
      funnyDucks_avg = teamAverageResult(23, 34, 27)

function checkWinner(crazyKats_avg, funnyDucks_avg) {
    if (crazyKats_avg >= 2 * funnyDucks_avg) {
        console.log(`crazyKats is win! funnyDucks is lose :(
            crazyKats: ${crazyKats_avg}, funnyDucks: ${funnyDucks_avg}`)
    } else if (funnyDucks_avg >= 2 * crazyKats_avg) {
        console.log(`funnyDucks is win! crazyKats is lose :( 
            crazyKats: ${crazyKats_avg}, funnyDucks: ${funnyDucks_avg}`)
    } else {
        console.log("Standoff")
    }
}

checkWinner(500, 500)




