# Задача 4. PageRank

* **Дедлайн**: 19.11.2023, 23:59
* Основной полный балл: 5
* Максимум баллов: 10

## Задача

Везде считаем, что вершины графа занумерованы подряд с нуля.

- [ ] Используя `python-graphblas` реализовать функцию PageRank с параметрами из лекции.
- [ ] (+4 балла) Добавить в реализацию настройку всех параметров, которые есть в [реализации из библиотеки NetworkX](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.link_analysis.pagerank_alg.pagerank.html)
  - [ ] Про personalization и dangling рёбра можно почитать в [статье](https://www.cis.upenn.edu/~mkearns/teaching/NetworkedLife/pagerank.pdf).
- [ ] Добавить необходимые тесты и небольшие примеры.
- [ ] (+1 балл) Провести экспериментальное исследование полученной реализации и сравнить её с [реализацией из библиотеки NetworkX](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.link_analysis.pagerank_alg.pagerank.html) при различных значениях параметров на некоторых больших графах в формате `Matrix Market` с сайта [SuiteSparse Matrix Collection](https://sparse.tamu.edu/).
  - [ ] Например, небольшой граф `wb-cs-stanford` можно получить введя ключевое слово `web`.
