Цель проекта: предварительный анализ данных по влиянию условий жизни учащихся в возрасте от 15 до 22 лет на их успеваемость по математике для раннего выявления студентов, находящихся в группе риска.

Набор данных содержит как категориальную,так и количественную информацию об учащихся.
Стоит отметить довольно большое количество пропусков как в строковых, так и в численных данных. Ооднако дополнение последних на основе интерполяции или заменой соседним или наиболее часто встречающимся значением некорретна, так как большинтсво из них де-факто категориальны (колонки medu, fedu, famrel).

В своей работе я фактически оперировл двмя типами данных: строковыми и числовыми.
Для строковых данных было возможно написать функцию для очистки от пропущенных значений, тогда как при работе с цыфровыми столбцами потребовался индивидуальный подход.

