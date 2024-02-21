# Neural CAPTCHA Solver / Модель для решения капчи

- [English Version. Neural Network Model for CAPTCHA Solution](#neural-network-model-for-captcha-solution)
- [Russian Version. Нейронная модель для решения CAPTCHA](#нейронная-модель-для-решения-captcha)

---

## Neural Network Model for CAPTCHA Solution
<a name="neural-network-model-for-captcha-solution"></a>

This project involves the application of a neural network model to solve a set of CAPTCHAs. Each CAPTCHA consists of a group of images and a hint image that contains the answer. The objective is to select the correct image based on the hint.

## Task Description

On each answer option, icons are displayed on numbered orbits. There are a total of 5 orbits. The correct answer is the image where the icon from the hint image is located on the orbit with the number indicated on the hint image.

## Requirements

1. **Prediction**: The model must predict the coordinate of the point corresponding to the answer.
2. **Accuracy Measurement**: Accuracy is measured by comparing the predicted answer only with the markup in the form of a point.
3. **Model**: Pre-trained networks are utilized, or a specific network is trained for the task.
4. **Generalization**: The algorithm possesses the property of generalization.
5. **Prediction Accuracy**: The average accuracy of predicted coordinates is no less than 95%.
6. **Accuracy Calculation**: If the predicted point lies within the same patch as the icon on the correct orbit, the prediction is considered true. The ratio of the number of true predictions to all will be the accuracy.
7. **Note**: Along with the solution, an accuracy measurement script is provided.

## Dataset

The training data consists of 970 CAPTCHAs with LabelMe format markup. The final accuracy measurement will be made on a closed set of images, which may contain icons not represented in the training set.

![Data Example](assets/data_example.png)

## Getting Started
To get started with the project, follow the steps below:

1. Clone the repository to your local machine.
2. Install the necessary libraries and dependencies by running `pip install -r requirements.txt` in your terminal.
3. Once the installation is complete, you can launch the project by running `python main.py` in your terminal.

---

## Нейронная модель для решения CAPTCHA
<a name="нейронная-модель-для-решения-captcha"></a>

---

Этот проект включает в себя применение нейронной сети для решения набора CAPTCHA. Каждая CAPTCHA состоит из группы изображений и изображения-подсказки, которое содержит ответ. Цель состоит в том, чтобы выбрать правильное изображение на основе подсказки.

## Описание задачи

На каждом варианте ответа отображаются иконки на нумерованных орбитах. Всего есть 5 орбит. Правильный ответ - это изображение, на котором иконка из изображения-подсказки расположена на орбите с номером, указанным на изображении-подсказке.

## Требования

1. **Прогнозирование**: Модель должна предсказывать координаты точки, соответствующей ответу.
2. **Измерение точности**: Точность измеряется путем сравнения предсказанного ответа только с разметкой в виде точки.
3. **Модель**: Используются предварительно обученные сети, или обучается специфическая сеть для задачи.
4. **Обобщение**: Алгоритм обладает свойством обобщения.
5. **Точность прогнозирования**: Средняя точность предсказанных координат не менее 95%.
6. **Расчет точности**: Если предсказанная точка находится в том же участке, что и иконка на правильной орбите, прогноз считается верным. Отношение числа верных прогнозов ко всем будет точностью.
7. **Примечание**: Вместе с решением предоставляется скрипт для измерения точности.

## Набор данных

Тренировочные данные состоят из 970 CAPTCHA с разметкой в формате LabelMe. Окончательное измерение точности будет производиться на закрытом наборе изображений, которые могут содержать иконки, не представленные в тренировочном наборе.

![Пример данных](assets/data_example.png)

## Начало работы
Чтобы начать работу над проектом, следуйте шагам ниже:

1. Клонируйте репозиторий на свой локальный компьютер.
2. Установите необходимые библиотеки и зависимости, запустив `pip install -r requirements.txt` в терминале.
3. После завершения установки вы можете запустить проект, запустив `python main.py` в терминале.

---


