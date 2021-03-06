# Учебный проект: Список запланированных дел (ToDo List) на Python, Flask с использованием БД Redis

- [Установка](#установка)
- [Использование](#использование)
- [Скриншот интерфейса](#скриншот-интерфейса)
- [Замечания](#замечания)

## Установка
На ПК предварительно должен быть установлен Docker и Git.

   1. В консоли клонируйте репозиторий:

      ```
      git clone https://github.com/chrissark/python-flask-project.git     
      ```
   2. Перейдите в папку с проектом:
      ```
      cd python-flask-project
      ```
   3. Выполните команду:
      ```
      docker-compose up
      ```
## Использование
1. Для запуска приложения в окне своего браузера перейдите по ссылке **http://localhost:5000/**.
2. Для **добавления** нового задания введите в тектовом поле текст задания и нажмите кнопку **Add**. Задание появится на экране.
3. Вы можете отмечать **выполнение** задания. 

   Для изменения статуса задания нажмите на его текст. При повторном нажатии на текст задания оно будет отмечено как невыполненное. Невыполненные задания отображаются в сером цвете,        выполненные - в зеленом и отмечены символом ✔.
4. Для удаления задания нажмите на кнопку **Remove** справа от текста задания.

## Скриншот интерфейса
![img](https://github.com/chrissark/python-flask-project/blob/main/Screenshot%202021-11-21%20at%2016-31-53%20ToDo%20List.png)

## Замечания
Задание было создано как отдельный класс Task в Python для добавления различных методов. Пока реализована только отметка задания как выполненного. В планах переработать дизайн и добавить больше функций для заданий (типы заданий, даты выполнения заданий и т.п.).

Объекты класса Task содержатся в БД Redis по сгенерированным hash-ключам с рандомизацией с помощью SALT. Сами ключи содержаться в отдельном списке в БД для последовательного вывода заданий на экран.
